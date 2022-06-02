"""Module present diff in json format."""

import json


def format_diff_to_json(diff):
    """Format diff to json format."""
    return json.dumps(diff, indent=4)
