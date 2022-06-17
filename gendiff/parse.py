"""Module for decode jsonm yaml, yml files to python dicttionaries"""


import os
import json
import yaml


""" def decode_json_yaml(file):
    extension = os.path.splitext(file)[1]
    file_types = {
        ".json": json.load,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    }
    decoded_file = file_types[extension](open(file))
    return decoded_file """


def get_format(filename):
    return os.path.splitext(filename)[1]


def read_file(filename):
    with open(filename) as f:
        return f.read()


def parse(data, format):
    file_types = {
        ".json": json.loads,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    }
    return file_types[format](data)
