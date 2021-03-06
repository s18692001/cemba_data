"""
a. generate a bed file mimic pseudo-reads covering genome
Input:
- Read length distribution
- Read number distribution
- Genome coverage distribution (or for single cell, 2)
Output:
a bed file

b. Simulate pseudo-profiles based a given bed
Input:
- ALLC file path, the high coverage ALLC profile to simulate from
- The bed file
Output:
pseudo-ALLC
"""
import shlex
import subprocess
import pathlib
import pybedtools
import pandas as pd
import numpy as np
import logging

# logger
log = logging.getLogger()


def simulate_allc(genome_cov_path,
                  target_allc_path, out_path, allc_profile_path=None):
    """

    Parameters
    ----------
    genome_cov_path
    target_allc_path
    out_path
    allc_profile_path

    Returns
    -------

    """
    reader = subprocess.Popen(shlex.split(f'tabix -R {genome_cov_path} {target_allc_path}'),
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              encoding='utf8')
    genome_cov_bed = pd.read_table(genome_cov_path, header=None,
                                   names=['chrom', 'start', 'end', 'cov'])
    if allc_profile_path is None:
        allc_profile_path = str(target_allc_path) + '.profile'
        if not pathlib.Path(allc_profile_path).exists():
            raise FileNotFoundError(f'target ALLC file {allc_profile_path} do not have profile. '
                                    f'use yap allc-profile to generate')
    allc_profile = pd.read_table(allc_profile_path, index_col=0)
    context_a = allc_profile['base_beta_a'].to_dict()
    context_ab = allc_profile[['base_beta_a', 'base_beta_b']].sum(axis=1).to_dict()

    cur_chrom = None
    cur_row = None
    cur_row_num = None
    chrom_read_cov = pd.DataFrame()
    out_path = out_path.rstrip('.gz')
    out_file = pathlib.Path(out_path).absolute()
    f = out_file.open('w')
    for line in reader.stdout:
        chrom, pos, strand, context, mc, cov, p = line.split('\t')
        if 'N' in context:
            # N is very rare, just pass it
            continue
        if chrom != cur_chrom:
            cur_chrom = chrom
            log.info(f'Simulating chromosome: {cur_chrom}')
            chrom_read_cov = genome_cov_bed[genome_cov_bed['chrom'] == cur_chrom]
            cur_row_num = 0
            cur_row = chrom_read_cov.iloc[cur_row_num, :]

        pos = int(pos)
        if pos > cur_row['end']:
            # read to the next row
            cur_row_num += 1
            cur_row = chrom_read_cov.iloc[cur_row_num, :]
        read_cov = cur_row[-1]

        # the mc and cov is adjusted by assuming that mC% follow a prior distribution Beta(1, 1)
        # see https://www.nature.com/articles/nmeth.3035
        # this prevent the problem that most mC are 0, peak
        adj_mc = float(mc) + context_a[context]  # mc + a
        adj_cov = float(cov) + context_ab[context]  # cov + a + b
        read_mc = np.random.binomial(1, adj_mc / adj_cov, read_cov).sum()
        pseudo_line = [chrom, str(pos), strand, context, str(read_mc), str(read_cov), p]
        f.write('\t'.join(pseudo_line))
    f.close()

    subprocess.run(['bgzip', str(out_file)])
    return


def simulate_long_reads_coverage(read_number_mean, read_number_sd,
                                 read_length_mean, read_length_sd,
                                 out_path, chrom_size_path, genome_cov=2, remove_chr=False):
    """

    Parameters
    ----------
    read_number_mean
    read_number_sd
    read_length_mean
    read_length_sd
    out_path
    chrom_size_path
    genome_cov
    remove_chr

    Returns
    -------

    """
    chrom_sizes = pd.read_table(chrom_size_path, header=None, index_col=0, squeeze=True, names=['chrom_size'])
    read_number = int(np.random.normal(read_number_mean, read_number_sd, 1))
    # the portion of reads to keep in each genome copy
    keep_read_portion = read_number / genome_cov / (chrom_sizes.sum() / read_length_mean)

    records = []
    for _ in range(genome_cov):
        # loop for each genome copy
        for chrom, length in chrom_sizes.iteritems():
            fold = 1.1
            rand_reads = np.array([0])
            # generate enough number of reads that total length longer than chromosome
            while rand_reads.sum() < length:
                reads_needed = max(length * fold / read_length_mean, 1)
                new_rand_reads = np.random.normal(read_length_mean, read_length_sd, int(reads_needed))
                rand_reads = np.hstack([rand_reads, new_rand_reads])
            rand_reads = rand_reads[np.where(rand_reads.cumsum() < length)].astype(int)
            chrom_df = pd.DataFrame([rand_reads]).T
            if rand_reads.sum() != length:
                # add last row to the end of dataframe
                chrom_df.append([[length - rand_reads.sum()]])
            chrom_df['start'] = chrom_df[0].cumsum()
            chrom_df['end'] = chrom_df[0].cumsum()[1:].append(pd.Series([length])).reset_index(drop=True)
            if remove_chr:
                chrom_df['chrom'] = chrom
            else:
                chrom_df['chrom'] = chrom
            records.append(chrom_df[['chrom', 'start', 'end']].sample(frac=keep_read_portion))
    total_bed = pd.concat(records, ignore_index=True)
    # merge the total bed to get actual genome coverage bedgraph
    genome_cov_bed = pybedtools.BedTool.from_dataframe(total_bed) \
        .sort() \
        .genome_coverage(bg=True, g=chrom_size_path) \
        .sort() \
        .to_dataframe()
    genome_cov_path = pathlib.Path(out_path)
    if remove_chr:
        genome_cov_bed.iloc[:, 0] = genome_cov_bed.iloc[:, 0].str[3:]
    genome_cov_bed.to_csv(genome_cov_path, sep='\t', index=None, header=None)
    return


def simulate_obs_rate_under_cov(cov_mean, cov_std, rate_a, rate_b, n_obs=100000):
    """
    Simulate observed rate under cov (normal distribution) and mc_rate (beta distribution)
    Parameters
    ----------
    cov_mean
    cov_std
    rate_a
    rate_b
    n_obs

    Returns
    -------
    rand_obs_rate
        list of observed rate
    """
    # covs are randomly selected from normal dist
    rand_covs = np.random.normal(loc=cov_mean, scale=cov_std, size=n_obs)
    rand_covs = rand_covs[np.where(rand_covs > 0)]  # cut the rand_covs by 0
    # rates are randomly selected from beta dist
    rand_rates = np.random.beta(a=rate_a, b=rate_b, size=rand_covs.size)

    # mC are randomly selected from binomial dist given cov and rate
    rand_mcs = np.zeros(shape=(rand_covs.size,))
    for i, (cov, rate) in enumerate(np.vstack([rand_covs, rand_rates]).T):
        rand_mcs[i] = int(np.random.binomial(int(cov), rate, size=1))
    rand_obs_rate = rand_mcs / rand_covs
    return rand_obs_rate
