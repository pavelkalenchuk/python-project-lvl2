"""Replace boolean and None type values in dictianaries to str."""


def replace_bool_none_to_str(value):
    """Return replaced boolean or None type value to str type."""
    bool_or_none = {None: "null", True: "true", False: "false"}
    return bool_or_none[value]
