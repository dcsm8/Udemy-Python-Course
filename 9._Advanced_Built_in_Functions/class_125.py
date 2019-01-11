# Map function

friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']

friends_lower = map(lambda x: x.lower(), friends)

print(list(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users_list = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'anna', 'password': '321'}
]

users = [User.from_dict(user) for user in users_list]

another_users = map(User.from_dict, users_list)

print(next(another_users).username)
print(next(another_users).username)
