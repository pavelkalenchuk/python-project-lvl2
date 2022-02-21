"""Return defferense betweeт 2 dictionaries."""


def generate_diff(file1, file2):
    all_keys = set(file1) | set(file2)
    result_list = []
    for key in sorted(all_keys):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                item = f"  {key}: {file1[key]}"
            else:
                first_str = f"- {key}: {file1[key]}"
                second_str = f"+ {key}: {file2[key]}"
                item = first_str + "\n  " + second_str
        elif key in file1:
            item = f"- {key}: {file1[key]}"
        elif key in file2:
            item = f"+ {key}: {file2[key]}"
        result_list.append(item)
        diff_str = "\n  ".join(result_list)
        result_str = "{\n  " + diff_str + "\n}"
    return result_str
