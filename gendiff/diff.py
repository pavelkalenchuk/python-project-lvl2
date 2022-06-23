"""Generate diff between 2 files in user's choice format."""

import gendiff.formatters.stylish
import gendiff.formatters.plain
import gendiff.formatters.jsonish

from gendiff.diff_view import make_diff_view
from gendiff.parse import parse
from gendiff.read_file import get_format, read_file


def generate_diff(file_path1: str, file_path2: str, format_name="stylish"):
    """Return diff str depending on the formatter.
    Parameters:
        file_path1(str): path to first file
        file_path2(str): path to second file
        format_name(str): name of a formatter
    Returns:
        string(str) with a differnse between 2 configuration file(json, yaml, yml),
        fomatted by on of a three formatters
    """
    formatters = {
        "stylish": gendiff.formatters.stylish.format,
        "plain": gendiff.formatters.plain.format,
        "json": gendiff.formatters.jsonish.format,
    }
    dict1 = parse(read_file(file_path1), get_format(file_path1))
    dict2 = parse(read_file(file_path2), get_format(file_path2))
    diff = make_diff_view(dict1, dict2)
    return formatters[format_name](diff)
