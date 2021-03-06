"""
Input:
- a dict json file. key: cluster ID, value: list of cell IDs
- metadata contain file path
- output dir

1. gather all file paths based on metadata
2. merge allc
3. extract CG strand merge allc
4. bigwig for CG and CH
5. file path summary file
"""
import pandas as pd
import pathlib
import json


def _generate_merge_strategy(cluster_table, min_group, keep_unique_cluster=True):
    """
    Generate merge strategy for multilayer cluster assignment. The cluster assignment do not need to be hierarchical.
    Through hierarchical form is better.
    1. cells that assigned same cluster among all columns are merged into cell groups, this is stage 0
    2. after stage 0, clusters are merged by cell groups in a minimum way, this is other stages

    """
    dropped_cells = []  # list of cell_id
    dropped_clusters = []  # (column, cluster_name)

    # make group dict, cell in each group have all-level same cluster assignment
    cell_group_dict = {}
    for group_id, (group_pattern, sub_df) in enumerate(cluster_table.groupby(cluster_table.columns.tolist())):
        if sub_df.shape[0] < min_group:
            dropped_cells += sub_df.index.tolist()
            # if a group have too less cell, this group is dropped
            continue
        cell_group_dict[group_id] = {
            'pattern': group_pattern,
            'cell_ids': sub_df.index,
            'cell_count': sub_df.shape[0],
            'out_path': None  # will be assign in _batch_merge_allc
        }

    # make cluster dict, cluster is merged from 1 or more groups
    cluster_dict = {}
    existing_group_pattern = {}
    for column_num, column in enumerate(cluster_table.columns):
        for cluster_name, sub_df in cluster_table.groupby(column):
            cluster_uid = f'{column}-{cluster_name}'
            contain_groups = set([group_id for group_id, group_id_dict in cell_group_dict.items()
                                  if group_id_dict['pattern'][column_num] == cluster_name])
            if len(contain_groups) == 0:
                dropped_clusters.append((column, cluster_name))
                # this cluster have no group, which happens to small cluster whose group dropped by min_group
                continue
            if keep_unique_cluster and (contain_groups in existing_group_pattern):
                # always keep cluster exists in later columns, delete the previous one.
                # assume that later columns are always in higher level.
                # this do not check the cell, but check on group level. cell_count could be diff.
                del cluster_dict[existing_group_pattern[contain_groups]]
            existing_group_pattern[contain_groups] = cluster_uid

            cluster_dict[cluster_uid] = {
                'groups': contain_groups,
                'cell_count': sub_df.shape[0],
                'out_path': None,  # will be assign in _batch_merge_allc
                'cluster_level': column
            }
    return cell_group_dict, cluster_dict, dropped_cells, dropped_clusters


def _batch_merge_allc(cluster_table, cell_path_series, out_dir, min_group, cpu):
    """
    Batch merge ALLC function, also accept multilayer cluster assignment.
    """
    # making directories
    out_dir = pathlib.Path(out_dir).absolute()
    out_dir.mkdir(exist_ok=False)
    group_dir = out_dir / 'merge_tmp_cell_group'
    group_dir.mkdir()
    for column in cluster_table.columns:
        column_dir = out_dir / column
        column_dir.mkdir()

    # generate merge dict
    cell_group_dict, cluster_dict, dropped_cells, dropped_clusters = \
        _generate_merge_strategy(cluster_table, min_group)

    # generate cell_group merge commands
    records = []
    for group_id, group_dict in cell_group_dict.items():
        cell_paths = cell_path_series.reindex(group_dict['cell_ids'])
        cell_id_list_path = group_dir / f'{group_id}.cell_list'
        with cell_id_list_path.open('w') as f:
            for path in cell_paths:
                f.write(str(path) + '\n')
        group_allc_out_path = group_dir / f'{group_id}.allc.tsv.gz'
        cell_group_dict[group_id]['out_path'] = group_allc_out_path
        cmd = f'yap merge-allc --allc_paths {cell_id_list_path} ' \
              f'--out_path {group_allc_out_path} --cpu {cpu} --index tabix'
        cmd_dict = {
            'command': cmd,
            '-pe smp': cpu
        }
        records.append(cmd_dict)
    group_command_path = out_dir / 'group_merge.command.json'
    with group_command_path.open('w') as f:
        json.dump(records, f)

    # generate cluster merge commands
    records = []
    for cluster_id, cluster_id_dict in cluster_dict.items():
        cluster_column = cluster_id_dict['cluster_level']
        cluster_column_dir = out_dir / cluster_column
        cluster_allc_out_path = cluster_column_dir / f'{cluster_id}.allc.tsv.gz'
        cluster_dict[cluster_id]['out_path'] = cluster_allc_out_path
        group_out_paths = [cell_group_dict[group_id]['out_path'] for group_id in cluster_id_dict['groups']]
        if len(group_out_paths) == 1:
            # no need to merge, copy the file instead,
            # through increase space usage, but most straightforward
            cmd = f'cp {group_out_paths[0]} {cluster_allc_out_path}'
            cmd_dict = {
                'command': cmd,
                '-pe smp': 1
            }
        else:
            group_id_list_path = cluster_column_dir / f'{cluster_id}.group_list'
            with group_id_list_path.open('w') as f:
                for path in group_out_paths:
                    f.write(str(path) + '\n')
            cmd = f'yap merge-allc --allc_paths {group_id_list_path} ' \
                  f'--out_path {cluster_allc_out_path} --cpu {cpu} --index tabix'
            cmd_dict = {
                'command': cmd,
                '-pe smp': cpu
            }
        records.append(cmd_dict)
    cluster_command_path = out_dir / 'cluster_merge.command.json'
    with cluster_command_path.open('w') as f:
        json.dump(records, f)
    return


