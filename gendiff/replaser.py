"""Module for replace boolean and None type values in dictianaries to str."""
import collections.abc


def replace_bool_none_to_str(value):
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


def replace_bool_none(ob):
    """Replace bool or None type values in nested dictionaries to str."""
    if isinstance(ob, collections.abc.Mapping):
        return {k: replace_bool_none(v) for k, v in ob.items()}
    else:
        return replace_bool_none_to_str(ob)
