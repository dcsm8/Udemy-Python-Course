# Any and All functions

friends = [
    {
        'name': 'Rolf',
        'location': 'Washington, D.C.'
    },
    {
        'name': 'Anna',
        'location': 'San Francisco'
    },
    {
        'name': 'Charlie',
        'location': 'San Francisco'
    },
    {
        'name': 'Jose',
        'location': 'San Francisco'
    },
]

your_location = input('Where are you right now? ')

friend_nearby = [
    friend for friend in friends if friend['location'] == your_location]

if any(friend_nearby):
    print('You are not alone')

print(all([0, 1, 2, 3, 4, 5]))
