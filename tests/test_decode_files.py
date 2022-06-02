import pytest

from gendiff.decode_files import decode_files
from tests.fixtures.results import flat_decoded_files


first_json = 'tests/fixtures/file1.json'
second_json = 'tests/fixtures/file2.json'

first_yaml = 'tests/fixtures/file1.yaml'
second_yaml = 'tests/fixtures/file2.yaml'

first_yml = 'tests/fixtures/file1.yml'
second_yml = 'tests/fixtures/file2.yml'

files = [
    (first_json, second_json),
    (first_yaml, second_yaml),
    (first_yml, second_yaml)
]


@pytest.mark.parametrize('file1, file2', files)
def test_decode_files(file1, file2):
    assert decode_files(file1, file2) == flat_decoded_files
