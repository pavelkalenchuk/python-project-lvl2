import json


def replace_bool_to_str(value):
    NoneType = type(None)
    if isinstance(value, bool):
        if value:
            return "true"
        return "false"
    if isinstance(value, NoneType):
        return "null"
    return value


def decode_json__with_replace_bool_None(first_json, second_json):
    file1 = json.load(open(first_json))
    file2 = json.load(open(second_json))
    return (
        {k: replace_bool_to_str(v) for k, v in file1.items()},
        {k: replace_bool_to_str(v) for k, v in file2.items()},
    )


def generate_diff(first_file, second_file):
    file1, file2 = decode_json__with_replace_bool_None(first_file, second_file)
    all_keys = set(file1) | set(file2)
    result_list = []
    for key in sorted(all_keys):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                item = f"  {key}: {file1[key]}"
            else:
                first_str = f"- {key}: {file1[key]}"
                second_str = f"+ {key}: {file2[key]}"
                item = first_str + "\n  " + second_str
        elif key in file1:
            item = f"- {key}: {file1[key]}"
        elif key in file2:
            item = f"+ {key}: {file2[key]}"
        result_list.append(item)
        diff_str = "\n  ".join(result_list)
        result_str = "{\n  " + diff_str + "\n}"
    return result_str
