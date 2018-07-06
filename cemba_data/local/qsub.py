from subprocess import run, PIPE
import os
import json
import configparser
import datetime
import re
import time
import pandas as pd

qsub_config = configparser.ConfigParser()
qsub_config.read(os.path.dirname(__file__) + '/config_local.ini')


def default_command_dict(name, error_path, output_path):
    command_dict = {'command': None,
                    '-N': name,
                    '-V': '',
                    '-pe smp': qsub_config['QSUB_DEFAULT']['CPU'],
                    '-l h_rt': qsub_config['QSUB_DEFAULT']['H_RT'],
                    '-l s_rt': qsub_config['QSUB_DEFAULT']['S_RT'],
                    '-wd': qsub_config['QSUB_DEFAULT']['WD'],
                    '-e': error_path,
                    '-o': output_path}
    return command_dict


def check_qstat(id_set=None):
    space_pattern = re.compile(' +')
    qstat_result = run(['qstat', '-u', qsub_config['USER']['USER_NAME']],
                       stdout=PIPE, encoding='utf8')
    qstat_result_lines = qstat_result.stdout.split('\n')[:-1]
    qstat_data = [space_pattern.split(line) for line in qstat_result_lines]
    header = qstat_data[0][:-1]
    qstat_data = qstat_data[2:]
    qstat_df = pd.DataFrame(qstat_data, columns=header)
    qstat_df.set_index('job-ID', inplace=True)
    if id_set is not None:
        qstat_df = qstat_df.reindex(id_set).dropna(how='all')
    return qstat_df


class Qsubmitter:
    def __init__(self, command_file_path, project_name, auto_submit=False):
        self.command_file_path = command_file_path
        self.project_name = project_name
        self.project_dir = qsub_config['QSUB_DEFAULT']['JOB_DIR'] + '/' + project_name
        if not os.path.exists(self.project_dir):
            os.mkdir(self.project_dir)

        self.commands = self.parse_command_file()
        self.running_commands = []
        self.running_cpu = 0
        self.submitted_qsub_id = set()
        self.submission_fail_commands = []
        self.finished_commands = []  # modify this with check_command_finish_status
        self.qsub_failed_commands = []  # modify this with check_command_finish_status
        self.cmd_failed_commands = []  # modify this with check_command_finish_status

        if auto_submit:
            self.submit()
        return

    def parse_command_file(self):
        with open(self.command_file_path) as command:
            command_dict_list = json.load(command)
            obj_list = []
            n = 0
            for command_dict in command_dict_list:
                obj_list.append(Command(command_dict=command_dict,
                                        unique_id=f'{self.project_name}_{n}',
                                        project_dir=self.project_dir))
                n += 1
        return obj_list

    def submit(self,
               total_cpu=int(qsub_config['RUNNING_DEFAULT']['TOTAL_CPU']),
               submit_gap=int(qsub_config['RUNNING_DEFAULT']['SUBMISSION_GAP']),
               qstat_gap=int(qsub_config['RUNNING_DEFAULT']['QSTST_GAP']),
               resubmit=None):
        # job submission process:
        for command_obj in self.commands:
            self.submitted_qsub_id.add(command_obj.qsub_id)
            # judge if command has been submitted
            if command_obj.submitted:
                if resubmit is None:
                    print('Skip command:', command_obj.unique_id)
                    self.check_command_finish_status(command_obj)
                    continue  # not resubmit command
                elif resubmit == 'fail':
                    # only resubmit failed command
                    if not command_obj.qsub_failed and not command_obj.cmd_failed:
                        # both a success, the job is success
                        print('Skip command:', command_obj.unique_id)
                        self.check_command_finish_status(command_obj)
                        continue
                    else:
                        print('Resubmit failed command:', command_obj.unique_id)
                elif resubmit == 'all':
                    # resubmit all command
                    pass
                else:
                    raise ValueError('resubmit only allow None, fail or all. Got', resubmit)

            command_cpu = int(command_obj.qsub_parameter['-pe smp'])
            if self.running_cpu + command_cpu > total_cpu:
                while True:
                    time.sleep(qstat_gap)
                    self.check_running_cpu()
                    if self.running_cpu <= total_cpu:
                        break
            print('Submit job:', command_obj.unique_id)
            command_obj.submit()
            # gather submitted id and obj
            if command_obj.submission_fail:
                self.submission_fail_commands.append(command_obj)
            else:
                self.running_commands.append(command_obj)
            self.running_cpu += command_cpu
            time.sleep(submit_gap)

        # final job check:
        while True:
            self.check_running_cpu()
            if self.running_cpu == 0:
                break  # all job finished

        self.get_reports()
        return

    def check_running_cpu(self):
        print('check running job')
        cur_qstat_df = check_qstat()
        cur_running_qsub_id = cur_qstat_df.index

        # check every running obj
        cur_running_cpu = 0
        cur_running_command = []
        for command_obj in self.running_commands:
            if command_obj.qsub_id not in cur_running_qsub_id:
                # command have finished
                print(command_obj.unique_id, 'qacct')
                if command_obj.query_qacct() != 0:
                    raise ValueError('Command not finished but disappeared in qstat')
                self.check_command_finish_status(command_obj)
            else:
                cur_running_command.append(command_obj)
                cur_running_cpu += int(command_obj.qsub_parameter['-pe smp'])

        self.running_commands = cur_running_command
        # update running cpu
        self.running_cpu = cur_running_cpu
        return

    def check_command_finish_status(self, command_obj):
        self.finished_commands.append(command_obj)
        if command_obj.qsub_failed:
            self.qsub_failed_commands.append(command_obj)
        if command_obj.cmd_failed:
            self.cmd_failed_commands.append(command_obj)
        return

    def get_reports(self):
        cur_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        with open(self.project_dir + f'/submit_summary.{cur_time}.txt', 'w') as summary:
            summary.write(f'Total Command: {len(self.commands)}\n')
            summary.write(f'Submission Failed Command: {len(self.submission_fail_commands)}\n')

            summary.write(f'Qsub Failed Command: {len(self.qsub_failed_commands)}\n')
            if len(self.qsub_failed_commands) > 0:
                with open(self.project_dir + '/qsub_failed_commands.txt', 'w') as f:
                    f.write('\n'.join(self.qsub_failed_commands))
                summary.write(f'See qsub failed command id in {self.project_dir}/qsub_failed_commands.txt\n')

            summary.write(f'Command Failed Command: {len(self.cmd_failed_commands)}\n')
            if len(self.cmd_failed_commands) > 0:
                with open(self.project_dir + '/cmd_failed_commands.txt', 'w') as f:
                    f.write('\n'.join(self.cmd_failed_commands))
                summary.write(f'See qsub failed command id in {self.project_dir}/cmd_failed_commands.txt\n')
        return


