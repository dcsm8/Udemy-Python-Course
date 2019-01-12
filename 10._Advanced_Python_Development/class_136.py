# Argument Unpacking

accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str) -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]


transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-23.90, 'checking'),
    (-13.00, 'checking'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600.50, 'savings'),
]

for t in transactions:
    amount, name = t
    print(add_balance(*t))
    print(add_balance(amount, name))
    print(add_balance(amount=t[0], name=t[1]))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}
]

user_objects = map(User.from_dict, users)

# Dictionary unpacking

user_objects = [User(username=data['username'],
                     password=data['password']) for data in users]

print(user_objects)

user_objects = [User(**data) for data in users]
