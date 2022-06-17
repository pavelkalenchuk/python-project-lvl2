"""A module return a diff view between two dictionaries."""


def is_both_values_dicts(value1, value2):
    """Check if values is a 2 dictionaries."""
    if isinstance(value1, dict) and isinstance(value2, dict):
        return True
    return False


def make_node_info(dict1, dict2, key, shared_keys):
    """Return key state, value of a key."""
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


def make_diff_view(dict1, dict2):
    """
    Return a tree where every node is a dict
    with info about state of a key from 2 dicts.
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
