# Mutable default arguments


def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


a1 = create_account('checking', 'Rolf')
print(a1)

a2 = create_account('saving', 'Jen')
print(a2)

# option to avoid argument mutability problems


def create_account_better(name: str, holder: str, account_holders=None):
    if not account_holders:
        account_holders = []

    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }
