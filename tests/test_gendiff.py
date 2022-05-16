from gendiff.diff import generate_diff
from gendiff.decode_files import decode_files
from tests.fixtures.results import flat_diff
from tests.fixtures.results import nested_diff
from gendiff.stylish import format_diff_to_string


flat_json_1 = 'tests/fixtures/file1.json'
flat_json_2 = 'tests/fixtures/file2.json'

flat_yaml_1 = 'tests/fixtures/file1.yaml'
flat_yaml_2 = 'tests/fixtures/file2.yaml'

nested_json_1 = 'tests/fixtures/file1n.json'
nested_json_2 = 'tests/fixtures/file2n.json'

decoded_flat_json_1, decoded_flat_json_2 = decode_files(flat_json_1, flat_json_2)
decoded_flat_yaml_1, decoded_flat_yaml_2 = decode_files(flat_yaml_1, flat_yaml_2)

decoded_nested_json_1, decoded_nested_json_2 = decode_files(nested_json_1, nested_json_2)

result_file = 'tests/fixtures/result_flat'
f = open(result_file, 'r')
result_str = f.read()
f.close()

diff = generate_diff(decoded_flat_json_1, decoded_flat_json_2)


def test_generate_diff_json():
    assert generate_diff(decoded_flat_json_1, decoded_flat_json_2) == flat_diff
    assert generate_diff(decoded_nested_json_1, decoded_nested_json_2) == nested_diff


""" def test_generate_diff_yaml():
    assert generate_diff(decoded_flat_yaml_1, decoded_flat_yaml_2) == flat_diff """


# testing formatter stylish.py
def test_format_diff_to_string():
    assert format_diff_to_string(diff) == result_str
