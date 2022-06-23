"""Module for parsing data from file."""


import json
import yaml


def parse(data: str, format: str):
    """Return dict from json, yaml, yml files.
    Parameters:
        data(str): text from file
        format(str): extension of a file
    Return:
        dict type object
    """
    file_types = {
        ".json": json.loads,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    }
    return file_types[format](data)
