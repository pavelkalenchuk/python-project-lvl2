"""Module for decode jsonm yaml, yml files to python dicttionaries"""

import os
import json
import yaml


def decode_json_yaml(file):
    extension = os.path.splitext(file)[1]
    file_types = {
        ".json": json.load,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    }
    decoded_file = file_types[extension](open(file))
    return decoded_file


def decode_files(first_file, second_file):
    decoded_files = tuple(map(decode_json_yaml, (first_file, second_file)))
    return decoded_files
