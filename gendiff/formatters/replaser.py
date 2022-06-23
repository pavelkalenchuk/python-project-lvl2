"""Module consist 1 function for replacing boolean and None type values to str."""


def replace_bool_none_to_str(value):
    """Return replaced boolean or None type value to str type.
    Parameter:
        value(Any): value for replacing
    Return:
        string with replaced value
    """
    bool_or_none = {None: "null", True: "true", False: "false"}
    return bool_or_none[value]
