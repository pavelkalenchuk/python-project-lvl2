from gendiff.decode_files import decode_files
from tests.fixtures.results import flat_decodes_files


first_json = 'tests/fixtures/file1.json'
second_json = 'tests/fixtures/file2.json'

first_yaml = 'tests/fixtures/file1.yaml'
second_yaml = 'tests/fixtures/file2.yaml'

first_yml = 'tests/fixtures/file1.yml'
second_yml = 'tests/fixtures/file2.yml'


def test_decode_files_jsons():
    assert decode_files(first_json, second_json) == flat_decodes_files


def test_decode_files_yaml():
    assert decode_files(first_yaml, second_yaml) == flat_decodes_files


def test_decode_files_yml():
    assert decode_files(first_yml, second_yml) == flat_decodes_files
