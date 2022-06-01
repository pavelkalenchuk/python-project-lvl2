from itertools import chain
from gendiff.formaters.replaser import replace_str_dict_bool


def make_string(diff, k, keys):
    copy_keys = keys.copy()
    copy_keys.append(k)
    key_path = ".".join(copy_keys)
    key = f"'{key_path}'"
    if k in diff["modified_k"]:
        value1, value2 = tuple(map(replace_str_dict_bool, diff["modified_k"][k]))
        string = f"Property {key} was updated. From {value1} to {value2}"
    elif k in diff["only_dict1_k"]:
        string = f"Property {key} was removed"
    elif k in diff["only_dict2_k"]:
        value = replace_str_dict_bool(diff["only_dict2_k"][k])
        string = f"Property {key} was added with value: {value}"
    return string


def format_diff_to_plain(diff):
    def walk(current_diff, keys):
        same_keys = set(chain.from_iterable(current_diff.values()))
        diff_list = []
        for k in sorted(same_keys):
            if k in current_diff["same_k_and_v"]:
                continue
            if k in current_diff["children"]:
                copy_keys = keys.copy()
                copy_keys.append(k)
                string = walk(current_diff["children"][k], copy_keys)
            else:
                string = make_string(current_diff, k, keys)
            diff_list.append(string)
        diff_result = "\n".join(diff_list)
        return diff_result

    return walk(diff, [])
