"""
This file is modified from methylpy https://github.com/yupenghe/methylpy

Author: Yupeng He



                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright {2017} {Matthew D. Schultz and Yupeng He}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Input: bam_result dataframe
Processes: call allc.
Output: allc dataframe
"""

import subprocess
import shlex
import pathlib
import gzip
import pandas as pd
import multiprocessing
import collections


def _read_faidx(faidx_path):
    """
    Read fadix of reference fasta file
    samtools fadix ref.fa
    """
    return pd.read_table(faidx_path, index_col=0, header=None,
                         names=['NAME', 'LENGTH', 'OFFSET', 'LINEBASES', 'LINEWIDTH'])


def _get_chromosome_sequence(fasta_path, fai_df, query_chrom):
    """
    read a whole chromosome sequence into memory
    """
    if query_chrom not in fai_df.index:
        return None
    else:
        chrom_pointer = fai_df.loc[query_chrom, 'OFFSET']
        tail = fai_df.loc[query_chrom, 'LINEBASES'] - fai_df.loc[query_chrom, 'LINEWIDTH']
        seq = ""
        with open(fasta_path, 'r') as f:
            f.seek(chrom_pointer)
            for line in f:
                if line[0] == '>':
                    break
                seq += line[:tail]  # trim \n
        return seq


def _call_methylated_sites_worker(bam_path, reference_fasta,
                                  num_upstr_bases, num_downstr_bases,
                                  buffer_line_number, min_mapq, min_base_quality):
    """
    Main ALLC calling function. Take one bam file, use samtools mpileup to call variants
    and pipe to this function to generate mC and cov count. Only for single cell, not base level statistics.

    Parameters
    ----------
    bam_path
        path of input bam file
    reference_fasta
        path of reference fasta, no assumption, should be the same as mapping
    num_upstr_bases
        number of base before mC
    num_downstr_bases
        number of base after mC
    buffer_line_number
        number of buffer line
    min_mapq
        minimum MAPQ for a read being considered, samtools mpileup parameter
    min_base_quality
        minimum base quality for a base being considered, samtools mpileup parameter
    Returns
    -------
    count_df
        A dataframe contain all mC context summary counts.
    """
    # Check fasta index
    if not pathlib.Path(reference_fasta + ".fai").exists():
        raise FileNotFoundError("Reference fasta not indexed. Use samtools faidx to index it and run again.")
    fai_df = _read_faidx(pathlib.Path(reference_fasta + ".fai"))

    if not pathlib.Path(bam_path + ".bai").exists():
        subprocess.check_call(shlex.split("samtools index " + bam_path))

    # mpileup
    mpileup_cmd = f"samtools mpileup -Q {min_base_quality} " \
                  f"-q {min_mapq} -B -f {reference_fasta} {bam_path}"
    pipes = subprocess.Popen(shlex.split(mpileup_cmd),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             universal_newlines=True)
    result_handle = pipes.stdout

    # Output handel
    input_path = pathlib.Path(bam_path)
    file_dir = input_path.parent
    allc_name = 'allc_' + input_path.name.split('.')[0] + '.tsv.gz'
    output_path = str(file_dir / allc_name)
    output_file_handler = gzip.open(output_path, 'wt')

    # initialize variables
    complement = {"A": "T",
                  "T": "A",
                  "C": "G",
                  "G": "C",
                  "N": "N"}
    mc_sites = {'C', 'G'}
    context_len = num_upstr_bases + 1 + num_downstr_bases
    cur_chrom = ""
    line_counts = 0
    out = ""
    seq = None  # whole cur_chrom seq
    chr_out_pos_list = []
    cur_out_pos = 0
    cov_dict = collections.defaultdict(int)  # context: cov_total
    mc_dict = collections.defaultdict(int)  # context: mc_total

    # process mpileup result
    for line in result_handle:
        fields = line.split("\t")
        fields[2] = fields[2].upper()
        # if chrom changed, read whole chrom seq from fasta
        if fields[0] != cur_chrom:
            cur_chrom = fields[0]
            chr_out_pos_list.append((cur_chrom, str(cur_out_pos)))
            # get seq for cur_chrom
            seq = _get_chromosome_sequence(reference_fasta, fai_df, cur_chrom)
            if seq is not None:
                seq = seq.upper()

        if seq is None:
            continue
        if fields[2] not in mc_sites:
            continue

        # indels
        read_bases = fields[4]
        incons_basecalls = read_bases.count("+") + read_bases.count("-")
        if incons_basecalls > 0:
            read_bases_no_indel = ""
            index = 0
            prev_index = 0
            while index < len(read_bases):
                if read_bases[index] == "+" or read_bases[index] == "-":
                    # get insert size
                    indel_size = ""
                    ind = index + 1
                    while True:
                        try:
                            int(read_bases[ind])
                            indel_size += read_bases[ind]
                            ind += 1
                        except:
                            break
                    try:
                        # sometimes +/- does not follow by a number and
                        # it should be ignored
                        indel_size = int(indel_size)
                    except:
                        index += 1
                        continue
                    read_bases_no_indel += read_bases[prev_index:index]
                    index = ind + indel_size
                    prev_index = index
                else:
                    index += 1
            read_bases_no_indel += read_bases[prev_index:index]
            fields[4] = read_bases_no_indel

        # count converted and unconverted bases
        if fields[2] == "C":
            pos = int(fields[1]) - 1
            try:
                context = seq[(pos - num_upstr_bases):(pos + num_downstr_bases + 1)]
            except:  # complete context is not available, skip
                continue
            unconverted_c = fields[4].count(".")
            converted_c = fields[4].count("T")
            cov = unconverted_c + converted_c
            if cov > 0 and len(context) == context_len:
                line_counts += 1
                data = "\t".join([cur_chrom, str(pos + 1), "+", context,
                                  str(unconverted_c), str(cov), "1"]) + "\n"
                cov_dict[context] += cov
                mc_dict[context] += unconverted_c
                out += data
                cur_out_pos += len(data)

        elif fields[2] == "G":
            pos = int(fields[1]) - 1
            try:
                context = "".join([complement[base]
                                   for base in reversed(
                        seq[(pos - num_downstr_bases):(pos + num_upstr_bases + 1)]
                    )]
                                  )
            except:  # complete context is not available, skip
                continue
            unconverted_c = fields[4].count(",")
            converted_c = fields[4].count("a")
            cov = unconverted_c + converted_c
            if cov > 0 and len(context) == context_len:
                line_counts += 1
                data = "\t".join([cur_chrom, str(pos + 1), "-", context,
                                  str(unconverted_c), str(cov), "1"]) + "\n"
                cov_dict[context] += cov
                mc_dict[context] += unconverted_c
                out += data
                cur_out_pos += len(data)

        if line_counts > buffer_line_number:
            output_file_handler.write(out)
            line_counts = 0
            out = ""

    if line_counts > 0:
        output_file_handler.write(out)
    result_handle.close()
    output_file_handler.close()

    with open(output_path + '.idx', 'w') as idx_f:
        for (chrom, out_pos) in chr_out_pos_list:
            idx_f.write(f'{chrom}\t{out_pos}\n')
        idx_f.write('#eof\n')  # methylpy idx end

    count_df = pd.DataFrame({'mc': mc_dict, 'cov': cov_dict})
    count_df['mc_rate'] = count_df['mc'] / count_df['cov']
    return count_df


