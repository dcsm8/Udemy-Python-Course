# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

import json

csv_file = open('csv_file.txt', 'r')
csv_data = [line.strip() for line in csv_file.readlines()]
csv_file.close()
clubs = []

for item in csv_data:
    club, city, country = item.split(',')
    clubs.append({
        'club': club,
        'city': city,
        'country': country
    })

json_file = open('json_file.txt', 'w')
json.dump(clubs, json_file)
json_file.close()
