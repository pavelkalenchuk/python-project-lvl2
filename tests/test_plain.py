"""Test for formatter 'plain'."""

from gendiff.formatters.plain import format_diff_to_plain
from tests.test_data.diff_view_data import nested_diff


result_file = 'tests/fixtures/plain.txt'
f = open(result_file, 'r')
result_str = f.read()
f.close()


def test_format_diff_to_plain():
    assert format_diff_to_plain(nested_diff) == result_str