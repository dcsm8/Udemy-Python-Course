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

books_file = 'books.txt'


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


def mark_as_read_book(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'

    _save_all_books(books)


def _save_all_books(books):
    books = [f"{book['name']},{book['author']},{book['read']}" for book in books]
    with open(books_file, 'w') as file:
        for book in books:
            file.write("%s\n" % book)


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    books = [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]

    return books
