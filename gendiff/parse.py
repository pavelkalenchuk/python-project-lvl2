"""Decode json, yaml, yml files to python dicttionaries"""


import os
import json
import yaml


def get_format(filename):
    """Return extension of file."""
    return os.path.splitext(filename)[1]


def read_file(filename):
    """Return data from file."""
    with open(filename) as f:
        return f.read()


def parse(data, format):
    """Return dict from json, yaml files."""
    file_types = {
        ".json": json.loads,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    }
    return file_types[format](data)
