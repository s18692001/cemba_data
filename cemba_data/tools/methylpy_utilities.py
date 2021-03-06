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
"""

import sys
import os
import math
import shlex
import numpy as np
import subprocess
import time
import itertools
import multiprocessing
import gzip
import collections
from pkg_resources import parse_version
import glob


def get_executable_version(exec_name):
    try:
        out = subprocess.check_output(shlex.split(exec_name + " --version"))
        out = out.decode("utf-8")
    except:
        print_error("Failed to run %s\n" % (exec_name))
    first_line = out.split("\n")[0]
    fields = first_line.split(" ")
    return (fields[-1])


def infer_samples(allc_files):
    if isinstance(allc_files, str):
        allc_file_basename = allc_files[(allc_files.rfind("/") + 1):]
        # remove prefix allc_ and suffix .tsv[.gz]
        sample = allc_file_basename[5:allc_file_basename.find('.tsv')]
        sample = sample
        return (sample)
    elif isinstance(allc_files, list):
        samples = []
        for allc_file in allc_files:
            samples.append(infer_samples(allc_file))
        return (samples)
    else:
        print_error("Failed to infer sample names\n")


def bgzip_allc_file(allc_file,
                    path_to_bgzip="",
                    path_to_tabix="",
                    buffer_line_number=100000):
    if allc_file[-3:] == ".gz":
        output_file = allc_file[:-3] + ".bgz"
        g = open(output_file, 'w')
        output_pipe = subprocess.Popen(
            [path_to_bgzip + "bgzip"],
            stdin=subprocess.PIPE,
            stdout=g)
        # output
        f = open_allc_file(allc_file)
        out = ""
        line_counts = 0
        for line in f:
            out += line
            line_counts += 1
            if line_counts > buffer_line_number:
                output_pipe.stdin.write(out)
                line_counts = 0
                out = ""
        if line_counts > 0:
            output_pipe.stdin.write(out)
            out = ""
        # finish
        f.close()
        g.close()
        output_pipe.stdin.close()
    else:
        output_file = allc_file + ".bgz"
        with open(output_file, "w") as g:
            subprocess.check_call([path_to_bgzip + "bgzip", "-c", allc_file], stdout=g)
    # tabix indexing
    subprocess.check_call(shlex.split(path_to_tabix + "tabix -s 1 -b 2 -e 2 " + output_file))


def check_call_mc_dependencies(path_to_samtools="",
                               trim_reads=True,
                               path_to_cutadapt="",
                               aligner="bowtie2",
                               path_to_aligner="",
                               remove_clonal=True,
                               path_to_picard=""):
    # check samtools version
    if len(path_to_samtools) != 0:
        path_to_samtools += "/"
    # check picard
    samtools_version = get_executable_version(path_to_samtools + "samtools")
    if parse_version(samtools_version) < parse_version("1.2"):
        print_error("samtools version %s found.\nmethylpy need at least samtools 1.3\nExit!\n"
                    % (samtools_version))

    # check bowtie/bowtie2
    if len(path_to_aligner) != 0:
        path_to_aligner += "/"
    if aligner.lower() == "bowtie2":
        aligner_version = get_executable_version(path_to_aligner + "bowtie2")
    elif aligner.lower() == "bowtie":
        aligner_version = get_executable_version(path_to_aligner + "bowtie")
    elif aligner.lower() == "minimap2":
        aligner_version = get_executable_version(path_to_aligner + "minimap2")
    else:
        print_error("Unrecognize aligner: " + path_to_aligner + aligner.lower())

    # check cutadapt
    if trim_reads:
        if len(path_to_cutadapt) != 0:
            path_to_cutadapt += "/"
        cutadapt_version = get_executable_version(path_to_cutadapt + "cutadapt")
        if parse_version(cutadapt_version) < parse_version("1.8"):
            print_error("cutadapt version %s found.\nmethylpy need at least cutadapt 1.9\nExit!\n"
                        % (cutadapt_version))

    # check picard
    if remove_clonal:
        if len(path_to_picard) != 0:
            path_to_cutadapt += "/"
        # check java
        try:
            exec_name = "java"
            out = subprocess.check_output(shlex.split(exec_name + " -version"),
                                          stderr=subprocess.PIPE)
        except:
            print_error("java not found.\n"
                        + "methylpy need java to run picard to remove PCR duplicates\n"
                        + "Exit!\n")
        # check picard
        if not os.path.isfile(path_to_picard + "/picard.jar"):
            print_error("picard is not found at\n\""
                        + path_to_picard + "\"\n"
                        + "Exit!\n")

    return (True)


def convert_allc_to_bigwig(input_allc_file,
                           output_file,
                           chrom_size_file,
                           mc_type="CGN",
                           bin_size=100,
                           path_to_wigToBigWig="",
                           path_to_samtools="",
                           min_bin_sites=0,
                           min_bin_cov=0,
                           max_site_cov=None,
                           min_site_cov=0,
                           add_chr_prefix=False
                           ):
    if not isinstance(mc_type, list):
        if isinstance(mc_type, str):
            mc_type = [mc_type]
        else:
            exit("mc_type must be a list of string(s)")

    if len(path_to_wigToBigWig):
        path_to_wigToBigWig += "/"

    mc_class = expand_nucleotide_code(mc_type)

    chrom_end = {}

    # chromosome size
    f = open(chrom_size_file, 'r')
    g = open(output_file + ".chrom_size", 'w')
    for line in f:
        fields = line.split("\t")
        if not fields[0].startswith("chr"):
            fields[0] = "chr" + fields[0]
        chrom_end[fields[0]] = int(fields[1])
        g.write(fields[0] + "\t" + fields[1] + "\n")
    g.close()

    # prepare wig file
    cur_chrom = ""
    bin_start, bin_end = 0, 0
    bin_mc, bin_h, bin_site = 0, 0, 0
    g = open(output_file + ".wig", 'w')
    with open_allc_file(input_allc_file) as f:
        for line in f:
            fields = line.split("\t")
            if fields[3] not in mc_class:
                continue
            pos = int(fields[1]) - 1
            if cur_chrom != fields[0] or pos >= bin_end:
                try:
                    if fields[0].startswith("chr"):
                        cur_chrom_end = chrom_end[fields[0]]
                    else:
                        cur_chrom_end = chrom_end["chr" + fields[0]]
                except KeyError:
                    # chrom not in chrom size file
                    continue

                if bin_h > 0 and bin_site >= min_bin_sites and bin_h >= min_bin_cov:
                    mc_level = str(float(bin_mc) / float(bin_h))
                    if add_chr_prefix and not cur_chrom.startswith("chr"):
                        g.write("\t".join(["chr" + cur_chrom,
                                           str(bin_start),
                                           str(bin_end),
                                           mc_level]) + "\n")
                    else:
                        g.write("\t".join([cur_chrom,
                                           str(bin_start),
                                           str(bin_end),
                                           mc_level]) + "\n")

                if pos >= cur_chrom_end:
                    print_warning("Skip site beyond chromosome boundary: " + line)
                    cur_chrom = fields[0]
                    bin_mc, bin_h, bin_site = 0, 0, 0
                    continue
                # reset
                cur_chrom = fields[0]
                bin_mc, bin_h, bin_site = 0, 0, 0
                bin_end = int(float(pos) / float(bin_size) + 1) * bin_size
                bin_start = bin_end - bin_size
                if bin_end > cur_chrom_end:
                    bin_end = cur_chrom_end
            # update mc, h and site
            h_site = int(fields[5])
            if h_site >= min_site_cov \
                    and (max_site_cov is None or h_site <= max_site_cov):
                bin_mc += int(fields[4])
                bin_h += h_site
                bin_site += 1
    if bin_h > 0 and bin_site >= min_bin_sites and bin_h >= min_bin_cov:
        mc_level = str(float(bin_mc) / float(bin_h))
        if add_chr_prefix and not cur_chrom.startswith("chr"):
            g.write("\t".join(["chr" + cur_chrom,
                               str(bin_start),
                               str(bin_end),
                               mc_level]) + "\n")
        else:
            g.write("\t".join([cur_chrom,
                               str(bin_start),
                               str(bin_end),
                               mc_level]) + "\n")
    g.close()

    # generate bigwig file
    subprocess.check_call(shlex.split(path_to_wigToBigWig + "wigToBigWig "
                                      + "%s.wig " % (output_file)
                                      + "%s.chrom_size " % (output_file)
                                      + output_file), stderr=subprocess.PIPE)
    subprocess.check_call(shlex.split("rm " + output_file + ".wig " + output_file + ".chrom_size"))


def filter_allc_files(allc_files,
                      output_files,
                      num_procs=1,
                      mc_type=None,
                      chroms=None,
                      compress_output=False,
                      min_cov=0,
                      max_cov=None,
                      max_mismatch=None,
                      max_mismatch_frac=None,
                      buffer_line_number=100000):
    # User input checks
    if not isinstance(allc_files, list):
        exit("allc files must be a list of string(s)")
    if not isinstance(output_files, list):
        exit("output files must be a list of string(s)")
    if len(allc_files) != len(output_files):
        exit("Number of allc files does not match number of output files")

    if num_procs > 1:
        pool = multiprocessing.Pool(min(num_procs, len(allc_files)))
        print_checkpoint("Filtering allc files using "
                         + str(min(num_procs, len(allc_files)))
                         + " node(s).")
        for allc_file, output_file in zip(allc_files, output_files):
            pool.apply_async(filter_allc_file_worker,
                             (),
                             {"allc_file": allc_file,
                              "output_file": output_file,
                              "mc_type": mc_type,
                              "chroms": chroms,
                              "compress_output": compress_output,
                              "min_cov": min_cov,
                              "max_cov": max_cov,
                              "max_mismatch": max_mismatch,
                              "max_mismatch_frac": max_mismatch_frac
                              })
        pool.close()
        pool.join()
    else:
        print_checkpoint("Filtering allc files using single node.")
        for allc_file, output_file in zip(allc_files, output_files):
            filter_allc_file_worker(allc_file=allc_file,
                                    output_file=output_file,
                                    mc_type=mc_type,
                                    chroms=chroms,
                                    compress_output=compress_output,
                                    min_cov=min_cov,
                                    max_cov=max_cov,
                                    max_mismatch=max_mismatch,
                                    max_mismatch_frac=max_mismatch_frac)


def filter_allc_file_worker(allc_file,
                            output_file,
                            mc_type=None,
                            chroms=None,
                            compress_output=False,
                            min_cov=0,
                            max_cov=None,
                            max_mismatch=None,
                            max_mismatch_frac=None,
                            buffer_line_number=100000):
    if mc_type is not None:
        mc_class = expand_nucleotide_code(mc_type)
    # input & output
    f = open_allc_file(allc_file)
    if compress_output:
        if output_file[-3:] != ".gz":
            output_file += ".gz"
        output_fhandler = gzip.open(output_file, 'wt')
    else:
        output_fhandler = open(output_file, 'w')
    # begin
    line_counts = 0
    out = ""
    for line in f:
        fields = line.split("\t")
        if (chroms is None or fields[0] in chroms) \
                and (mc_type is None or fields[3] in mc_class) \
                and int(fields[5]) >= min_cov \
                and (max_cov is None or int(fields[5]) <= max_cov):
            pass
        else:
            continue

        if max_mismatch is not None or max_mismatch_frac is not None:
            try:
                matches = map(int, fields[7].split(","))
                mismatches = map(int, fields[8].split(","))
            except:
                print_error("allc file " + allc_file + "does not contain SNP information used "
                            + "for applying mismatch-based filtering!\n")
            pass_snp_filter = True
            if max_mismatch is not None:
                try:
                    for index, cutoff in enumerate(max_mismatch):
                        if mismatches[index] > cutoff:
                            pass_snp_filter = False
                            break
                except:
                    pass
            if max_mismatch_frac is not None:
                try:
                    for index, cutoff in enumerate(max_mismatch_frac):
                        cov = mismatches[index] + matches[index]
                        if cov > 0 and float(mismatches[index]) / float(cov) > cutoff:
                            pass_snp_filter = False
                            break
                except:
                    pass
            if not pass_snp_filter:
                continue

        line_counts += 1
        out += line
        # print out once reach buffer limit
        if line_counts > buffer_line_number:
            output_fhandler.write(out)
            line_counts = 0
            out = ""
    # clear buffer
    if line_counts > 0:
        output_fhandler.write(out)
        out = ""
    f.close()
    output_fhandler.close()


def merge_allc_files(allc_files,
                     output_file,
                     num_procs=1,
                     mini_batch=100,
                     compress_output=True,
                     skip_snp_info=True,
                     buffer_line_number=100000, index=True):
    # User input checks
    if not isinstance(allc_files, list):
        exit("allc_files must be a list of string(s)")
    # add .gz suffix
    if compress_output and output_file[-3:] != ".gz":
        output_file += ".gz"

    # check index
    # ME: keep this for original index
    index_allc_file_batch(allc_files,
                          num_procs=num_procs)
    print_checkpoint("Start merging")
    if not (num_procs > 1):
        merge_allc_files_minibatch(allc_files,
                                   output_file,
                                   query_chroms=None,
                                   mini_batch=mini_batch,
                                   compress_output=compress_output,
                                   skip_snp_info=skip_snp_info)
        if index:
            index_allc_file(output_file)
        return 0

    # parallel merging
    print_checkpoint("Getting chromosome names")
    chroms = set([])
    for allc_file in allc_files:
        c_p = read_allc_index(allc_file)
        for chrom in c_p.keys():
            chroms.add(chrom)
    try:
        pool = multiprocessing.Pool(min(num_procs,
                                        len(chroms)))  # ,
        # int(float(mini_batch)/float(len(allc_files)))))
        print_checkpoint("Merging allc files")
        for chrom in chroms:
            pool.apply_async(merge_allc_files_minibatch,
                             (),
                             {"allc_files": allc_files,
                              "output_file": output_file + "_" + str(chrom) + ".tsv",
                              "query_chroms": chrom,
                              "mini_batch": mini_batch,
                              "compress_output": False,
                              "skip_snp_info": skip_snp_info,
                              }
                             )
        pool.close()
        pool.join()
        # output
        print_checkpoint("Merging outputs")
        if compress_output:
            g = gzip.open(output_file, 'wt')
        else:
            g = open(output_file, 'w')
        out = ""
        line_counts = 0
        for chrom in chroms:
            f = open(output_file + "_" + chrom + ".tsv", 'r')
            for line in f:
                out += line
                line_counts += 1
                if line_counts > buffer_line_number:
                    g.write(out)
                    out = ""
                    line_counts = 0
            f.close()
        if line_counts > 0:
            g.write(out)
            out = ""
        g.close()
    except:
        print("Failed to merge using multiple processors. " +
              "Do minibatch merging using single processor.")
        merge_allc_files_minibatch(allc_files,
                                   output_file,
                                   mini_batch=mini_batch,
                                   compress_output=compress_output,
                                   skip_snp_info=skip_snp_info)
    # remove temporary files
    for chrom in set(chroms):
        tmp_file = glob.glob(output_file + "_" + str(chrom) + ".tsv")
        if tmp_file:
            tmp_file = tmp_file[0]
            subprocess.check_call(["rm", tmp_file])
            remove_allc_index(tmp_file)
    # index output allc file
    if index:
        index_allc_file(output_file)
    return 0


def merge_allc_files_minibatch(allc_files,
                               output_file,
                               query_chroms=None,
                               mini_batch=100,
                               compress_output=False,
                               skip_snp_info=True):
    # User input checks
    if not isinstance(allc_files, list):
        exit("allc_files must be a list of string(s)")
    # merge all files at once
    try:
        merge_allc_files_worker(allc_files=allc_files,
                                output_file=output_file,
                                query_chroms=query_chroms,
                                compress_output=compress_output,
                                skip_snp_info=skip_snp_info)
        return 0
    except:
        print("Failed to merge all allc files at once. Do minibatch merging")

    # init
    remaining_allc_files = list(allc_files[mini_batch:])
    output_tmp_file = output_file + ".tmp"
    merge_allc_files_worker(allc_files=allc_files[:mini_batch],
                            output_file=output_file,
                            query_chroms=query_chroms,
                            compress_output=compress_output,
                            skip_snp_info=skip_snp_info)
    # batch merge
    while len(remaining_allc_files) > 0:
        processing_allc_files = [output_file]
        while len(remaining_allc_files) > 0 \
                and len(processing_allc_files) < mini_batch:
            processing_allc_files.append(remaining_allc_files.pop())
        merge_allc_files_worker(allc_files=processing_allc_files,
                                output_file=output_tmp_file,
                                query_chroms=query_chroms,
                                compress_output=compress_output,
                                skip_snp_info=skip_snp_info)
        subprocess.check_call(["mv", output_tmp_file, output_file])
        index_allc_file(output_file)
    return 0


def merge_allc_files_worker(allc_files,
                            output_file,
                            query_chroms=None,
                            compress_output=False,
                            skip_snp_info=True,
                            buffer_line_number=100000):
    # User input checks
    if not isinstance(allc_files, list):
        exit("allc_files must be a list of string(s)")

    # scan allc file to set up a table for fast look-up of lines belong
    # to different chromosomes
    fhandles = []
    chrom_pointer = []
    chroms = set([])
    try:
        for index, allc_file in enumerate(allc_files):
            fhandles.append(open_allc_file(allc_file))
            chrom_pointer.append(read_allc_index(allc_file))
            for chrom in chrom_pointer[index].keys():
                chroms.add(chrom)
    except:
        for f in fhandles:
            f.close()
        raise
        # exit() # exit due to failure of openning all allc files at once
    if query_chroms is not None:
        if isinstance(query_chroms, list):
            chroms = query_chroms
        else:
            chroms = [query_chroms]
    chroms = list(map(str, chroms))
    # output
    if compress_output:
        g = gzip.open(output_file, 'wt')
    else:
        g = open(output_file, 'w')

    # merge allc files
    out = ""
    for chrom in chroms:
        cur_pos = np.array([np.nan for index in range(len(allc_files))])
        cur_fields = []
        num_remaining_allc = 0
        # init
        for index, allc_file in enumerate(allc_files):
            fhandles[index].seek(chrom_pointer[index].get(chrom, 0))
            line = fhandles[index].readline()
            fields = line.split("\t")
            cur_fields.append(None)
            if fields[0] == chrom:
                cur_pos[index] = int(fields[1])
                cur_fields[index] = fields
                num_remaining_allc += 1

        # check consistency of SNP information
        context_len = None
        if not skip_snp_info:
            for index, allc_file in enumerate(allc_files):
                # skip allc with no data in this chromosome
                if cur_fields[index] is None:
                    continue
                # SNP information is missing
                if len(cur_fields[index]) < 9:
                    print_warning("SNP information not found in " + allc_file + "!\n"
                                  + "Skip SNP information\n")
                    skip_snp_info = True
                    break
                # init contex_len
                if context_len is None:
                    context_len = len(cur_fields[index][7].split(","))
                # check whether contex length are the same
                if context_len != len(cur_fields[index][7].split(",")) or \
                        context_len != len(cur_fields[index][8].split(",")):
                    print_error("Inconsistent sequence context length: "
                                + allc_file + "\n")
        # merge
        line_counts = 0
        while num_remaining_allc > 0:
            mc, h = 0, 0
            if not skip_snp_info:
                matches = [0 for index in range(context_len)]
                mismatches = list(matches)
            c_info = None
            for index in np.where(cur_pos == np.nanmin(cur_pos))[0]:
                mc += int(cur_fields[index][4])
                h += int(cur_fields[index][5])
                if not skip_snp_info:
                    for ind, match, mismatch in zip(range(context_len),
                                                    cur_fields[index][7].split(","),
                                                    cur_fields[index][8].split(",")):
                        matches[ind] += int(match)
                        mismatches[ind] += int(mismatch)
                if c_info is None:
                    c_info = "\t".join(cur_fields[index][:4])
                # update
                line = fhandles[index].readline()
                fields = line.split("\t")
                if fields[0] == chrom:
                    cur_pos[index] = int(fields[1])
                    cur_fields[index] = fields
                else:
                    cur_pos[index] = np.nan
                    num_remaining_allc -= 1
            # output
            if not skip_snp_info:
                out += c_info + "\t" + str(mc) + "\t" + str(h) + "\t1" + "\t" \
                       + ",".join(map(str, matches)) + "\t" + ",".join(map(str, mismatches)) + "\n"
            else:
                out += c_info + "\t" + str(mc) + "\t" + str(h) + "\t1\n"
            line_counts += 1
            if line_counts > buffer_line_number:
                g.write(out)
                line_counts = 0
                out = ""
    if line_counts > 0:
        g.write(out)
        out = ""
    g.close()
    for index in range(len(allc_files)):
        fhandles[index].close()
    return 0


def get_index_file_name(allc_file):
    return allc_file + ".idx"


def index_allc_file_batch(allc_files, num_procs=1, reindex=False):
    if num_procs == 1:
        for allc_file in allc_files:
            index_allc_file(allc_file, reindex)
    else:
        pool = multiprocessing.Pool(min(num_procs, len(allc_files), 100))
        for allc_file in allc_files:
            pool.apply_async(index_allc_file, (allc_file, reindex))
        pool.close()
        pool.join()
    return 0


def index_allc_file(allc_file, reindex=False):
    index_file = get_index_file_name(allc_file)
    # do not reindex if the index file is available and is complete
    if (not reindex) and os.path.exists(index_file):
        return 0
        # check index file completeness
        eof_count = 0
        line = False
        with open(index_file, 'r') as f:
            for line in f:
                if line == '#eof\n':
                    eof_count += 1
        # need reindex
        if eof_count > 1 or line != '#eof\n':
            pass
        else:
            return 0
    g = open(index_file, 'w')
    if 'gz' in allc_file:
        subprocess.run(f'pigz -d -p 8 {allc_file}', shell=True)
        f = open(allc_file[:-3])
    else:
        f = open(allc_file)

    cur_chrom = ""
    # check header
    line = f.readline()
    try:
        fields = line.split("\t")
        int(fields[1])
        int(fields[4])
        int(fields[5])
        # no header, continue to start from the beginning of allc file
        f.seek(0)
        cur_pointer = 0
    except:
        # find header, skip it
        cur_pointer = f.tell()
    # find chrom pointer
    while True:
        line = f.readline()
        if not line:
            break
        fields = line.split("\t")
        if fields[0] != cur_chrom:
            g.write(fields[0] + "\t" + str(cur_pointer) + "\n")
            cur_chrom = fields[0]
        cur_pointer = f.tell()
    g.write("#eof\n")
    f.close()
    g.close()
    if 'gz' in allc_file:
        subprocess.run(f'pigz -p 8 {allc_file[:-3]}', shell=True)
    return 0


def read_allc_index(allc_file):
    index_file = get_index_file_name(allc_file)
    index_allc_file(allc_file, reindex=False)
    f = open(index_file, 'r')
    chrom_pointer = {}
    for line in f:
        if line[0] != '#':
            fields = line.rstrip().split("\t")
            chrom_pointer[fields[0]] = int(fields[1])
    f.close()
    return chrom_pointer


def remove_allc_index(allc_file):
    index_file = get_index_file_name(allc_file)
    if glob.glob(index_file):
        subprocess.check_call(["rm", index_file])


def expand_nucleotide_code(mc_type):
    iub_dict = {"N": ["A", "C", "G", "T", "N"],
                "H": ["A", "C", "T", "H"],
                "D": ["A", "G", "T", "D"],
                "B": ["C", "G", "T", "B"],
                "A": ["A", "C", "G", "A"],
                "R": ["A", "G", "R"],
                "Y": ["C", "T", "Y"],
                "K": ["G", "T", "K"],
                "M": ["A", "C", "M"],
                "S": ["G", "C", "S"],
                "W": ["A", "T", "W"],
                "C": ["C"],
                "G": ["G"],
                "T": ["T"],
                "A": ["A"]}

    mc_class = list(mc_type)  # copy
    if "C" in mc_type:
        mc_class.extend(["CGN", "CHG", "CHH", "CNN"])
    elif "CG" in mc_type:
        mc_class.extend(["CGN"])

    mc_class_final = []
    for motif in mc_class:
        mc_class_final.extend(["".join(i) for i in
                               itertools.product(*[iub_dict[nuc] for nuc in motif])])
    return (set(mc_class_final))


def split_fastq_file(num_chunks,
                     input_files,
                     output_prefix,
                     buffer_line_number=100000):
    """
    This function mimics the unix split utility.
    """
    if not isinstance(input_files, list):
        if isinstance(input_files, str):
            input_files = [input_files]
        else:
            sys.exit("input_files must be a list of strings")
    file_handles = {}
    for index in range(0, num_chunks):
        file_handles[index] = open(output_prefix + str(index), 'w')
    cycle = itertools.cycle(list(range(0, num_chunks)))
    total_reads = 0
    for inputf in input_files:
        if inputf[-3:] == ".gz":
            f = gzip.open(inputf, 'rt')
        else:
            f = open(inputf, 'r')

        while True:
            current_file = next(cycle)
            # processing read id
            # remove any string after the first space character
            line = f.readline()
            if not line:
                break
            line = line.rstrip()
            file_handles[current_file].write(line.split(" ")[0] + "\n")
            total_reads += 1
            # seq
            line = f.readline()
            file_handles[current_file].write(line)
            # seq
            line = f.readline()
            file_handles[current_file].write("+\n")
            # qual
            line = f.readline()
            file_handles[current_file].write(line)
        f.close()

    for index in range(0, num_chunks):
        file_handles[index].close()

    return (total_reads)


def split_fastq_file_pbat(num_chunks, input_files, output_prefix):
    """
    This function mimics the unix split utility.
    """

    def reverse_complement(dna):
        complement = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N"}
        return ("".join([complement[base] for base in reversed(dna)]))

    if not isinstance(input_files, list):
        if isinstance(input_files, str):
            input_files = [input_files]
        else:
            sys.exit("input_files must be a list of strings")
    file_handles = {}
    for index in range(0, num_chunks):
        file_handles[index] = open(output_prefix + str(index), 'w')
    cycle = itertools.cycle(list(range(0, num_chunks)))
    total_reads = 0
    for inputf in input_files:
        if inputf[-3:] == ".gz":
            f = gzip.open(inputf, 'rt')
        else:
            f = open(inputf, 'r')

        while True:
            current_file = next(cycle)
            # processing read id
            # remove any string after the first space character
            line = f.readline()
            if not line:
                break
            # read id
            line = line.rstrip()
            file_handles[current_file].write(line.split(" ")[0] + "\n")
            total_reads += 1
            # seq
            line = f.readline()
            line = line.rstrip()
            file_handles[current_file].write(reverse_complement(line) + "\n")
            #
            line = f.readline()
            file_handles[current_file].write(line)
            # qual
            line = f.readline()
            line = line.rstrip()
            file_handles[current_file].write(line[::-1] + "\n")

        f.close()

    for index in range(0, num_chunks):
        file_handles[index].close()

    return (total_reads)


def split_mpileup_file(num_chunks, inputf, output_prefix):
    """
    This function mimics the unix split utility.
    preserve_order guarantees that the chunk files are split in the same order as the input file
    """
    total_lines = int(subprocess.check_output(["wc", "-l", inputf]).rstrip().split()[0])
    chunk_size = math.ceil(float(total_lines) / num_chunks)
    if chunk_size == 0:
        sys.exit("No lines in " + inputf)
    chunk_num = 0
    try:
        f = gzip.open(inputf, 'rt')
        f.readline()
    except:
        f = open(inputf, 'r')
    finally:
        f.seek(0)
    g = open(output_prefix + str(chunk_num), 'w')
    count = 0
    prev_lines = collections.deque(maxlen=2)
    line = f.readline()
    while line:
        if count >= chunk_size:
            g.close()
            chunk_num += 1
            # This code looks a bit weird, but it's to handle a nasty edge case.
            # There's a problem if there is a C in one of the last two positions of a chunk
            # This information is needed at the end of the current file
            # (to figure out the context of previous cytosines)
            # and the beginning of the next (to create new positions in the allc file). Consequently I write
            # the last two positions of a file again to the beginning of the next file.
            g = open(output_prefix + str(chunk_num), 'w')
            g.write("".join(prev_lines))
            count = 0
        g.write(line)
        count += 1
        prev_lines.append(line)
        line = f.readline()
    g.close()
    f.close()


def parallel_count_lines(filename,
                         sample_chrom_pointer, chrom,
                         min_cov, mc_class):
    """
    Parallel helper to count lines in files. Used in split_files_by_position.
    """
    f = open_allc_file(filename)
    f.seek(sample_chrom_pointer[chrom])
    num_lines = 0

    for line in f:
        fields = line.split("\t")
        try:
            int(fields[1])
            int(fields[5])
        except:
            print("WARNING: One of the lines in " + filename + " is not formatted correctly:\n" + line + "Skipping it.")
            continue
        if fields[0] != chrom: break
        if fields[3] in mc_class and int(fields[5]) >= min_cov:
            num_lines += 1

    return ((num_lines, filename))


def split_files_by_position(files, samples,
                            chunks, mc_class,
                            chrom_pointer, chrom,
                            num_procs=1, min_cov=0, pool=False, max_dist=0,
                            weight_by_dist=False):
    """
    This function will split a group of files into chunks number of subfiles with the guarantee
    that two subfiles with the same suffix will contain the same range of positions. These files are
    assumed to be from the same chromosome. ASSUMES THAT ALLC FILES ARE SORTED.
    files - a list of file names
    chunks - the number of subfiles you wish to create
    mc_class - a list of 3 character strings indicating the nucleotide contexts you wish to consider.
    nrange - only consider positions between these coordinates
    max_dist - mc and h values from positions within max_dist of one another will be combined
        this helps leverage the correlation of methylation across a distance to make up for low
        coverage experiments.
    weight_by_dist - weight nearby position influence on mc & h values by their distance (otherwise sum them with equal weight)
    """
    # Note: only the first file will be truly evenly split, the other files will be split such that each
    # file contains the same range (but not necessarily the same number) of positions (e.g., from chr1:1000-2000)
    # num_lines = subprocess.check_output("wc -l "+files[0],shell=True).split(" ")[0]
    if not isinstance(files, list):
        if isinstance(files, str):
            files = [files]
        else:
            sys.exit("files must be a list")
    # use multiprocessing to count lines in each file and return (num_lines, filename) tuple
    if num_procs > 1:
        line_results = []
        # If a pool has not been passed to this function
        if pool == False:
            pool_new = multiprocessing.Pool(num_procs)
            for input_file, sample in zip(files, samples):
                line_results.append(pool_new.apply_async(parallel_count_lines,
                                                         (input_file, chrom_pointer[sample],
                                                          chrom, min_cov, mc_class)))
            pool_new.close()
            pool_new.join()
        # If a pool has been passed to this function make sure it doesn't get closed by this funciton
        else:
            for input_file, sample in zip(files, samples):
                line_results.append(pool.apply_async(parallel_count_lines,
                                                     (input_file, chrom_pointer[sample],
                                                      chrom, min_cov, mc_class)))
        lines = [r.get() for r in line_results]  # get() call blocks until all are finished so no need for wait()
    else:
        lines = []
        for input_file, sample in zip(files, samples):
            lines.append(parallel_count_lines(input_file, chrom_pointer[sample],
                                              chrom, min_cov, mc_class))

    # I have to guarantee that the smallest file is the one the chunk splitting is based on
    # if I don't do this, the smallest file might not have enough lines to be split into enough
    # chunks and then bad things happen.
    min_lines = 100000000000000
    min_file = None
    for index in range(len(lines)):
        if lines[index][0] > 0 and min_lines > lines[index][0]:
            min_lines, min_file = lines[index]
    chunk_size = math.ceil(float(min_lines) / chunks)
    if chunk_size == 0 or min_file is None:
        return 0
        # sys.exit("No lines match your range and/or mc_class criteria")
    min_sample = 0
    for input_file, sample in zip(files, samples):
        if input_file == min_file:
            min_sample = sample
            break
    chunk_num = 0
    count = 0
    # This list stores the position cutoffs for each chunk
    cutoffs = {}
    with open_allc_file(min_file) as f:
        f.seek(chrom_pointer[min_sample][chrom])
        for line in f:
            line = line.rstrip("\n")
            fields = line.split("\t")
            try:
                int(fields[1])
                int(fields[5])
            except:
                print(
                    "WARNING: One of the lines in " + min_file + " is not formatted correctly:\n" + line + "\nSkipping it.")
                continue
            if fields[0] != chrom:
                break
            elif int(fields[5]) >= min_cov and fields[3] in mc_class:
                count += 1
                if count > chunk_size:
                    cutoffs[chunk_num] = int(fields[1])
                    chunk_num += 1
                    count = 0
    # Want to make sure that for the last chunk all remaining lines get output
    # There's an edge case where the initial sample has positions which aren't as far
    # along the chromosome as other samples
    cutoffs[chunk_num] = 50000000000
    # enable multiprocessing
    if num_procs > 1:
        # If a pool has not been passed to this function
        if pool == False:
            pool_new = multiprocessing.Pool(num_procs)
            for input_file, sample in zip(files, samples):
                pool_new.apply_async(parallel_split_files_by_position, (input_file, cutoffs,
                                                                        chrom_pointer[sample][chrom],
                                                                        chrom,
                                                                        mc_class),
                                     {"min_cov": min_cov, "max_dist": max_dist, "weight_by_dist": weight_by_dist})
            pool_new.close()
            pool_new.join()
        # If a pool has been passed to this function make sure it doesn't get closed by this funciton
        else:
            results = []
            for input_file, sample in zip(files, samples):
                results.append(pool.apply_async(parallel_split_files_by_position,
                                                (input_file, cutoffs,
                                                 chrom_pointer[sample][chrom],
                                                 chrom,
                                                 mc_class),
                                                {"min_cov": min_cov,
                                                 "max_dist": max_dist,
                                                 "weight_by_dist": weight_by_dist}))
            for result in results:
                result.wait()
    else:
        for input_file, sample in zip(files, samples):
            parallel_split_files_by_position(input_file, cutoffs,
                                             chrom_pointer[sample][chrom],
                                             chrom,
                                             mc_class,
                                             min_cov=min_cov, max_dist=max_dist,
                                             weight_by_dist=weight_by_dist)


def parallel_split_files_by_position(filen, cutoffs,
                                     sample_chrom_pointer, chrom,
                                     mc_class,
                                     min_cov=0, max_dist=0,
                                     weight_by_dist=False):
    chunk_num = 0
    f = open_allc_file(filen)
    f.seek(sample_chrom_pointer)
    # Just in case there's a header line in the file
    # I assume that if the position field can't be cast as an int
    # it must be a header
    fields_deque = collections.deque()
    added_values_deque = collections.deque()
    g = open(filen + "_" + chrom + "_" + str(chunk_num) + ".tsv", 'w')
    for line in f:
        line = line.rstrip("\n")
        fields = line.split("\t")
        try:
            int(fields[1])
            int(fields[5])
        except:
            print(
                "WARNING: One of the lines in " + files[0] + " is not formatted correctly:\n" + line + "\nSkipping it.")
            continue
        if fields[0] != chrom: break
        if int(fields[1]) >= cutoffs[chunk_num]:
            g.close()
            chunk_num += 1
            g = open(filen + "_" + chrom + "_" + str(chunk_num) + ".tsv", 'w')
        if fields[3] in mc_class and int(fields[5]) >= min_cov:
            fields_deque.append(fields)
            mc = int(fields[4])
            h = int(fields[5])
            added_values_deque.append([mc, h])
            while len(fields_deque) > 0 and (int(fields_deque[-1][1]) - int(fields_deque[0][1])) >= max_dist:
                fields = fields_deque.popleft()
                added_values = added_values_deque.popleft()
                if added_values[0] != int(fields[4]):
                    g.write(
                        "\t".join(fields[0:4]) + "\t" + str(added_values[0]) + "\t" + str(added_values[1]) + "\t1\n")
                else:
                    g.write("\t".join(fields[0:4]) + "\t" + str(added_values[0]) + "\t" + str(added_values[1]) + "\t" +
                            fields[6] + "\n")
            if len(fields_deque) > 1:
                for index in range(0, len(added_values_deque) - 1):
                    if weight_by_dist:
                        weighting_factor = float(max_dist - abs(int(fields_deque[index][1]) -
                                                                int(fields_deque[-1][1]))) / max_dist
                    else:
                        weighting_factor = 1.0
                    added_values_deque[index][0] += int(round(mc * weighting_factor))
                    added_values_deque[index][1] += int(round(h * weighting_factor))
                    added_values_deque[-1][0] += int(round(int(fields_deque[index][4]) * weighting_factor))
                    added_values_deque[-1][1] += int(round(int(fields_deque[index][5]) * weighting_factor))

    if len(added_values_deque) > 0:
        fields = fields_deque.popleft()
        added_values = added_values_deque.popleft()
        if added_values[0] != int(fields[4]):
            g.write("\t".join(fields[0:4]) + "\t" + str(added_values[0]) + "\t" + str(added_values[1]) + "\t1\n")
        else:
            g.write("\t".join(fields[0:4]) + "\t" + str(added_values[0]) + "\t" + str(added_values[1]) + "\t" + fields[
                6] + "\n")
    g.close()
    f.close()


def open_allc_file(allc_file):
    if allc_file[-3:] == ".gz":
        f = gzip.open(allc_file, 'rt')
    else:
        f = open(allc_file, 'r')
    return f


def print_checkpoint(message):
    """
    Print message and current time
    """
    print(message)
    tabs = message.count("\t")
    print(("\t" * tabs) + time.asctime(time.localtime(time.time())) + "\n")
    sys.stdout.flush()


def print_error(error_message=""):
    sys.stderr.write("Error:\n" + error_message)
    sys.exit(1)


def print_warning(error_message=""):
    sys.stderr.write("Warning:\n" + error_message)
    # sys.exit(1)

