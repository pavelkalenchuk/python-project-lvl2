def define_type(value):
    """Return list of types (flat or dict) of values."""
    return [type(v).__name__ for v in value]


def define_state(dict1, dict2, shared_keys, key):
    """Return key state."""
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
            return state


def get_value(dict1, dict2, key, state):
    """Return value of a key."""
    dict_states = {
        "added": dict2,
        "removed": dict1,
        "modified": (dict1, dict2),
        "same": dict1,
    }
    if state == "modified":
        return [dict_states[state][0][key], dict_states[state][1][key]]
    return [
        dict_states[state][key],
    ]


def make_flat_node(dict1, dict2, shared_keys, key):
    """Return key descriptor."""
    state = define_state(dict1, dict2, shared_keys, key)
    value = get_value(dict1, dict2, key, state)
    type = define_type(value)
    return {"value": value, "state": state, "type": type}


def is_both_values_dicts(value1, value2):
    """Check if values is a 2 dictionaries."""
    if isinstance(value1, dict) and isinstance(value2, dict):
        return True
    return False


def make_nested_node(state, children):
    """Return key descriptor."""
    return {"state": state, "children": children}


def make_diff_view(dict1, dict2):
    """Return a tree where every node is a dict with info about
    type and state of a key from both dicts."""
    all_keys = set(dict1) | set(dict2)
    shared_keys = set(dict1) & set(dict2)
    diff_tree = dict()
    for key in all_keys:
        if key in shared_keys and is_both_values_dicts(dict1[key], dict2[key]):
            diff_node = make_nested_node(
                "nested", make_diff_view(dict1[key], dict2[key])
            )
        else:
            diff_node = make_flat_node(dict1, dict2, shared_keys, key)
        diff_tree[key] = diff_node
    return diff_tree
