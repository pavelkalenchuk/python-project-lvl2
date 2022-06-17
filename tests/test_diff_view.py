import pytest

from gendiff.diff_view import is_both_values_dicts
from tests.test_data.diff_view_data import is_both_values_dicts_data

from gendiff.diff_view import make_node_info
from tests.test_data.diff_view_data import dict1, dict2, shared_keys, make_node_info_data

from gendiff.diff_view import make_diff_view
from tests.test_data.diff_view_data import nested_dict1, nested_dict2, nested_diff


@pytest.mark.parametrize("value1, value2, result", is_both_values_dicts_data)
def test_is_both_values_dicts(value1, value2, result):
    assert is_both_values_dicts(value1, value2) == result


@pytest.mark.parametrize("key, result", make_node_info_data)
def test_make_node_info(key, result):
    assert make_node_info(dict1, dict2, key, shared_keys ) == result


def test_make_diff_view():
    assert make_diff_view(nested_dict1, nested_dict2) == nested_diff
