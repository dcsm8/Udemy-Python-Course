import json
"""
Concerned with storing and retrieving books from a csv file
Format of the csv file:

name,author,read
"""

"""
{
    'name': 'Harry Potter',
    'author': 'Rowling',
    'read': False
}
"""

books_file = 'books.json'


def add_book(name, author):
    books = get_all_books()
    with open(books_file, 'w') as file:
        books.append({
            'name': name,
            'author': author,
            'read': False
        })
        _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


def mark_as_read_book(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True

    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)
