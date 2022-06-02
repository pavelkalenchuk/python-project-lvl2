import pytest
from gendiff.formaters.replaser import replace_bool_none
from gendiff.formaters.replaser import replace_bool_none_to_str
from gendiff.formaters.replaser import replace_str_dict_bool

string = 'string'
number = 100

flat_dict = {
    'a': True,
    'b': False,
    'c': None,
    'd': string,
    'e': number
}

nested_dict = {
    'a': True,
    'a_1': string,
    'a_2': number, 
    'b': {
        'c': False,
        'c_1': string,
        'd': {
            'e': None,
            'e_1': number
        }
    }
}

flat_result = {
    'a': 'true',
    'b': 'false',
    'c': 'null',
    'd': 'string',
    'e': 100
}

nested_result = {
    'a': 'true',
    'a_1': 'string',
    'a_2': 100, 
    'b': {
        'c': 'false',
        'c_1': 'string',
        'd': {
            'e': 'null',
            'e_1': 100
        }
    }
}

values1 = [
    (None, 'null'),
    (True, 'true'),
    (False, 'false'),
    ((None, False), ('null', 'false')),
    ((number, False), (number, 'false')),
    (number, number),
    (string, string),
]

values2 = [
    (None, 'null'),
    (True, 'true'),
    (False, 'false'),
    (number, number),
    (string, f"'{string}'"),
    ({'a': 1}, "[complex value]")
]


@pytest.mark.parametrize('value1, replaced_value1', values1)
def test_replace_bool_to_str(value1, replaced_value1):
    assert(replace_bool_none_to_str(value1)) == replaced_value1


def test_replace_bool_none():
    assert replace_bool_none(flat_dict) == flat_result
    assert replace_bool_none(nested_dict) == nested_result


@pytest.mark.parametrize('value2, replaced_value2', values2)
def test_replace_str_dict_bool(value2, replaced_value2):
    assert(replace_str_dict_bool(value2)) == replaced_value2
