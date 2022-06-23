"""Input data for testing diff_view.py."""


# data for test_diff_view.py:
dict1 = {"a": True, "b": "string", "c": 100}

dict2 = {"a": True, "b": None, "d": {"a": 1}}

all_keys = {"a", "b", "c", "d"}

shared_keys = {"a", "b"}

make_node_info_data = [
    (
        "a",
        {
            "value": [
                True,
            ],
            "state": "same",
        },
    ),
    (
        "b",
        {
            "value": ["string", None],
            "state": "modified",
        },
    ),
    (
        "c",
        {
            "value": [
                100,
            ],
            "state": "removed",
        },
    ),
    (
        "d",
        {
            "value": [
                {"a": 1},
            ],
            "state": "added",
        },
    ),
]

# data for testing is_both_value_dicts function:
is_both_values_dicts_data = [
    ({"a": 1}, {"b": 2}, True),
    ({"a": 1}, "string", False),
    (
        {
            100,
        },
        {"b": 2},
        False,
    ),
    (
        {
            1,
        },
        ("string",),
        False,
    ),
]

# data for testing make nested_node

# nested data for make_diff_view function
nested_dict1 = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {"key": "value", "doge": {"wow": ""}},
    },
    "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
    "group2": {"abc": 12345, "deep": {"id": 45}},
}


nested_dict2 = {
    "common": {
        "follow": False,
        "setting1": "Value 1",
        "setting3": None,
        "setting4": "blah blah",
        "setting5": {"key5": "value5"},
        "setting6": {"key": "value", "ops": "vops", "doge": {"wow": "so much"}},
    },
    "group1": {"foo": "bar", "baz": "bars", "nest": "str"},
    "group3": {"deep": {"id": {"number": 45}}, "fee": 100500},
}

nested_diff = {
    "common": {
        "state": "nested",
        "value": {
            "follow": {
                "state": "added",
                "value": [
                    False,
                ],
            },
            "setting1": {
                "state": "same",
                "value": [
                    "Value 1",
                ],
            },
            "setting2": {
                "state": "removed",
                "value": [
                    200,
                ],
            },
            "setting3": {"state": "modified", "value": [True, None]},
            "setting4": {
                "state": "added",
                "value": [
                    "blah blah",
                ],
            },
            "setting5": {
                "state": "added",
                "value": [
                    {"key5": "value5"},
                ],
            },
            "setting6": {
                "state": "nested",
                "value": {
                    "key": {
                        "state": "same",
                        "value": [
                            "value",
                        ],
                    },
                    "ops": {
                        "state": "added",
                        "value": [
                            "vops",
                        ],
                    },
                    "doge": {
                        "state": "nested",
                        "value": {
                            "wow": {"state": "modified", "value": ["", "so much"]},
                        },
                    },
                },
            },
        },
    },
    "group1": {
        "state": "nested",
        "value": {
            "baz": {"state": "modified", "value": ["bas", "bars"]},
            "foo": {
                "state": "same",
                "value": [
                    "bar",
                ],
            },
            "nest": {"state": "modified", "value": [{"key": "value"}, "str"]},
        },
    },
    "group2": {"state": "removed", "value": [{"abc": 12345, "deep": {"id": 45}}]},
    "group3": {
        "state": "added",
        "value": [{"deep": {"id": {"number": 45}}, "fee": 100500}],
    },
}
