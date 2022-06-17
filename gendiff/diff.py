"""Module generate diff between 2 files in user's choice format."""

import gendiff.formatters.stylish
import gendiff.formatters.plain
import gendiff.formatters.jsonish

from gendiff.diff_view import make_diff_view
from gendiff.parse import parse, get_format, read_file


def generate_diff(file_path1, file_path2, format_name="stylish"):
    """Return diff str depend formatter."""
    formatters = {
        "stylish": gendiff.formatters.stylish.format,
        "plain": gendiff.formatters.plain.format,
        "json": gendiff.formatters.jsonish.format,
    }
    dict1 = parse(read_file(file_path1), get_format(file_path1))
    dict2 = parse(read_file(file_path2), get_format(file_path2))
    diff = make_diff_view(dict1, dict2)
    return formatters[format_name](diff)


