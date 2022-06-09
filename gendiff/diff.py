"""Module for generate dictionary with info about defference between 2 dictionaries."""

from gendiff.diff_view import make_diff_view
from gendiff.formatters.stylish import format_diff_to_string
from gendiff.formatters.plain import format_diff_to_plain
from gendiff.formatters.jsonish import format_diff_to_json
from gendiff.decode_file import decode_json_yaml


def generate_diff(file_path1, file_path2, format_name="stylish"):
    formatters = {
        "stylish": format_diff_to_string,
        "plain": format_diff_to_plain,
        "json": format_diff_to_json,
    }
    dict1, dict2 = tuple(map(decode_json_yaml, (file_path1, file_path2)))
    diff = make_diff_view(dict1, dict2)
    return formatters[format_name](diff)
