"""Module with 2 functions:
    1) get extension of a file
    2) read data from a file(context manager).
"""


import os


def get_format(filename: str):
    """Return extension of file.
    Parameter:
        name of file(str)
    Return:
        extension(str) of a file
    """
    return os.path.splitext(filename)[1]


def read_file(filename: str):
    """Return data from file.
    Parameter:
        name of file(str)
    Return:
        text(str) from file
    """
    with open(filename) as f:
        return f.read()
