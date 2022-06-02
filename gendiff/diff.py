"""Module for generate dictionary with info about defference between 2 dictionaries."""

from gendiff.formaters.stylish import format_diff_to_string
from gendiff.formaters.plain import format_diff_to_plain
from gendiff.formaters.jsonish import format_diff_to_json
from gendiff.decode_file import decode_json_yaml


def is_dictionary(value):
    """Check if value is a dictionary."""
    if isinstance(value, dict):
        return True
    return False


def is_both_value_dict(value1, value2):
    """Check if values is a 2 dictionaries."""
    if is_dictionary(value1) and is_dictionary(value2):
        return True
    return False


""" def is_both_value_not_dict(value1, value2):
    """ "Check if both values is not a dictionaries. """"
    if not is_dictionary(value1) and not is_dictionary(value2):
        return True
    return False """


def make_diff_view(dict1, dict2):
    """Generate a dictionary with info about defference between 2 dictionaries."""
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
            children[k] = make_diff_view(dict1[k], dict2[k])
    return {
        "children": children,
        "same_k_and_v": same_k_and_v,
        "modified_k": modified_k,
        "only_dict1_k": only_dict1_k,
        "only_dict2_k": only_dict2_k,
    }


def generate_diff(file_path1, file_path2, format_name):
    formatters = {
        "stylish": format_diff_to_string,
        "plain": format_diff_to_plain,
        "json": format_diff_to_json,
    }
    dict1, dict2 = tuple(map(decode_json_yaml, (file_path1, file_path2)))
    diff = make_diff_view(dict1, dict2)
    return formatters[format_name](diff)
