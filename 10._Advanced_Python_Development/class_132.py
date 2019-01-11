# Mutability in Python

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0

print(id(friends_last_seen))
