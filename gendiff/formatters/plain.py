from gendiff.formatters.replaser import replace_bool_none_to_str


def replace_value(value, type):
    if type == "bool" or type == "NoneType":
        return replace_bool_none_to_str(value)
    replaced_value = {"dict": "[complex value]", "str": f"'{value}'"}
    return replaced_value.get(type, value)


def make_string(key, key_description, keys):
    copy_keys = keys.copy()
    copy_keys.append(key)
    key_path = ".".join(copy_keys)
    full_key = f"'{key_path}'"
    value = key_description["value"]
    type = key_description["type"]
    state = key_description["state"]
    replaced_value = [replace_value(v, t) for v, t in zip(value, type)]
    if state == "modified":
        return (
            f"Property {full_key} was updated. "
            f"From {replaced_value[0]} to {replaced_value[1]}"
        )
    string = {
        "added": f"Property {full_key} was added with value: {replaced_value[0]}",
        "removed": f"Property {full_key} was removed",
    }
    return string[state]


def format_diff_to_plain(diff):
    """Return diff in  plain view."""

    def walk(current_diff, keys):
        all_keys = set(current_diff.keys())
        diff_list = []
        for key in sorted(all_keys):
            key_state = current_diff[key].get("state")
            if key_state == "same":
                continue
            if key_state == "nested":
                copy_keys = keys.copy()
                copy_keys.append(key)
                string = walk(current_diff[key]["children"], copy_keys)
            else:
                string = make_string(key, current_diff[key], keys)
            diff_list.append(string)
        return "\n".join(diff_list)

    return walk(diff, [])
