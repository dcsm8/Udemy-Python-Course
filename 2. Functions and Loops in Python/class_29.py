# Set and dictionary comprehensions

friends = {'rolf', 'anna', 'charlie'}
guests = {'jose', 'rolf', 'ruth', 'charlie', 'michael'}

# guests.intersection(friends)
present_friends = [friend for friend in guests & friends]
print(present_friends)

names = ['Rolf', 'Anna', 'Charlie']
time_last_seen = [10, 15, 8]

friends_list = {names[i]: time_last_seen[i] for i in range(len(names))}
print(friends_list)

friends_last_seen = dict(zip(names, time_last_seen))
