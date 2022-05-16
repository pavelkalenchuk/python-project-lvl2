""" def generate_diff(file1, file2):
    all_keys = set(file1) & set(file2)
    only_file1_keys = set(file1) - set(file2)
    only_file2_keys = set(file2) - set(file1)
    diff = {
        "same_k_and_v": {k: file1[k] for k in all_keys if file1[k] == file2[k]},
        "same_k_diff_v_file1": {k: file1[k] for k in all_keys if file1[k] != file2[k]},
        "same_k_diff_v_file2": {k: file2[k] for k in all_keys if file1[k] != file2[k]},
        "only_file1_k": {k: file1[k] for k in only_file1_keys},
        "only_file2_k": {k: file2[k] for k in only_file2_keys},
    }
    return diff
 """


def is_dictionary(item):
    if isinstance(item, dict):
        return True
    return False


def is_both_value_dict(value1, value2):
    if is_dictionary(value1) and is_dictionary(value2):
        return True
    return False


def is_both_value_not_dict(value1, value2):
    if not is_dictionary(value1) and not is_dictionary(value2):
        return True
    return False


def generate_diff(dict1, dict2):
    shared_keys = set(dict1) & set(dict2)
    only_dict1_keys = set(dict1) - set(dict2)
    only_dict2_keys = set(dict2) - set(dict1)
    children = dict()
    same_k_and_v = {
        k: dict1[k]
        for k in shared_keys
        if dict1[k] == dict2[k] and is_both_value_not_dict(dict1[k], dict2[k])
    }
    same_k_diff_v_dict1 = {
        k: dict1[k]
        for k in shared_keys
        if dict1[k] != dict2[k] and not is_both_value_dict(dict1[k], dict2[k])
    }
    same_k_diff_v_dict2 = {
        k: dict2[k]
        for k in shared_keys
        if dict1[k] != dict2[k] and not is_both_value_dict(dict1[k], dict2[k])
    }
    only_dict1_k = {k: dict1[k] for k in only_dict1_keys}
    only_dict2_k = {k: dict2[k] for k in only_dict2_keys}
    for k in shared_keys:
        if is_both_value_dict(dict1[k], dict2[k]):
            children[k] = generate_diff(dict1[k], dict2[k])
    diff = {
        "children": children,
        "same_k_and_v": same_k_and_v,
        "same_k_diff_v_dict1": same_k_diff_v_dict1,
        "same_k_diff_v_dict2": same_k_diff_v_dict2,
        "only_dict1_k": only_dict1_k,
        "only_dict2_k": only_dict2_k,
    }
    return diff