def _batch_allc_profile(out_dir):
    records = []
    allc_files = pathlib.Path(out_dir).absolute().glob('**/*allc.tsv.gz')
    for allc_file in allc_files:
        cmd = f'yap allc-profile --allc_path {allc_file}'
        cmd_dict = {
            'command': cmd,
            '-pe smp': 1
        }
        records.append(cmd_dict)
    command_path = out_dir / 'allc_profile.command.json'
    with command_path.open('w') as f:
        json.dump(records, f)
    return


def _batch_allc_to_bigwig(out_dir, chrom_size_path, mc_contexts):
    records = []
    allc_files = pathlib.Path(out_dir).absolute().glob('**/*allc.tsv.gz')
    for mc_context in mc_contexts:
        for allc_file in allc_files:
            out_path = str(allc_file).rstrip('allc.tsv.gz') + f'{mc_context}.bw'
            cmd = f'yap allc-to-bigwig --allc_path {allc_file} ' \
                  f'--out_path {out_path} --chrom_size {chrom_size_path} --mc_type {mc_context}'
            cmd_dict = {
                'command': cmd,
                '-pe smp': 1
            }
            records.append(cmd_dict)
    command_path = out_dir / 'allc_bigwig.command.json'
    with command_path.open('w') as f:
        json.dump(records, f)
    return


def _batch_extract_mc(out_dir, mc_contexts, merge_strand):
    if isinstance(mc_contexts, str):
        mc_contexts = [mc_contexts]
    records = []
    allc_files = pathlib.Path(out_dir).absolute().glob('**/*allc.tsv.gz')
    for mc_context in mc_contexts:
        for allc_file in allc_files:
            out_path = str(allc_file).rstrip('tsv.gz') + f'{mc_context}.tsv.gz'
            cmd = f'yap allc-extract --allc_path {allc_file} ' \
                  f'--out_path {out_path} --merge_strand {merge_strand} --mc_context {mc_context}'
            cmd_dict = {
                'command': cmd,
                '-pe smp': 1
            }
            records.append(cmd_dict)
    command_path = out_dir / 'allc_extract.command.json'
    with command_path.open('w') as f:
        json.dump(records, f)
    return


def cluster_merge_pipeline(cluster_table_path, cell_path_file, out_dir,
                           chrom_size_path, bigwig_contexts=('CGN', 'CHN'),
                           extract_contexts=('CGN',), merge_strand=True,
                           min_group=10, cpu=50):
    """
    TODO: clustering name system, also OS path safe characters
    """
    cluster_table = pd.read_table(cluster_table_path, index_col=0)
    if cluster_table.columns.duplicated().sum() != 0:
        raise ValueError('Cluster table have duplicated columns')
    if cluster_table.columns.duplicated().sum() != 0:
        raise ValueError('Cluster table have duplicated cell_ids')

    cell_path_series = pd.read_table(cell_path_file, index_col=0, header=None, squeeze=True)

    _batch_merge_allc(cluster_table, cell_path_series=cell_path_series,
                      out_dir=out_dir, min_group=min_group, cpu=min(cpu // 8, 30))
    _batch_allc_profile(out_dir=out_dir)
    _batch_allc_to_bigwig(out_dir, chrom_size_path, mc_contexts=bigwig_contexts)
    _batch_extract_mc(out_dir, mc_contexts=extract_contexts, merge_strand=merge_strand)

    command_path_list = [
        out_dir / 'group_merge.command.json',
        out_dir / 'cluster_merge.command.json',
        out_dir / 'allc_profile.command.json',
        out_dir / 'allc_bigwig.command.json',
        out_dir / 'allc_extract.command.json'
    ]

    # submit master of master
    command_path = ' '.join(command_path_list)
    qsub_command = f'yap qsub --working_dir {out_dir} ' \
                   f'--project_name master ' \
                   f'--command_file_path {command_path} ' \
                   f'--total_cpu 120'

    print(f"""
        The command file for prepare-cluster-profile is prepared
        ---------------------------------------------------------------------------------------
        - Output directory: {out_dir}
        - Yap command list: {command_path}

        To run the command list using qsub, use "yap qsub" like this:

        {qsub_command}

        Modify the qsub parameters if you need. See "yap qsub -h" for help.
        """)

    return
