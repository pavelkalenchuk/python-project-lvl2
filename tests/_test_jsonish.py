import json

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

#diff_nested_json_file = 'tests/fixtures/result_diff_json'
#f = open(diff_nested_json_file, 'r')
#result_diff_json = f.read()
#f.close()


#testing formatter json
my_json = format_diff_to_json(diff_nested_json)
def test_format_diff_to_json():
    assert is_json(my_json) == True