# Argument Mutability

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}


def see_friend(friends, name):
    print(friends is friends_last_seen)
    print(id(friends))
    friends[name] = 0


print(id(friends_last_seen))

see_friend(friends_last_seen, 'Rolf')

print(friends_last_seen)

print(id(friends_last_seen))

num = 12


def add_number(number):
    number = number + 1
    print(number is num)


add_number(num)

primes = [2, 3, 5]
print(id(primes))

primes += [7, 11]
print(id(primes))

primes = primes + [7, 11]
print(id(primes))
