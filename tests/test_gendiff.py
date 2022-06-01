from pydoc import plain
from gendiff.diff import generate_diff
from gendiff.decode_files import decode_files
from tests.fixtures.results import flat_diff
from tests.fixtures.results import nested_diff
from gendiff.formaters.stylish import format_diff_to_string
from gendiff.formaters.plain import format_diff_to_plain
from gendiff.formaters.jsonish import format_diff_to_json
import json

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True


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

flat_plain_result_file = 'tests/fixtures/result_plain_flat'
f = open(flat_plain_result_file, 'r')
result_plain_flat = f.read()
f.close()

nested_plain_result_file = 'tests/fixtures/result_plain_nested'
f = open(nested_plain_result_file, 'r')
result_plain_nested = f.read()
f.close()

#diff_nested_json_file = 'tests/fixtures/result_diff_json'
#f = open(diff_nested_json_file, 'r')
#result_diff_json = f.read()
#f.close()



diff_flat_json = generate_diff(decoded_flat_json_1, decoded_flat_json_2)
diff_nested_json = generate_diff(decoded_nested_json_1, decoded_nested_json_2)

diff_flat_yaml = generate_diff(decoded_flat_yaml_1, decoded_flat_yaml_2)
diff_nested_yaml= generate_diff(decoded_nested_yaml_1, decoded_nested_yaml_2)




def test_generate_diff_json():
    assert generate_diff(decoded_flat_json_1, decoded_flat_json_2) == flat_diff
    assert generate_diff(decoded_nested_json_1, decoded_nested_json_2) == nested_diff
    assert generate_diff(decoded_flat_yaml_1, decoded_flat_yaml_2) == flat_diff
    assert generate_diff(decoded_nested_yaml_1, decoded_nested_yaml_2) == nested_diff


# testing formatter stylish
def test_format_diff_to_string():
    assert format_diff_to_string(diff_flat_json) == result_flat_str
    assert format_diff_to_string(diff_nested_json) == result_nested_str
    assert format_diff_to_string(diff_flat_json) == result_flat_str
    assert format_diff_to_string(diff_nested_yaml) == result_nested_str


#testing formatter plain.py
def test_format_diff_to_plain():
    assert format_diff_to_plain(diff_flat_json) == result_plain_flat
    assert format_diff_to_plain(diff_nested_json) == result_plain_nested


#testing formatter json
my_json = format_diff_to_json(diff_nested_json)
def test_format_diff_to_json():
    assert is_json(my_json) == True
