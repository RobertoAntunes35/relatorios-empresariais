import json

# create a list of dictionaries
people = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "London"},
    {"name": "Bob", "age": 40, "city": "Paris"}
]

# convert the list to a JSON array
json_array = json.dumps(people)

# print the JSON array
print(json_array)
