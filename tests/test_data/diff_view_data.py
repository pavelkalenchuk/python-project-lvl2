"""Input data for testing diff_view.py."""


# data for testing get_type function
get_type_data = [
    ({'key': 1}, 'dict'),
    ('string', 'flat'),
    (100, 'flat'), 
    ([1, 2], 'flat'),
    ({1}, 'flat'),
    (('string', ), 'flat'),
    ('', 'flat'),
    (True, 'bool_none'),
    (False, 'bool_none'),
    (None, 'bool_none')
]

# data for testing define_type function
define_type_data = [
    ([{'a': 1}, ], ['dict', ]),
    (['string',], ['flat', ]),
    ([{'a': 1}, 'string'], ['dict', 'flat']),
    ([{'a': 1}, {'a': 1}], ['dict', 'dict']),
    ([1, 1], ['flat', 'flat']),
    ([], [])
]

# data for testing define_type, get_value, make_flat_node functions:
dict1 = {
    'a': True,
    'b': "string",
    'c': 100
}

dict2 = {
    'a': True,
    'b': 'number',
    'd': {'a': 1}
}

all_keys = {'a', 'b', 'c', 'd'}

shared_keys = {'a', 'b'}

# data for testing define_type functions:
define_state_data = [
    ('a', 'same'),
    ('b', 'modified'),
    ('c', 'removed'),
    ('d', 'added')
]

# data for testing get_value function:
get_value_data = [
    ('a', 'same', [True, ]),
    ('b', 'modified', ['string', 'number']),
    ('c', 'removed', [100, ]),
    ('d', 'added', [{'a': 1}])
]

# data for testing make flat node:
make_flat_node_data = [
    ('a', {
            'value': [True, ],
            'state': 'same',
            'type': ['bool_none', ]
            }
    ),
    ('b', {
            'value': ['string', 'number'],
            'state': 'modified',
            'type': ['flat', 'flat']
            }
    ),
    ('c', {
            'value': [100, ],
            'state': 'removed',
            'type': ['flat', ]
            }
    ),
    ('d', {
            'value': [{'a': 1}, ],
            'state': 'added',
            'type': ['dict', ]
            }
    ),
]

# data for testing is_both_value_dicts:
is_both_values_dicts_data = [
    ({'a': 1}, {'b': 2}, True),
    ({'a': 1}, 'string', False),
    ({100, }, {'b': 2}, False),
    ({1, }, ('string', ), False)
]

# nested data for make_diff_view function
nested_dict1 = {
    "common": {
      "setting1": "Value 1",
      "setting2": 200,
      "setting3": True,
      "setting6": {
        "key": "value",
        "doge": {
          "wow": ""
        }
      }
    },
    "group1": {
      "baz": "bas",
      "foo": "bar",
      "nest": {
        "key": "value"
      }
    },
    "group2": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  }


nested_dict2 = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}

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