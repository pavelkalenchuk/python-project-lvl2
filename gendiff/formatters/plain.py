"""Module constist 3 functions for  presenting diff tree in a plain format."""

from gendiff.formatters.replaser import replace_bool_none_to_str


def replace_value(value, type_name: str):
    """Return replaced boolean,None type, dict value to str type.
    Parameters:
        value(Any): value for replacing
        type_name(str): type of a value
    Return:
        replced value(str)
    """
    if type_name == "bool" or type_name == "NoneType":
        return replace_bool_none_to_str(value)
    replaced_value = {"dict": "[complex value]", "str": f"'{value}'"}
    return replaced_value.get(type_name, value)


def make_string(key: str, key_description: dict, keys: list):
    """Return string with property name and state and value(s) of the property.
    Parameters:
        key(str): a property name
        key_description(dict): description of a property
        keys(list): key path(for nested dicts) to key
    Return:
        string with  property name and state and value(s) of the property
    """
    copy_keys = keys.copy()
    copy_keys.append(key)
    key_path = ".".join(copy_keys)
    full_key = f"'{key_path}'"
    state = key_description["state"]
    value = key_description["value"]
    type_name = [type(v).__name__ for v in value]

    replaced_value = [replace_value(v, t) for v, t in zip(value, type_name)]
    if state == "modified":
        return (
            f"Property {full_key} was updated. "
            f"From {replaced_value[0]} to {replaced_value[1]}"
        )
    string = {
        "added": f"Property {full_key} was added with value: {replaced_value[0]}",
        "removed": f"Property {full_key} was removed",
    }
    return string[state]


def format(diff: dict):
    """Return string with a sorted keys witn information of a state
       and value(s) of a key in plain format.
    Parameters:
        diff(dict): diff tree
    Return:
        string with a sorted keys witn information of a state
        and value(s) of a key in plain format
    """

    def walk(current_diff, keys):
        all_keys = set(current_diff.keys())
        diff_list = []
        for key in sorted(all_keys):
            key_state = current_diff[key].get("state")
            if key_state == "same":
                continue
            if key_state == "nested":
                copy_keys = keys.copy()
                copy_keys.append(key)
                string = walk(current_diff[key]["value"], copy_keys)
            else:
                string = make_string(key, current_diff[key], keys)
            diff_list.append(string)
        return "\n".join(diff_list)

    return walk(diff, [])
