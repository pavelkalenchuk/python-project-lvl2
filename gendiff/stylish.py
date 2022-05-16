"""Formater."""

from itertools import chain
from gendiff.replaser import replace_bool_none
from icecream import ic


""" def format_diff_to_string(diff):
    '''Format differense between 2 dictionaries to result string.'''
    diff = replace_bool_none(diff)
    ic(diff.keys())
    ic(diff.values())
    same_keys = set(chain.from_iterable(diff.values()))
    ic(same_keys)
    diff_list = []
    for k in sorted(same_keys):
        ic(k)
        if k in diff['children']:
            value = format_diff_to_string(diff['children'][k])
            string = f'{k}: {value}'  # format_diff_to_string(diff['children'][k])
        if k in diff["same_k_and_v"]:
            string = f'  {k}: {diff["same_k_and_v"][k]}'
        elif k in diff["same_k_diff_v_dict1"] and k in diff["same_k_diff_v_dict2"]:
            dict1_diff_string = f'- {k}: {diff["same_k_diff_v_dict1"][k]}\n'
            dict2_diff_string = f'  + {k}: {diff["same_k_diff_v_dict2"][k]}'
            string = f"{dict1_diff_string}{dict2_diff_string}"
        elif k in diff["only_dict1_k"]:
            string = f'- {k}: {diff["only_dict1_k"][k]}'
        elif k in diff["only_dict2_k"]:
            string = f'+ {k}: {diff["only_dict2_k"][k]}'
        diff_list.append(string)
    diff_string = "\n  ".join(diff_list)
    diff_result = "{\n  " + diff_string + "\n}"
    return diff_result """


def format_diff_to_string(diff):
    def walk(current_diff):
        current_diff = replace_bool_none(current_diff)
        ic(current_diff.keys())
        ic(current_diff.values())
        same_keys = set(chain.from_iterable(current_diff.values()))
        ic(same_keys)
        diff_list = []
        for k in sorted(same_keys):
            ic(k)
            if k in current_diff["children"]:
                value = walk(current_diff["children"][k])
                string = f"{k}: {value}"  # format_diff_to_string(current_diff['children'][k])
            if k in current_diff["same_k_and_v"]:
                string = f'  {k}: {current_diff["same_k_and_v"][k]}'
            elif (
                k in current_diff["same_k_diff_v_dict1"]
                and k in current_diff["same_k_diff_v_dict2"]
            ):
                dict1_diff_string = f'- {k}: {current_diff["same_k_diff_v_dict1"][k]}\n'
                dict2_diff_string = f'  + {k}: {current_diff["same_k_diff_v_dict2"][k]}'
                string = f"{dict1_diff_string}{dict2_diff_string}"
            elif k in current_diff["only_dict1_k"]:
                string = f'- {k}: {current_diff["only_dict1_k"][k]}'
            elif k in current_diff["only_dict2_k"]:
                string = f'+ {k}: {current_diff["only_dict2_k"][k]}'
            diff_list.append(string)
        diff_string = "\n  ".join(diff_list)
        diff_result = "{\n  " + diff_string + "\n}"
        return diff_result

    return walk(diff)
