"""Module for generate dictionary with defference between 2 dictionary."""


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
    only_dict1_k = {k: dict1[k] for k in only_dict1_keys}
    only_dict2_k = {k: dict2[k] for k in only_dict2_keys}
    modified_k = {
        k: (dict1[k], dict2[k])
        for k in shared_keys
        if dict1[k] != dict2[k] and not is_both_value_dict(dict1[k], dict2[k])
    }
    for k in shared_keys:
        if is_both_value_dict(dict1[k], dict2[k]):
            children[k] = generate_diff(dict1[k], dict2[k])
    diff = {
        "children": children,
        "same_k_and_v": same_k_and_v,
        "modified_k": modified_k,
        "only_dict1_k": only_dict1_k,
        "only_dict2_k": only_dict2_k,
    }
    return diff
