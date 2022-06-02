import pytest

from gendiff.diff import is_dictionary
from gendiff.diff import is_both_value_dict
from gendiff.diff import is_both_value_not_dict
from gendiff.diff import make_diff_view
from gendiff.diff import generate_diff


values1 = [
    ({'a': 1}, True),
    ('foo', False),
    (1, False)
]

values2 = [
    (({'a': 1}, {'b': 2}), True),
    (('foo', {'a': 1}, False)),
    (({'a': 1}, 'foo'), False),
    (('foo', 'baz'), False)
]

values3 = [
    (({'a': 1}, {'b': 2}), False),
    (('foo', {'a': 1}, True)),
    (({'a': 1}, 'foo'), True),
    (('foo', 'baz'), True)
]

