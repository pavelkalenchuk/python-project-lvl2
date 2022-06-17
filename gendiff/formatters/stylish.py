"""Formatter 'stylish'."""

from itertools import chain

from gendiff.formatters.replaser import replace_bool_none_to_str


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


def replace_value(value, type_name, indent):
    if type_name == "dict":
        return stringify(value, indent)
    if type_name == "bool" or type_name == "NoneType":
        return replace_bool_none_to_str(value)
    return value


def make_string(key, key_description, indent):
    """ "Return string with info about a key state."""
    value = key_description["value"]
    state = key_description["state"]
    type_name = [type(v).__name__ for v in value]
    replaced_value = [replace_value(v, t, indent) for v, t in zip(value, type_name)]
    tabulators = {
        "added": [
            "+ ",
        ],
        "removed": [
            "- ",
        ],
        "modified": ["- ", "+ "],
        "same": [
            "  ",
        ],
    }
    tab = tabulators[state]
    if state == "modified":
        string_val1 = f"{indent}{tab[0]}{key}: {replaced_value[0]}\n"
        string_val2 = f"{indent}{tab[1]}{key}: {replaced_value[1]}"
        return f"{string_val1}{string_val2}"
    return f"{indent}{tab[0]}{key}: {replaced_value[0]}"


def format(diff):
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
            state = diff[k].get("state")
            if state == "nested":
                value = walk(diff[k]["value"], deep_indent_size)
                string = f"  {deep_indent}{k}: {value}"
            else:
                string = make_string(k, diff[k], deep_indent)
            diff_list.append(string)
        result = chain("{", diff_list, [current_indent + "}"])
        diff_result = "\n".join(result)
        return diff_result

    return walk(diff, 0)
