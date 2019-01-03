# List comprehension

numbers = list(range(10))

doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

# using list comprehension

doubled_list_2 = [n*2 for n in numbers]
print(doubled_list_2)

phrases = [f'I am {age} years old' for age in doubled_numbers]
print(phrases)

names_list = ['John', 'Rolf', 'Anne']
lowercase_names = [name.lower() for name in names_list]

print(lowercase_names)

# With conditional

evens = [n for n in doubled_numbers if n % 2 == 0]
print(evens)

friends = ['rolf', 'anna', 'charlie']
guests = ['Jose', 'Rolf', 'ruth', 'Charlie', 'michael']

present_friends = [guest for guest in guests if guest.lower() in friends]
print(present_friends)
