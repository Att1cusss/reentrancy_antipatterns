import re


def anti_sprcial(function_object):
    # 外部调用列表
    function_calls = {}

    # 外部调用中与经济操作有关的函数名列表
    economy_functions = ['transfer', 'send', 'withdraw', 'approve', 'transferFrom', 'withdrawEther']

    # 函数中所有调用的信息集合
    all_calls = function_object.calls_as_expressions
    for call in all_calls:

        # 匹配每一个调用中被修改的数据，修改使用的函数，修改函数使用的参数
        pattern = r'(?:(\w+)\.)?(\w+)\((.*?)\)'
        match = re.match(pattern, str(call))
        if match:
            # 获取匹配到的函数名和参数
            prefix = match.group(1)
            function_name = match.group(2)
            arguments = match.group(3).split(',')

            # 如果前缀不存在，则设为空字符串
            if prefix is None:
                prefix = ''

            # 记录函数及参数
            if prefix not in function_calls:
                function_calls[prefix] = {}
                if function_name not in function_calls[prefix]:
                    function_calls[prefix][function_name] = []
                    if function_calls[prefix][function_name] is None:
                        function_calls[prefix][function_name] = arguments
                    else:
                        function_calls[prefix][function_name].append(arguments)
                else:
                    function_calls[prefix][function_name].append(arguments)
            else:
                if function_name not in function_calls[prefix]:
                    function_calls[prefix][function_name] = []
                    if function_calls[prefix][function_name] is None:
                        function_calls[prefix][function_name] = arguments
                    else:
                        function_calls[prefix][function_name].append(arguments)
                else:
                    function_calls[prefix][function_name].append(arguments)
        else:
            # print("\tNo match found")
            pass

    # 遍历所有调用信息
    for vair in function_calls:
        functions = function_calls[vair]
        # print('外部调用函数', functions)
        for function in functions:
            if function not in economy_functions:  # 查看外部调用的函数a是否是与经济操作相关的函数
                for argument in function_calls[vair][function]:
                    for arg in argument:
                        if 'msg.value' in arg:
                            return True
                    continue
    return False