from .database_connection import DatabaseConnection
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


def create_book_table():
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `book` (
            `id`	INTEGER PRIMARY KEY AUTOINCREMENT,
            `name`	TEXT NOT NULL,
            `author`	TEXT NOT NULL,
            `read`	INTEGER NOT NULL
        )""")


def add_book(name, author):
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO book(name, author, read) VALUES(?, ?, 0)', (name, author))


def delete_book(name):
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM book WHERE name=?', (name,))


def mark_as_read_book(name):
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE book SET read=1 WHERE name=?', (name,))


def get_all_books():
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM book')
        books = [{'id': row[0], 'name': row[1], 'author': row[2], 'read': row[3]}
                 for row in cursor.fetchall()]
        return books


create_book_table()
