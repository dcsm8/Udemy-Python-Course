# Filter function


def starts_with_r(friend: str):
    return friend.startswith('R')


friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']

start_with_r = filter(starts_with_r, friends)

another_start_with_r = (friend for friend in friends if friend.startswith('R'))


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


custom_start_with_r = my_custom_filter(
    lambda friend: friend.startswith('R'), friends)

print(list(start_with_r))
print(list(another_start_with_r))
print(list(custom_start_with_r))
