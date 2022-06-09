"""Test for formatter 'stylish'."""

from gendiff.formatters.stylish import format_diff_to_string
from tests.test_data.diff_view_data import nested_diff


result_file = "tests/fixtures/stylish.txt"
f = open(result_file, "r")
result_str = f.read()
f.close()


def test_format_diff_to_string():
    assert format_diff_to_string(nested_diff) == result_str
