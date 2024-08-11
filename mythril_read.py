import re


def read(report_file):
    with open(report_file, 'r') as file:
        content = file.read()

    # 结合检测报告中的固定格式，在检测报告中获取信息
    pattern = (r"==== External Call To User-Supplied Address "
               r"====\nSWC ID: \d+\nSeverity: "
               r"\w+\nContract: ([^\n]+)\nFunction name: ([^\n]+)")
    matches = re.findall(pattern, content)

    pattern = (r"==== State access after external call "
               r"====\nSWC ID: \d+\nSeverity: "
               r"\w+\nContract: ([^\n]+)\nFunction name: ([^\n]+)")
    matches += re.findall(pattern, content)

    # 将检测报告中重复出现的函数剔除，使每个疑似存在漏洞的函数只出现一次
    match_list = []
    for item in matches:
        contract_name, function_real = item
        function_name = function_real.split('(')[0]
        problem_item = (contract_name, function_name)
        if problem_item in match_list:
            pass
        else:
            match_list.append(problem_item)
    # 查看mythril检测报告中是否存在有可重入漏洞检测结果
    # if match_list:
        # print('  mythril报告中与可重入漏洞相关的信息：')
        # for item in match_list:
        #     contract_name, function_name = item
        #     print('   Contract: ', contract_name, end=', ')
        #     print('   Function: ', function_name)
    # else:
    #     print("mythril检测结果中未找到匹配的结果。")
    return match_list
