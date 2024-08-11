from slither.slither import Slither
import json


def read(report_file, slither):
    problem_list = []
    function_list = []
    report_json = json.load(open(report_file))

    for report in report_json:
        bug_type = report_json[report]['bug_type']
        if bug_type == 'dao':
            function_name = report_json[report]['from_function']
            # if function_name in function_list:
            #     pass
            # else:
            function_list.append(function_name)
    # print('jadihiuwhaudhauidh', function_list)
    for contract in slither.contracts:
        # print(contract.name)
        for function in contract.functions:
            # print('\t', function.name)
            if function.name in function_list:
                problem_list.append((contract.name, function.name))
    # print('PROBLEM', problem_list)
    # if problem_list:
    #     print('sailfish报告中与可重入漏洞相关的信息：')
    #     for (contract_name, function_name) in problem_list:
    #         print('Contract: ' + contract_name + ', Function: ' + function_name)
    #     return problem_list
    # else:
    #     print("sailfish检测结果中未找到匹配的结果。")
    #     return []
    return problem_list