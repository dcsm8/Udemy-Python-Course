# Generators


def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


g = hundred_numbers()

print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2

print(list(g))  # [3 - 99]
