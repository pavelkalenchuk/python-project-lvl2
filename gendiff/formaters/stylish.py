"""Formater."""

from itertools import chain
from gendiff.formaters.replaser import replace_bool_none


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


def make_string(k, diff, indent):
    """Make string depend key status."""
    if k in diff["modified_k"]:
        dict1_diff_string = (
            f'{indent}- {k}: {stringify(diff["modified_k"][k][0], indent)}\n'
        )
        dict2_diff_string = (
            f'{indent}+ {k}: {stringify(diff["modified_k"][k][1], indent)}'
        )
        string = f"{dict1_diff_string}{dict2_diff_string}"
        return string
    if k in diff["same_k_and_v"]:
        tab = "  "
        val = diff["same_k_and_v"][k]
    elif k in diff["only_dict1_k"]:
        tab = "- "
        val = diff["only_dict1_k"][k]
    elif k in diff["only_dict2_k"]:
        tab = "+ "
        val = diff["only_dict2_k"][k]
    string = f"{indent}{tab}{k}: {stringify(val, indent)}"
    return string


def format_diff_to_string(diff):
    def walk(current_diff, depth):
        current_diff = replace_bool_none(current_diff)
        same_keys = set(chain.from_iterable(current_diff.values()))
        diff_list = []
        if depth == 0:
            deep_indent_size = depth + 2
            current_indent = " " * depth
        else:
            deep_indent_size = depth + 4
            current_indent = " " * (depth + 2)
        deep_indent = " " * deep_indent_size
        for k in sorted(same_keys):
            if k in current_diff["children"]:
                value = walk(current_diff["children"][k], deep_indent_size)
                string = f"  {deep_indent}{k}: {value}"
            else:
                string = make_string(k, current_diff, deep_indent)
            diff_list.append(string)
        result = chain("{", diff_list, [current_indent + "}"])
        diff_result = "\n".join(result)
        return diff_result

    return walk(diff, 0)
