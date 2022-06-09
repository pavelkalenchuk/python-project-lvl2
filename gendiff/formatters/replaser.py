"""Module for replace boolean and None type values in dictianaries to str."""
import collections.abc


def replace_bool_none_to_str(value):
    """Replace boolean or None type value to str type."""
    bool_or_none = {None: "null", True: "true", False: "false"}
    return bool_or_none[value]


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
