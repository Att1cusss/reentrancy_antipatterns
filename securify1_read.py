import json
from slither.slither import Slither
from py_solidity_parser.main import *
import solcx


def read(contract_address, report_address):
    contract_file = contract_address
    report_file = report_address

    # with open(contract_file, 'r') as fp:
    #     source_code = fp.read()
    #     fp.close()

    # print(contract_file, report_file)
    report_json = json.load(open(report_file))
    contracts = report_json['analysis']
    line_dic = get_line_dic(contract_file)

    # print(line_dic)
    line_result = {}  # 字典，存储数据为{合约名（字符）：行数（列表）}
    for key in contracts:
        contract_name = key.split('sol:')[-1]  # 找到报告中的合约节点中合约名字
        # print(contract_name, end='')
        if 'DAO' not in contracts[key]['results']:
            continue
        dao_lines = contracts[key]['results']['DAO']['warnings']
        if len(dao_lines) == 1 and dao_lines[0] == -1:
            pass
        else:
            line_result[contract_name] = dao_lines
        # print(dao_lines)
    # print(line_result)
    problem_list = get_problem(line_dic, line_result)
    # if problem_list:
    #     print('securify1报告中与可重入漏洞相关的信息：')
    #     for (contract_name, function_name) in problem_list:
    #         print('Contract: ' + contract_name + ', Function: ' + function_name)
    #     return problem_list
    # else:
    #     print("securify1检测结果中未找到匹配的结果。")
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
        if contract in line_dic:
            function_line_list = line_dic[contract]
        else:
            function_line_list = []
        for problem_line in problem_line_list:
            for function in function_line_list:
                (start_line, end_line) = function_line_list[function]
                if start_line <= problem_line <= end_line:
                    problem_list.append((contract, function))
                    break

    return problem_list
