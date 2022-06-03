# 'key':
# 'value':['value', ]  or 'value': ['value1', 'value2']
# 'type': 'nested', 'flat'
# 'status': 'same', 'modified', 'added', 'removed'
# 'children': [{new_node}]


def make_flat_node(key, value, state, type):
    """Return key descriptor."""
    return {
        'key': key,
        'value': value,
        'state': state,
        'type': type
    }


def make_nested_node(key, type, children=[]):
    """Return key descriptor."""
    return {
        'key': key,
        'type': type,
        'children': children
    }


def define_state(dict1, dict2, shared_keys, key):
    """Return key state."""
    added = set(dict1) - set(dict2)
    removed = set(dict2) - set(dict1)
    modified = set(k for k in shared_keys if dict1[k] != dict2[k]) # same keys diffent values
    same = set(k for k in shared_keys if dict1[k] == dict2[k]) # same keys equal values
    states = {
        'added': added,
        'removed': removed,
        'modified': modified,
        'same': same
    }
    for k in states:
        if key in states[k]:
            state = states[k]
            return state


def get_value(dict1, dict2, key, state):
    """Return value of a key."""
    destination = {
        'added': dict2,
        'removed': dict1,
        'modified': (dict1, dict2),
        'same': dict1
    }
    if state == 'modified':
        return [
            destination[state][0][key],
            destination[state][1][key]
        ]
    return [destination[state][key],]


def get_type(value):
    """Return type (flat or nested) of a value."""
    if (isinstance(value, dict)):
        return 'dict'
    return 'flat'


def define_type(value):
    """Return list of types (flat or nested) of values."""
    return [get_type(v) for v in value]


def make_flat_node(dict1, dict2, shared_keys, key):
    """Return key descriptor."""
    state = define_state(dict1, dict2, shared_keys, key)
    value = get_value(dict1, dict2, key, state)
    type = define_type(value)
    return {
        'key': key,
        'value': value,
        'state': state,
        'type': type
    }


def is_both_values_dict(value1, value2):
    """Check if values is a 2 dictionaries."""
    if isinstance(value1, dict) and isinstance(value2, dict):
        return True
    return False


def make_diff_view(dict1, dict2):
    """Generate a list with nodes info about defference between 2 dictionaries."""
    shared_keys = set(dict1) & set(dict2)
    diff_tree = []
    for key in shared_keys:
        if is_both_values_dict(dict1, dict2):
            diff_node = make_nested_node(dict1, dict2, make_diff_view)
        diff_node = make_flat_node(dict1, dict2, shared_keys, key)
        diff_tree.append(diff_node)
    return diff_tree
