# For loops, range(), and tuple destructuring in Python

primes = [2, 3, 5, 7, 11]

for prime in primes:
    print(f'{prime} is a prime number.')

kid_ages = (3, 7, 12)

for age in kid_ages:
    print(f'I have a {age} year old kid')

for i in range(20):
    print(i)

my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}

for name, days in my_friends.items():
    print(f'I last saw {name} {days} days ago.')

who_do_i_know = 'Anne'

# The in keyword can be used in any iterable
if who_do_i_know in my_friends:
    print('I know Anne')
