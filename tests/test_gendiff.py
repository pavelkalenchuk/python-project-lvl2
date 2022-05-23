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

nested_yaml_1 = 'tests/fixtures/file1n.yaml'
nested_yaml_2 = 'tests/fixtures/file2n.yaml'

decoded_flat_json_1, decoded_flat_json_2 = decode_files(flat_json_1, flat_json_2)
decoded_flat_yaml_1, decoded_flat_yaml_2 = decode_files(flat_yaml_1, flat_yaml_2)

decoded_nested_json_1, decoded_nested_json_2 = decode_files(nested_json_1, nested_json_2)
decoded_nested_yaml_1, decoded_nested_yaml_2 = decode_files(nested_yaml_1, nested_yaml_2)



flat_result_file = 'tests/fixtures/result_flat'
f = open(flat_result_file, 'r')
result_flat_str = f.read()
f.close()

nested_result_file = 'tests/fixtures/result_nested'
f = open(nested_result_file, 'r')
result_nested_str = f.read()
f.close()

diff_flat_json = generate_diff(decoded_flat_json_1, decoded_flat_json_2)
diff_nested_json = generate_diff(decoded_nested_json_1, decoded_nested_json_2)

diff_flat_yaml = generate_diff(decoded_flat_yaml_1, decoded_flat_yaml_2)
diff_nested_yaml= generate_diff(decoded_nested_yaml_1, decoded_nested_yaml_2)




def test_generate_diff_json():
    assert generate_diff(decoded_flat_json_1, decoded_flat_json_2) == flat_diff
    assert generate_diff(decoded_nested_json_1, decoded_nested_json_2) == nested_diff
    assert generate_diff(decoded_flat_yaml_1, decoded_flat_yaml_2) == flat_diff
    assert generate_diff(decoded_nested_yaml_1, decoded_nested_yaml_2) == nested_diff


# testing formatter stylish.py
def test_format_diff_to_string():
    assert format_diff_to_string(diff_flat_json) == result_flat_str
    assert format_diff_to_string(diff_nested_json) == result_nested_str
    assert format_diff_to_string(diff_flat_json) == result_flat_str
    assert format_diff_to_string(diff_nested_yaml) == result_nested_str
