import json

file = open('friends_json.txt')
file_contents = json.load(file)
file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'},
]

json_output_file = open('json_output.json', 'w')
json.dump(cars, json_output_file, indent=4)

print(cars)
