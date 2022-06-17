from gendiff.formatters import stylish
from gendiff.formatters import plain
from gendiff.formatters import jsonish
from tests.test_data.diff_view_data import nested_diff
from tests.test_data.formatters_data import (
    result_str_stylish,
    result_str_plain,
    result_str_jsonish,
)


def test_stylish_format():
    assert stylish.format(nested_diff) == result_str_stylish


def test_plain_format():
    assert plain.format(nested_diff) == result_str_plain


def test_jsonish_format():
    assert jsonish.format(nested_diff) == result_str_jsonish
