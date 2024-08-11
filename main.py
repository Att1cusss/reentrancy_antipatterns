import os
import version
import compile
import mythril_read
import sailfish_read
import securify1_read
import securify2_read
import anti_search
import oyente_read
from slither.slither import Slither


def main():
    # 全局变量
    file_number = 0
    mythril = 0
    mythril_report_count = 0
    mythril_false = 0

    sailfish = 0
    sailfish_report_count = 0
    sailfish_false = 0

    securify1 = 0
    securify1_report_count = 0
    securify1_false = 0

    securify2 = 0
    securify2_report_count = 0
    securify2_false = 0

    oyente = 0
    oyente_report_count = 0
    oyente_false = 0
    conunt = 0
    false = 0

    # 被测数据集：source_file_folder
    source_file_folder = 'RE_random_500'

    # 运行测试数据集：test_file_folder
    test_file_folder = 'want'
    # test_file_folder = 'test_files'
    source_file_folder = test_file_folder

    # 遍历被测数据集，获取一个合约与其对应所有检测报告的文件地址：file_address
    for file_address in os.listdir(source_file_folder):
        # 初始化
        file_number += 1
        print('处理第{}个合约'.format(file_number))

        print('合约与检测结果集合文件地址：', file_address)

        # 当前地址下的文件列表
        file_list = os.listdir(source_file_folder + '/' + file_address)
        print('当前地址下文件列表:', file_list)

        # 查看当前地址下是否存在合约
        if 'contract.sol' in file_list:  # 存在合约
            # 获取合约文件路径
            contract_address = source_file_folder + '/' + file_address + '/' + 'contract.sol'
            print('合约路径：', contract_address)

            # 根据合约路径获取合约版本，后修改版本
            try:
                version.solc_version(contract_address)
            except Exception:
                print('编译失败\n')
                continue  # 跳出当前合约的检测

            # 编译合约文件，存入output.json
            try:
                slither = Slither(contract_address)
                compile.file_compile(contract_address)
                print('编译完成')
            except Exception:
                print('编译失败\n')
                continue  # 跳出当前合约的检测

            print('漏洞检测报告：')
            # 漏洞检测报告中有mythril检测报告
            if 'mythril.txt' in file_list:
                print('\n mythril.txt')
                report_address = source_file_folder + '/' + file_address + '/' + 'mythril.txt'
                mythril_problem = mythril_read.read(report_address)
                print(mythril_problem)
                try:
                    false_count, problem_count = anti_search.anti_search(mythril_problem, slither)
                    conunt += problem_count
                    false += false_count
                    print('mythril的{}个检测结果中中{}个为假阳性'.format(problem_count, false_count))
                    mythril += 1
                    mythril_report_count += problem_count
                    mythril_false += false_count
                except Exception:
                    pass

            # 漏洞检测报告中有sailfish检测报告
            if 'sailfish.json' in file_list:
                print('\n sailfish.json')
                report_address = source_file_folder + '/' + file_address + '/' + 'sailfish.json'
                sailfish_problem = sailfish_read.read(report_address, slither)
                print(sailfish_problem)
                try:
                    false_count, problem_count = anti_search.anti_search(sailfish_problem, slither)
                    conunt += problem_count
                    false += false_count
                    print('sailfish的{}个检测结果中中{}个为假阳性'.format(problem_count, false_count))
                    sailfish += 1
                    sailfish_report_count += problem_count
                    sailfish_false += false_count
                except Exception:
                    pass

            # 漏洞检测报告中有securify1检测报告
            if 'securify1.json' in file_list:
                print('\n securify1.json')
                report_address = source_file_folder + '/' + file_address + '/' + 'securify1.json'
                securify1_problem = securify1_read.read(contract_address, report_address)
                print(securify1_problem)
                try:
                    false_count, problem_count = anti_search.anti_search(securify1_problem, slither)
                    conunt += problem_count
                    false += false_count
                    print('securify1的{}个检测结果中中{}个为假阳性'.format(problem_count, false_count))
                    securify1 += 1
                    securify1_report_count += problem_count
                    securify1_false += false_count
                except Exception:
                    pass

            # 漏洞检测报告中有securify2检测报告
            if 'securify2.txt' in file_list:
                print('\n securify2.txt')
                report_address = source_file_folder + '/' + file_address + '/' + 'securify2.txt'
                securify2_problem = securify2_read.read(contract_address, report_address)
                print(securify2_problem)
                try:
                    false_count, problem_count = anti_search.anti_search(securify2_problem, slither)
                    conunt += problem_count
                    false += false_count
                    print('securify2的{}个检测结果中中{}个为假阳性'.format(problem_count, false_count))
                    securify2 += 1
                    securify2_report_count += problem_count
                    securify2_false += false_count
                except Exception:
                    pass

            # 漏洞检测报告中有oyente检测报告
            if 'oyente.txt' in file_list:
                print('\n oyente.txt')
                report_address = source_file_folder + '/' + file_address + '/' + 'oyente.txt'
                oyente_problem = oyente_read.read(contract_address, report_address)
                print(oyente_problem)
                try:
                    false_count, problem_count = anti_search.anti_search(oyente_problem, slither)
                    conunt += problem_count
                    false += false_count
                    print('oyente的{}个检测结果中中{}个为假阳性'.format(problem_count, false_count))
                    oyente += 1
                    oyente_report_count += problem_count
                    oyente_false += false_count
                except Exception:
                    # print('tiaoguo1')
                    pass
        else:
            print('改地址文件下没有合约')
            continue
        if conunt == 0:
            print('总数为0')
        else:
            print('\n\n')
            print('工具\t\t报告数量\t假阳性\t检测结果总数')
            print('mythril\t\t', mythril,   '\t', mythril_false,   '\t', mythril_report_count)
            print('sailfish\t',  sailfish,  '\t',  sailfish_false, '\t', sailfish_report_count)
            print('securify1\t', securify1, '\t', securify1_false, '\t', securify1_report_count)
            print('securify2\t', securify2, '\t', securify2_false, '\t', securify2_report_count)
            print('oyente\t\t',  oyente,    '\t', oyente_false,    '\t', oyente_report_count)
            print('\n假阳性统计')
            print(false, conunt)
            print('{:.2f}%识别率'.format(100 * float(false) / float(conunt)))
        print('\n\n\n')


if __name__ == '__main__':
    main()

