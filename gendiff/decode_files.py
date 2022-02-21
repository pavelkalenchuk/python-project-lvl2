import os
import json
import yaml


def replace_bool_none_to_str(value):
    NoneType = type(None)
    # fmt: off
    bool_or_none = {
        None: "null",
        True: "true",
        False: "false"
    }
    # fmt: on
    if isinstance(value, (bool, NoneType)):
        return bool_or_none[value]
    return value


def decode_files(first_file, second_file):
    extension = os.path.splitext(first_file)[1]
    # fmt: off
    file_types = {
        ".json": json.load,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    }
    # fmt: on
    file1 = file_types[extension](open(first_file))
    file2 = file_types[extension](open(second_file))
    return (
        {k: replace_bool_none_to_str(v) for k, v in file1.items()},
        {k: replace_bool_none_to_str(v) for k, v in file2.items()},
    )
