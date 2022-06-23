"""Module present diff in JSON format."""

import json


def format(diff: dict):
    """Return string in JSON fromat.
    Paramater:
        diff(dict): diff tree
    Return:
        JSON formatted string(str) with sorted keys from diff tree
        with indent in 4 spaces
    """
    return json.dumps(diff, indent=4, sort_keys=True)
