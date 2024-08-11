import anti_modifier
import anti_out
import anti_constructor
import anti_sprcial


def anti_search(problem_list, slither):
    problem_count = len(problem_list)

    false_list = []
    read_list = []
    false = 0

    for problem in problem_list:
        contract_name, function_name = problem
        # print(contract_name, function_name)
        if problem in read_list:
            if problem in false_list:
                false += 1
            continue

        contract_object = None
        function_object = None
        for contract in slither.contracts:
            if contract.name == contract_name:
                for function in contract.functions:
                    if function.name == function_name:
                        contract_object = contract
                        function_object = function
                        break

        if contract_object is None and function_object is None:
            # print('未匹配')
            false += 1
            read_list.append(problem)
            false_list.append(problem)
            continue

        anti_1 = anti_modifier.anti_modifier(function_object)
        anti_2 = anti_out.anti_out(function_object)
        anti_3 = anti_constructor.anti_constructor(function_object)
        anti_4 = anti_sprcial.anti_sprcial(function_object)
        if anti_1 or anti_2 or anti_3 or anti_4:
            false += 1
            false_list.append(problem)
            read_list.append(problem)
    return false, problem_count
