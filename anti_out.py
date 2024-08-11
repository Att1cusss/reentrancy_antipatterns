import re


def anti_out(function_object):
    state_variables_written_list = function_object.state_variables_written
    if len(state_variables_written_list) == 0:
        return True

    # 外部调用列表
    function_calls = {}

    # 内部调用列表
    internal_calls = function_object.all_internal_calls()

    # 外部调用中与经济操作有关的函数名列表
    risk_functions = ['transfer', 'send', 'withdraw']

    # 内部调用函数名列表
    internal_calls_name = []
    for call in internal_calls:
        # print('1', call.name)
        internal_calls_name.append(call.name)

    # 函数中所有调用的信息集合
    all_calls = function_object.calls_as_expressions
    for call in all_calls:
        # print('2', call)

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

            # 将内部调用从所有调用中剔除，只保留外部调用信息
            if function_name in internal_calls_name:
                continue

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

    # print('外部调用', function_calls)

    # 获取函数写入的状态变量列表
    state_vairables_written = function_object.state_variables_written
    # for call in state_vairables_written:
    #     print('125', call)

    # 遍历外部调用信息，查看是否有与经济操作的函数调用之后修改了状态变量
    for vair in function_calls:
        functions = function_calls[vair]
        for function in functions:
            if function in risk_functions:  # 查看外部调用的函数a是否是与经济操作相关的函数
                vair_list = [vair]
                for arguments in function_calls[vair][function]:
                    vair_list += arguments
                # print('12345', vair_list)
                risk_vair = [x for x in vair_list if x in state_vairables_written]
                # print('1827', risk_vair)
                if not risk_vair:
                    return True

    # 外部调用中与经济操作有关的函数名列表
    economy_functions = ['transfer', 'send', 'withdraw', 'receive', 'transferFrom']

    # 安全的外部调用
    safe_function = ['balanceOf', 'receiveApproval']
    # 遍历外部调用信息
    for vair in function_calls:
        functions = function_calls[vair]
        # print('外部调用函数', functions)
        for function in functions:
            if function not in economy_functions:  # 查看外部调用的函数a是否是与经济操作相关的函数
                if function in safe_function:
                    continue
                # print('不安全的经济操作函数', function)
                return False
    return True

    # return False