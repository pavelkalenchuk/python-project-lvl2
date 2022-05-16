"""Results for testing."""


flat_decodes_files = (
    {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False},
    {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
)

flat_diff = {
    "children": {},
    "same_k_and_v": {'host': 'hexlet.io'},
    "same_k_diff_v_dict1": {'timeout': 50},
    "same_k_diff_v_dict2": {'timeout': 20},
    "only_dict1_k": {"follow": False, 'proxy': '123.234.53.22'},
    "only_dict2_k": {'verbose': True}
}

nested_dicoded_file1 = {
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

nested_decoded_file2 = {
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

nested_decoded_files = (
    nested_dicoded_file1,
    nested_decoded_file2
)

nested_diff = {
    "same_k_and_v": {},
    "same_k_diff_v_dict1": {},
    "same_k_diff_v_dict2": {},
    "only_dict1_k": {
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
      }
    }
    },
    "only_dict2_k": {
        "group3": {
            "deep": {
            "id": {
                "number": 45
      }
    },
        "fee": 100500
  }
    },
    'children':{
        "common": {
            "same_k_and_v": {"setting1": "Value 1"},
            "same_k_diff_v_dict1": {'setting3': True},
            "same_k_diff_v_dict2": {"setting3": None},
            "only_dict1_k": {"setting2": 200},
            "only_dict2_k": {"setting4": "blah blah", "follow": False, "setting5": {"key5": "value5"}},
            'children':{
                'setting6': {
                      "same_k_and_v": {"key": "value",},
                      "same_k_diff_v_dict1": {},
                      "same_k_diff_v_dict2": {},
                      "only_dict1_k": {},
                      "only_dict2_k": {"ops": "vops"},
                      'children':{
                        'doge': {
                              "same_k_and_v": {},
                              "same_k_diff_v_dict1": {"wow": ""},
                              "same_k_diff_v_dict2": {"wow": "so much"},
                              "only_dict1_k": {},
                              "only_dict2_k": {},
                              'children':{}
                      }
                    }
              }
            }
            
        },
        "group1": {
            "same_k_and_v": {"foo": "bar"},
            "same_k_diff_v_dict1": {"baz": "bas", "nest": {"key": "value"}},
            "same_k_diff_v_dict2": {"baz": "bars", "nest": "str"},
            "only_dict1_k": {},
            "only_dict2_k": {},
            'children':{}
        }
    }
}



""" a = {
    "same_k_and_v": {},
    "same_k_diff_v_dict1": {},
    "same_k_diff_v_dict2": {},
    "only_dict1_k": {},
    "only_dict2_k": {},
    'children':{}
} """