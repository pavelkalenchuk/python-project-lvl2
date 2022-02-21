from gendiff.engine import generate_diff
from gendiff.decode_files import decode_files


first_json = 'tests/fixtures/file1.json'
second_json = 'tests/fixtures/file2.json'

first_yaml = 'tests/fixtures/file1.yaml'
second_yaml = 'tests/fixtures/file2.yaml'

result_file = 'tests/fixtures/result'


f = open(result_file, 'r')
result_str = f.read()
f.close()

first_file_json, second_file_json = decode_files(first_json, second_json)
first_file_yaml, second_file_yaml = decode_files(first_yaml, second_yaml)


def test_generate_diff_json():
    assert generate_diff(first_file_json, second_file_json) == result_str


def test_generate_diff():
    assert generate_diff(first_file_yaml, second_file_yaml) == result_str
