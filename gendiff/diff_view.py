"""
Module for  creation a diff(dict type) view between two dictionaries.
Every node in a diff tree is a key with value(dict type).
Value is a key description with 2 keys:
    - "value" of a key
    - "state" of a key:
        - "added": only first dict consist that key
        - "removed": only second dict consist that key
        - "modified": key in a both dicts, but values of a key are different
        - "same": keys in a both dicts, values of a dicts are the same.
        - "nested": keys in a both dicts, values are dicts.
"""


def is_both_values_dicts(value1, value2):
    """Check if values are a dict type.
    Parameters:
        value1(Any): first value
        vale2(Any): second value
    Returns:
        True: both values are dict type
        False: one of values is not a dict type

    """
    if isinstance(value1, dict) and isinstance(value2, dict):
        return True
    return False


def make_node_info(dict1: dict, dict2: dict, key: str, shared_keys: set):
    """Return dict with a  key state, value of a key.
    Parameters:
        dict1(dict): first dict for comparing
        dict2(dict): second dict for comparing
        key(str): key for comparing a state in a dict1, dict2
        shared_keys(set): union of set(dict1) and set(dict2)
    Returns:
        a dict type object with 2 keys:
            "state": state of a key after comparing a state in a dict1, dict2
            "value": value(values) of a key
    """
    added = set(dict2) - set(dict1)
    removed = set(dict1) - set(dict2)
    modified = set(
        k for k in shared_keys if dict1[k] != dict2[k]
    )  # same keys diffent values
    same = set(k for k in shared_keys if dict1[k] == dict2[k])  # same keys equal values
    states = {"added": added, "removed": removed, "modified": modified, "same": same}
    for k in states:
        if key in states[k]:
            state = k
    dict_select = {
        "added": dict2,
        "removed": dict1,
        "modified": (dict1, dict2),
        "same": dict1,
    }
    if state == "modified":
        return {
            "state": state,
            "value": [dict_select["modified"][0][key], dict_select["modified"][1][key]],
        }
    return {"state": state, "value": [dict_select[state][key]]}


def make_diff_view(dict1: dict, dict2: dict):
    """
    Return a tree(dict type) where every node is key with a dict type value,
    value is a key descriotion about a state of a key in a both dicts.
    Parameters:
        dict1(dict): first dict
        dict2(dict): second dict
    Returns:
        diff tree(dict): tree with a nodes are keys form both dict, with a key descriprion
    """
    all_keys = set(dict1) | set(dict2)
    shared_keys = set(dict1) & set(dict2)
    diff_tree = dict()
    for key in all_keys:
        if key in shared_keys and is_both_values_dicts(dict1[key], dict2[key]):
            key_description = {
                "state": "nested",
                "value": make_diff_view(dict1[key], dict2[key]),
            }
        else:
            key_description = make_node_info(dict1, dict2, key, shared_keys)
        diff_tree[key] = key_description
    return diff_tree
