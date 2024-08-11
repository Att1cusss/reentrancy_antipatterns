import json
import solcx


def file_compile(contract_file):
    input_json = json.load(open('input.json'))
    with open(contract_file, 'r') as fp:
        source_code = fp.read()
        fp.close()
    input_json["sources"]["destructible"]["content"] = source_code
    output_json = solcx.compile_standard(input_json)
    output_json_file = 'out/output.json'  # 编译结果存放地址
    with open(output_json_file, 'w', encoding='utf8') as fp:
        json.dump(output_json, fp, indent=4)
    fp.close()