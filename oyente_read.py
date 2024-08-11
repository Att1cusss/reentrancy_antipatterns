import re
import json
from slither.slither import Slither
from py_solidity_parser.main import *
import solcx


def read(contract_address, report_file):
    with open(report_file, 'r') as file:
        log_output = file.read()
    warning_pattern = re.compile(r'Warning: Re-Entrancy Vulnerability\.', re.MULTILINE)
    relevant_code = []
    for line in log_output.split('\n'):
        if warning_pattern.search(line):
            next_line = next(iter(log_output.split('\n')[log_output.split('\n').index(line) + 1:]), None)
            if next_line and not next_line.startswith('INFO:') and not next_line.startswith('/tmp/'):
                next_line = next_line.strip()
                relevant_code.append(next_line)
    # 打印或返回相关代码段
    line_list = []
    for code in relevant_code:
        # print(code)
        line = find_line_number_in_file(contract_address, code)
        if line is not None:
            line_list.append(line)
    if len(line_list) == 0:
        return []
    line_dic = get_line_dic(contract_address)
    problem_list = []
    for contract in line_dic:
        functions = line_dic[contract]
        for function in functions:
            strat_line, end_line = functions[function]
            for line in line_list:
                if line >= strat_line and line <= end_line:
                    problem = (contract, function)
                    problem_list.append(problem)
            # print(contract, function, strat_line, end_line)
    return problem_list



def find_line_number_in_file(file_path, line_to_find):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if line_to_find in line:
                    return line_number
    except Exception:
        return None
    return None  # 如果没有找到，返回None

def get_line_dic(contract_file):
    output_json = json.load(open('out/output.json'))
    if 'ast' not in output_json["sources"]["destructible"]:
        return {}
    source_node = from_ast(output_json["sources"]["destructible"]["ast"])

    with open(contract_file, 'r') as fp:
        source_code = fp.read()
        fp.close()

    line_dic = {}
    for contract in source_node:
        if contract.nodeType == 'ContractDefinition':
            # print(contract.name)
            line_dic[contract.name] = {}
            (start_line, end_line) = contract.get_line_numbers(source_code)
            # print(start_line, end_line)
            for function in contract:
                if function.nodeType == 'FunctionDefinition':
                    (start_line, end_line) = function.get_line_numbers(source_code)
                    line_dic[contract.name][function.name] = [start_line, end_line]
                # print(function, function.get_line_numbers(source_code))
    return line_dic

