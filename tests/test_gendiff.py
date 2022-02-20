from gendiff.engine import generate_diff


file1 = '/home/pavel/projects/python-project-lvl2/tests/fixtures/file1.json'
file2 = '/home/pavel/projects/python-project-lvl2/tests/fixtures/file2.json'
result_file = '/home/pavel/projects/python-project-lvl2/tests/fixtures/result.txt'


f = open(result_file, 'r')
result_str = f.read()
f.close()


def test_generate_diff():
    assert generate_diff(file1, file2) == result_str

