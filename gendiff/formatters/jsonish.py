"""Module present diff in json format."""

import json


def format(diff):
    """Format diff to json format."""
    return json.dumps(diff, indent=4, sort_keys=True)