class Command:
    def __init__(self, command_dict, unique_id, project_dir,
                 error_path=None, output_path=None):
        self.project_dir = project_dir
        self.unique_id = unique_id

        # command status
        self.submitted = False
        self.qsub_id = None
        self.submission_fail = False
        self.finish = False  # if submitted is True and not in qstat
        self.qsub_failed = None  # check from qacct_status['failed'], fail due to qsub
        self.cmd_failed = None  # check from qacct_status['exit_status'], fail due to cmd
        self.qacct_status = None  # dict of qacct results
        self.qacct_status_path = f'{self.project_dir}/{unique_id}.qacct.json'
        self.script_path = f'{self.project_dir}/{unique_id}.sh'
        if error_path is None:
            self.error_path = f'{self.project_dir}/{unique_id}.error.log'
        if output_path is None:
            self.output_path = f'{self.project_dir}/{unique_id}.output.log'

        # prepare command dict
        self.command_dict = default_command_dict(name=self.unique_id,
                                                 error_path=self.error_path,
                                                 output_path=self.output_path)
        self.command_dict.update(**command_dict)
        for k, v in self.command_dict.items():
            if v is None:
                raise ValueError(f'{k} is None in command dict')

        # separate command and qsub parameter
        self.command = self.command_dict.pop('command')
        self.qsub_parameter = self.command_dict
        self.command_dict = None

        # make command sh file
        self.make_script_file()

        # modify command status if it has been submitted and finished
        if os.path.exists(self.qacct_status_path):
            with open(self.qacct_status_path) as f:
                self.qacct_status = json.load(f)
            self.submitted = True
            self.qsub_id = self.qacct_status['jobnumber']
            self.finish = True
            self.judge_qacct_status()
        return

    def make_script_file(self):
        with open(self.script_path, 'w') as sh:
            sh.write("#!/bin/bash\n")
            for k, v in self.qsub_parameter.items():
                if k[:2] == '-l':
                    sh.write(f'#$ {k}={v}\n')
                else:
                    sh.write(f'#$ {k} {v}\n')
            sh.write(self.command)
        return

    def submit(self):
        job_id_pattern = re.compile(r'(?<=Your job )\d+')
        return_obj = run(['qsub', self.script_path], stdout=PIPE, encoding='utf8')
        try:
            self.qsub_id = job_id_pattern.search(return_obj.stdout).group()
        except AttributeError:
            self.submission_fail = True
        self.submitted = True

        # remove previous qacct status
        self.finish = False
        self.qsub_failed = None
        self.cmd_failed = None
        self.qacct_status = None
        return

    def query_qacct(self):
        if self.qacct_status is not None:
            return 0
        time.sleep(10)
        qstat_result = run(['qstat', '-j', self.qsub_id], stdout=PIPE, stderr=PIPE, encoding='utf8')
        if 'Following jobs do not exist' in qstat_result.stderr and self.submitted:
            self.finish = True
        else:
            return 1  # not finish
        qacct_result = run(['qacct', '-j', self.qsub_id, '-o', qsub_config['USER']['USER_NAME']],
                           stdout=PIPE, encoding='utf8')
        status_dict = {}
        qacct_result_lines = qacct_result.stdout.split('\n')[1:-1]
        for line in qacct_result_lines:
            k = line[:13].strip()  # how to separate lines without \t???
            v = line[13:].strip()
            status_dict[k] = v
        self.qacct_status = status_dict
        self.judge_qacct_status()
        with open(self.qacct_status_path, 'w') as f:
            json.dump(self.qacct_status, f)
        return 0

    def judge_qacct_status(self):
        if self.qacct_status['failed'] == '0':
            self.qsub_failed = False
        else:
            self.qsub_failed = True
        if self.qacct_status['exit_status'] == '0':
            self.cmd_failed = False
        else:
            self.cmd_failed = True
        return