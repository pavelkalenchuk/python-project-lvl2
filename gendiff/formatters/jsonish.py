"""Module present diff in json format."""

import json


def format(diff):
    """Return string in json fromat."""
    return json.dumps(diff, indent=4, sort_keys=True)
