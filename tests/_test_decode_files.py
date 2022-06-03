import pytest

from gendiff.decode_file import decode_file
from tests.fixtures.results import nested_dicoded_file

files = {
    'json': 'tests/fixtures/file1.json',
    'yaml': 'tests/fixtures/file1.yaml',
    'yml': 'tests/fixtures/file1.yml'
}


@pytest.mark.parametrize('file', files.values())
def test_decode_file(file):
    assert decode_file(file) == nested_dicoded_file
