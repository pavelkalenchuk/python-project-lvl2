"""Module for replace boolean and None type values in dictianaries."""
import collections.abc


def replace_bool_none_to_str(value):
    """Replace bool or None type value to str type."""
    NoneType = type(None)
    bool_or_none = {None: "null", True: "true", False: "false"}
    if isinstance(value, (bool, NoneType)):
        return bool_or_none[value]
    return value


def replace_bool_none(ob):
    """Replace bool or None type values in nested dictionaries."""
    if isinstance(ob, collections.abc.Mapping):
        return {k: replace_bool_none(v) for k, v in ob.items()}
    else:
        return replace_bool_none_to_str(ob)
