"""Module for replace boolean and None type values in dictianaries to str."""
import collections.abc


def replace_bool_none_to_str_(value):
    """Replace bool or None type value to str type to str."""
    NoneType = type(None)
    bool_or_none = {None: "null", True: "true", False: "false"}
    if isinstance(value, tuple):
        value_1, value_2 = value
        if isinstance(value_1, (bool, NoneType)):
            replaced_value_1 = bool_or_none[value_1]
        else:
            replaced_value_1 = value_1
        if isinstance(value_2, (bool, NoneType)):
            replaced_value_2 = bool_or_none[value_2]
        else:
            replaced_value_2 = value_2
        return replaced_value_1, replaced_value_2
    if isinstance(value, (bool, NoneType)):
        return bool_or_none[value]
    return value


def replace_bool_none_to_str(value):
    """Replace bool or None type value to str type."""
    NoneType = type(None)
    bool_or_none = {None: "null", True: "true", False: "false"}
    if isinstance(value, tuple):
        return tuple(map(replace_bool_none_to_str, value))
    if isinstance(value, (bool, NoneType)):
        return bool_or_none[value]
    return value


def replace_bool_none(diff):
    """Replace bool or None type values in nested dictionaries to str."""
    if isinstance(diff, collections.abc.Mapping):
        return {k: replace_bool_none(v) for k, v in diff.items()}
    else:
        return replace_bool_none_to_str(diff)


def replace_str_dict_bool(value):
    NoneType = type(None)
    bool_or_none = {None: "null", True: "true", False: "false"}
    if isinstance(value, (bool, NoneType)):
        return bool_or_none[value]
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, dict):
        return f'{"[complex value]"}'
    return value
