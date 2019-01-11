# Enumarete Function

top_friends = ['Jose', 'Rolf', 'Anna']

for i, friend in enumerate(top_friends):
    print(f'My top {i+1} friend is {friend}')

friend_g = enumerate(top_friends)
print(next(friend_g))
