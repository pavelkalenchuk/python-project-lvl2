from gendiff.decode_files import decode_files, replace_bool_none_to_str


first_json = 'tests/fixtures/file1.json'
second_json = 'tests/fixtures/file2.json'

first_yaml = 'tests/fixtures/file1.yaml'
second_yaml = 'tests/fixtures/file2.yaml'

first_yml = 'tests/fixtures/file1.yml'
second_yml = 'tests/fixtures/file2.yml'


result = (
    {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': 'false'},
    {'timeout': 20, 'verbose': 'true', 'host': 'hexlet.io'}
)


def test_decode_files_jsons():
    assert decode_files(first_json, second_json) == result


def test_decode_files_yaml():
    assert decode_files(first_yaml, second_yaml) == result


def test_decode_files_yaml():
    assert decode_files(first_yml, second_yml) == result


def test__replace_bool_to_str():
    assert replace_bool_none_to_str(None) == 'null'
    assert replace_bool_none_to_str(False) == 'false'
    assert replace_bool_none_to_str(True) == 'true'

