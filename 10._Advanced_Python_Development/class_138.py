# Python collections

from collections import defaultdict
"""
* counter
* defaultdict  
* ordereddict
* namedtuple
* deque
"""

from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])


coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'),
             ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = {}

for coworker in coworkers:
    if coworker[0] not in alma_maters:
        alma_maters[coworker[0]] = []
    alma_maters[coworker[0]].append(coworker[1])

print(alma_maters)

alma_maters = defaultdict(list)

for coworker in coworkers:
    alma_maters[coworker[0]].append(coworker[1])

print(alma_maters)


o = OrderedDict()

o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)


account = ('checking', 1850.90)

Account = namedtuple('Account', ['name', 'balance'])

account_tuple = Account(*account)

print(account_tuple)
print(account_tuple.name)
print(account_tuple.balance)


friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
print(friends)

friends.append('Jose')
friends.appendleft('Jose')
print(friends)

friends.pop()
friends.popleft()
print(friends)
