import re
import subprocess
import time


def solc_version(contract_file):
    version_get = get_version(contract_file)
    # print('1: ', version_get, end=':::')
    # print(type(version_get))
    version = ''
    version_list = ['0.8.9',  '0.8.8',  '0.8.7',  '0.8.6',  '0.8.5',  '0.8.4',  '0.8.3',  '0.8.25', '0.8.24', '0.8.23',
                    '0.8.22', '0.8.21', '0.8.20', '0.8.2',  '0.8.19', '0.8.18', '0.8.17', '0.8.16', '0.8.15', '0.8.14',
                    '0.8.13', '0.8.12', '0.8.11', '0.8.10', '0.8.1',  '0.8.0',  '0.7.6',  '0.7.5',  '0.7.4',  '0.7.3',
                    '0.7.2',  '0.7.1',  '0.7.0',  '0.6.9',  '0.6.8',  '0.6.7',  '0.6.6',  '0.6.5',  '0.6.4',  '0.6.3',
                    '0.6.2',  '0.6.12', '0.6.11', '0.6.10', '0.6.1',  '0.6.0',  '0.5.9',  '0.5.8',  '0.5.7',  '0.5.6',
                    '0.5.5',  '0.5.4',  '0.5.3',  '0.5.2',  '0.5.17', '0.5.16', '0.5.15', '0.5.14', '0.5.13', '0.5.12',
                    '0.5.11', '0.5.10', '0.5.1',  '0.5.0',  '0.4.9',  '0.4.8',  '0.4.7',  '0.4.6',  '0.4.5',  '0.4.26',
                    '0.4.25', '0.4.24', '0.4.23', '0.4.22', '0.4.21', '0.4.20', '0.4.2',  '0.4.19', '0.4.18', '0.4.17',
                    '0.4.16', '0.4.15', '0.4.14', '0.4.13', '0.4.12', '0.4.11', '0.4.10', '0.4.1']

    pattern = r'>=(\d+\.\d+\.\d+)'
    match = re.match(pattern, version_get)
    if match:
        version = match.group(1)
        # print('2', match.group(1))
    else:
        version = version_get
        # print('3', version_get)
    if version not in version_list:
        print('version_not_exist', version)
        return False
    print('Version: {}'.format(version))
    version_switch(version)
    return True


def get_version(contract_file):
    version = '0.0.0'
    with open(contract_file, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(r'pragma solidity ([^;]+);', line)
            if match:
                version = match.group(1)
                # print('Version: {}'.format(version))
                version = version.split('^')[-1]
                break
    return version


def version_switch(version):
    cmd = 'solc-select use ' + version
    execute_cmd_with_timeout(cmd)
    print('切换solc版本为' + version)


def execute_cmd_with_timeout(cmd, timeout=300):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    t_beginning = time.time()
    seconds_passed = 0
    while True:
        seconds_passed = time.time() - t_beginning
        if p.poll() is not None:
            return str(round(float(seconds_passed), 2))
        if seconds_passed > timeout:
            p.terminate()
            return 'timeout, seconds_passed:' + str(timeout)
        time.sleep(0.1)