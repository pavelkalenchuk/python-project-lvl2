# only_dict2_k -- > Property [PATH_TO_KEY] was added with value: [VALUE] 
# only_dict1_k -- > Prorerty [PATH_TO_KEY] was removed
# midified_k -- > Property [PATH_TO_KEY] was updated. From [VALUE[0]] to [VALUE[1]]
# [VALUE] == dict -- >  bla bla bla value: [complex value]


def is_dict(value):
    if isinstance(value, dict):
        return '[complex value]'
    return value
        


def make_string(k, diff):
    if k in diff["modified_k"]:
        value1, value2 = map(is_dict, diff["modified_k"])
        string = f'Property {k} was updated. From {value_1} to {value_2}'
    elif k in diff["only_dict1_k"]:
        value = diff["only_dict1_k"][k]
        string = f'Property {k} was removed'
    elif k in diff["only_dict2_k"]:
        value = diff["only_dict2_k"][k]
        string = f'Property {k} was added with value: {value}'
    return string