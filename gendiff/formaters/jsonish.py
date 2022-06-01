import json


def format_diff_to_json(diff):
    return json.dumps(diff, indent=4)
