"""Module for replace boolean and None type values in dictianaries to str."""
import collections.abc


def replace_bool_none_to_str(value):
    """Replace boolean or None type value to str type."""
    NoneType = type(None)
    bool_or_none = {None: "null", True: "true", False: "false"}
    if isinstance(value, tuple):
        return tuple(map(replace_bool_none_to_str, value))
    if isinstance(value, (bool, NoneType)):
        return bool_or_none[value]
    return value


def replace_bool_none(diff):
    """Replace boolean or None type values in nested dictionaries to str."""
    if isinstance(diff, collections.abc.Mapping):
        return {k: replace_bool_none(v) for k, v in diff.items()}
    else:
        return replace_bool_none_to_str(diff)


def replace_str_dict_bool(value):
    """Replace boolean, None type, dict to values for plain formatter."""
    NoneType = type(None)
    bool_or_none = {None: "null", True: "true", False: "false"}
    if isinstance(value, (bool, NoneType)):
        return bool_or_none[value]
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, dict):
        return f'{"[complex value]"}'
    return value
