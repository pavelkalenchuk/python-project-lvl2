from gendiff.replaser import replace_bool_none
from gendiff.replaser import replace_bool_none_to_str

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

def test__replace_bool_to_str():
    assert replace_bool_none_to_str(None) == 'null'
    assert replace_bool_none_to_str(False) == 'false'
    assert replace_bool_none_to_str(True) == 'true'


def test_replace_bool_none():
    assert replace_bool_none(flat_dict) == flat_result
    assert replace_bool_none(nested_dict) == nested_result
