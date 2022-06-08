import pytest


from gendiff.diff_view import get_type, is_both_values_dicts
from tests.test_data.diff_view_data import get_type_data

from gendiff.diff_view import define_type
from tests.test_data.diff_view_data import define_type_data

from gendiff.diff_view import define_state
from tests.test_data.diff_view_data import dict1, dict2, shared_keys, define_state_data

from gendiff.diff_view import get_value
from tests.test_data.diff_view_data import get_value_data

from gendiff.diff_view import make_flat_node
from tests.test_data.diff_view_data import make_flat_node_data

from gendiff.diff_view import is_both_values_dicts
from tests.test_data.diff_view_data import is_both_values_dicts_data

from gendiff.diff_view import make_diff_view
from tests.test_data.diff_view_data import nested_dict1, nested_dict2, nested_diff



@pytest.mark.parametrize('value, result', get_type_data)
def test_get_type(value, result):
    assert get_type(value) == result


@pytest.mark.parametrize('value, result', define_type_data)
def test_define_type(value, result):
    assert define_type(value) == result


@pytest.mark.parametrize('key, state', define_state_data)
def test_define_state(key, state):
    assert define_state(dict1, dict2, shared_keys, key) == state


@pytest.mark.parametrize('key, state, value', get_value_data)
def test_get_value(key, state, value):
    get_value(dict1, dict2, key, state) == value


@pytest.mark.parametrize('key, flat_node', make_flat_node_data)
def test_make_flat_node(key, flat_node):
    assert make_flat_node(dict1, dict2, shared_keys, key) == flat_node


@pytest.mark.parametrize('value1, value2, result', is_both_values_dicts_data)
def test_is_both_values_dicts(value1, value2, result):
    assert is_both_values_dicts(value1, value2) == result

def test_make_diff_view():
    assert make_diff_view(nested_dict1, nested_dict2) == nested_diff


