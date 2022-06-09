"""Formatter 'stylish'."""

from itertools import chain

from gendiff.formatters.replaser import replace_bool_none_to_str
from icecream import ic

def stringify(value, key_indent):
    """Format value to string with indent."""
    len_indent = len(key_indent)
    start_indent = len_indent + 6

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        if depth == 0:
            deep_indent_size = start_indent
            deep_indent = " " * deep_indent_size
            current_indent = " " * (len_indent + 2)
        else:
            deep_indent_size = depth + 4
            deep_indent = " " * deep_indent_size
            current_indent = " " * (deep_indent_size - 4)
        lines = []
        for key, val in current_value.items():
            lines.append(f"{deep_indent}{key}: {iter_(val, deep_indent_size)}")
        result = chain("{", lines, [current_indent + "}"])
        return "\n".join(result)

    return iter_(value, 0)


def replace_value(value, type, indent):
    if type == 'dict':
        return stringify(value, indent)
    if type == 'bool_none':
        return replace_bool_none_to_str(value)
    return value



def make_string(key, description, indent):
    """"Return string with info about a key state."""
    value = description['value']
    type = description['type']
    state = description['state']
    replaced_value = [replace_value(v, t, indent) for v, t in zip(value, type)]
    tabulators = {
        'added': ['+ ', ],
        'removed': ['- ', ],
        'modified': ['- ', '+ '],
        'same': ['  ', ]
    }
    tab = tabulators[state]
    if state == 'modified':
        string_val1 = (
            f'{indent}{tab[0]}{key}: {replaced_value[0]}\n'
        )
        string_val2 = (
            f'{indent}{tab[1]}{key}: {replaced_value[1]}'
        )
        return f"{string_val1}{string_val2}"
    return f"{indent}{tab[0]}{key}: {replaced_value[0]}"


def format_diff_to_string(diff):
    """Return string with formatted diff."""

    def walk(diff, depth):
        all_keys = set(diff.keys())
        diff_list = []
        if depth == 0:
            deep_indent_size = depth + 2
            current_indent = " " * depth
        else:
            deep_indent_size = depth + 4
            current_indent = " " * (depth + 2)
        deep_indent = " " * deep_indent_size
        for k in sorted(all_keys):
            if diff[k]['type'] == 'nested':
                value = walk(diff[k]['children'], deep_indent_size)
                string = f'  {deep_indent}{k}: {value}'
            else:
                string = make_string(k, diff[k], deep_indent)
            diff_list.append(string)
        result = chain("{", diff_list, [current_indent + "}"])
        diff_result = "\n".join(result)
        return diff_result

    return walk(diff,0)







nested_diff = {
    'common':{
        'type': 'nested',
        'children': {
                'follow': {
                    'value': [False,],
                    'type': ['bool_none',],
                    'state': 'added'
                },
                'setting1':{
                    'value': ['Value 1', ],
                    'type': ['flat' , ],
                    'state': 'same'
                },
                'setting2': {
                    'value': [200, ],
                    'type': ['flat', ],
                    'state': 'removed'
                },
                'setting3': {
                    'value': [True, None],
                    'type': ['bool_none', 'bool_none'],
                    'state': 'modified' 
                },
                'setting4': {
                    'value': ['blah blah', ],
                    'type': ['flat', ],
                    'state':'added'

                },
                'setting5': {
                    'value': [{'key5': 'value5'}, ],
                    'type': ['dict', ],
                    'state':'added'
                    
                },
                'setting6': {
                        'type': 'nested',
                        'children': {
                            'key': {
                                'value': ['value', ],
                                'type': ['flat', ],
                                'state':'same'
                            },
                            'ops': {
                                'value': ['vops', ],
                                'type': ['flat', ],
                                'state':'added'
                            },
                            'doge': {
                                'type': 'nested',
                                'children': {
                                    'wow':{
                                        'value': ['', 'so much'],
                                        'type': ['flat', 'flat'],
                                        'state': 'modified'
                                    }
                                }
                            }
                        }
                }
        },
    },
    'group1': {
        'type': 'nested',
        'children': {
            'baz': {
                'value': ['bas', 'bars'],
                'type': ['flat', 'flat'],
                'state': 'modified'
            },
            'foo': {
                'value': ['bar'],
                'type': ['flat', ],
                'state': 'same'
            },
            'nest':{
                'value': [{"key": "value"}, 'str'],
                'type': ['dict', 'flat'],
                'state': 'modified'
            }
        }
     },
    'group2': {
            'value': [{"abc": 12345, "deep": {"id": 45}}, ],
            'type': ['dict', ],
            'state': 'removed'
    },
    'group3': {
            'value': [{"deep": {"id": {"number": 45}}, "fee": 100500}, ],
            'type': ['dict', ],
            'state': 'added'
    }
}
print(format_diff_to_string(nested_diff))