def call_methylated_sites(bam_result_df, out_dir, config):
    """
    Parallel function for ALLC calling.

    Parameters
    ----------
    bam_result_df
        dataframe from bam qc step
    out_dir
        universal pipeline out_dir
    config
        universal pipeline config
    Returns
    -------
    allc_count_df
        id columns are: uid, index_name
    """
    reference_fasta = config['callMethylation']['reference_fasta']
    num_upstr_bases = int(config['callMethylation']['num_upstr_bases'])
    num_downstr_bases = int(config['callMethylation']['num_downstr_bases'])
    buffer_line_number = int(config['callMethylation']['buffer_line_number'])
    min_mapq = int(config['callMethylation']['min_mapq'])
    min_base_quality = int(config['callMethylation']['min_base_quality'])
    cores = int(config['callMethylation']['cores'])

    pool = multiprocessing.Pool(cores)
    results = {}
    for (uid, index_name), _ in bam_result_df.groupby(['uid', 'index_name']):
        final_bam_path = pathlib.Path(out_dir) / f'{uid}_{index_name}.final.bam'
        result = pool.apply_async(_call_methylated_sites_worker,
                                  (str(final_bam_path), reference_fasta,
                                   num_upstr_bases, num_downstr_bases,
                                   buffer_line_number, min_mapq, min_base_quality))
        results[(uid, index_name)] = result
    pool.close()
    pool.join()

    total_results = []
    for (uid, index_name), result in results.items():
        count_df = result.get()
        count_df['uid'] = uid
        count_df['index_name'] = index_name
        total_results.append(count_df)
    allc_count_df = pd.concat(total_results).reset_index(drop=False)
    return allc_count_df
