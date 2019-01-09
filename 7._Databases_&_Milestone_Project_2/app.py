from utils import database


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'l':
            list_books()
        if user_input == 'r':
            prompt_read_book()
        if user_input == 'a':
            prompt_add_book()
        if user_input == 'd':
            prompt_delete_book()
        user_input = input(USER_CHOICE)


def print_book(book):
    print(f"""
        - Name: {book['name']}
        - Author: {book['author']}
        - Read: {book['read']}
        """)


def prompt_add_book():
    book_name = input('Enter the book name: ')
    book_author = input('Enter the book author: ')

    database.add_book(book_name, book_author)


def list_books():
    for book in database.get_all_books():
        print_book(book)


def prompt_read_book():
    text = input('Enter the book name: ')
    database.mark_as_read_book(text)


def prompt_delete_book():
    text = input('Enter the book name: ')
    database.delete_book(text)


menu()
