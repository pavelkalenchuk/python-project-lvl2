import pytest

from gendiff.diff import generate_diff
from tests.test_data.formatters_data import (
    result_str_stylish,
    result_str_plain,
    result_str_jsonish,
)


json1 = "tests/fixtures/file1.json"
json2 = "tests/fixtures/file2.json"
yaml1 = "tests/fixtures/file1.yaml"
yaml2 = "tests/fixtures/file2.yaml"
yml1 = "tests/fixtures/file1.yml"
yml2 = "tests/fixtures/file2.yml"

input_data = [
    (json1, json2, "stylish", result_str_stylish),
    (json1, json2, "plain", result_str_plain),
    (json1, json2, "json", result_str_jsonish),
    (yaml1, yaml2, "stylish", result_str_stylish),
    (yaml1, yaml2, "plain", result_str_plain),
    (yaml1, yaml2, "json", result_str_jsonish),
    (yml1, yml2, "stylish", result_str_stylish),
    (yml1, yml2, "plain", result_str_plain),
    (yml1, yml2, "json", result_str_jsonish),
    (json1, yaml2, "stylish", result_str_stylish),
    (yaml1, json2, "plain", result_str_plain),
    (json1, yml2, "json", result_str_jsonish),
]


@pytest.mark.parametrize("file1, file2, formatter, result", input_data)
def test_generate_diff(file1, file2, formatter, result):
    assert generate_diff(file1, file2, formatter) == result
