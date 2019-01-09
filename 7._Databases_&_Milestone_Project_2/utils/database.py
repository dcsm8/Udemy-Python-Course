"""
Concerned with storing and retrieving books from a list
"""

"""
{
    'name': 'Harry Potter',
    'author': 'Rowling',
    'read': False
}
"""

books = [
    {
        'name': 'Harry Potter',
        'author': 'Rowling',
        'read': False
    },
    {
        'name': 'The Da Vinci Code',
        'author': 'Dan Brown',
        'read': True
    },
    {
        'name': 'The Hobbit',
        'author': 'J. R. R. Tolkien',
        'read': False
    },
    {
        'name': '1984',
        'author': 'George Orwell',
        'read': True
    },
    {
        'name': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'read': False
    }
]


def add_book(name, author):
    books.append({
        'name': name,
        'author': author,
        'read': False
    })


def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]


def mark_as_read_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


def get_all_books():
    return books
