import re
import json
from slither.slither import Slither
from py_solidity_parser.main import *
import solcx


def read(contract_address, report_file):
    contract_file = contract_address
    problem_list = []
    with open(report_file, 'r') as file:
        content = file.read()

    pattern = (r"Pattern:\s+.*Reentrancy\n"  # 匹配Pattern行
               r"Description:.*\n"  # 匹配Description行
               r"[\s\S]*?"  # 匹配任意字符（包括换行符）
               r"Type:.*\n"  # 匹配Type行
               r"Contract:\s+([^\n]+)\n"  # 匹配Contract行
               r"Line:\s+(\d+)")  # 匹配Line行

    matches = re.findall(pattern, content)
    line_result = {}
    for match in matches:
        (contract, line) = match
        # print(line)
        if contract not in line_result:
            line_result[contract] = [int(line)]
        else:
            if int(line) not in line_result[contract]:
                line_result[contract].append(int(line))
    line_dic = get_line_dic(contract_file)
    problem_list = get_problem(line_dic, line_result)
    return problem_list


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


def get_problem(line_dic, line_result):
    problem_list = []
    for contract in line_result:
        problem_line_list = line_result[contract]
        if contract not in line_dic:
            continue
        function_line_list = line_dic[contract]
        for problem_line in problem_line_list:
            for function in function_line_list:
                (start_line, end_line) = function_line_list[function]
                if start_line <= problem_line <= end_line:
                    problem_list.append((contract, function))
                    break

    return problem_list