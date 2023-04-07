import json
'Python JSON --> '
'Python JSON stands for JavaScript Object Notation'
'JSON contains data that is send or received to and from a server.'
'JSON is simply a string which follows a format similar to the Python Dictionary'

# Example :- Basic JSON String
sampleJSON = '{"first_name":"Romeo","last_name":"Siwach","age":"30"}'
print(type(sampleJSON))
print(sampleJSON)

'# JSON to Dictionary :-'
'Before we can individually access the data present in a JSON , we need to convert it into a Python dictionary first'
'To do that we need to imnport json module first'
'To convert JSON to Dictionary , use [json.loads()] method'
'This method parses a JSON and returns a Dictionary'

'# Dictionary to JSON :-'
'To convert a Dictionary to a JSON, we need to use [json.dumps()] method'
'Sample dictionary should not be taken in single quotes only curly braces are required'

'# JSON Formatting :-'
'JSON formatting is done by using parameter of JSON, [json.dumps()] method'

'# Saving JSON Files :-'
'As JSON is similar to a string so we can save them like a plain text by using .json file extension. ex- filename.json'

# Example 1:-

sampleJson = '{"First_name":"Romeo","Last_name":"Siwach","Age":"30"}'
print(type(sampleJson))
print(sampleJson)

json_dictionary = json.loads(sampleJson)
print(type(json_dictionary))
print(json_dictionary)

# Example 2:-
sampleDictionary = {"First_name":"Romeo","Last_name":"Siwach","Age":"30"}
print(type(sampleDictionary))
print(sampleDictionary)

dictionary_json = json.dumps(sampleDictionary, indent=4)
print(type(dictionary_json))
print(dictionary_json)
