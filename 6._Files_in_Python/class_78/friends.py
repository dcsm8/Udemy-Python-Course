people_file = open('people.txt', 'r')

# Ask the user for a list of 3 friends
list_of_friends = ['Rolf', 'Jose', 'Charlie']

people_nearby = [line.strip() for line in people_file.readlines()]
people_file.close()

# For each friend, we'll tell the user whether they are nearby
list_of_friends_set = set(list_of_friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = people_nearby_set.intersection(list_of_friends_set)

nearby_friends_file = open('nearby_friends.txt', 'w')
# For each nearby friend, we'll save their name to `nearby_friends.txt`

for friend in friends_nearby_set:
    print(f'Your friend {friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
# hint: readlines()
