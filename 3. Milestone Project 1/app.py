"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[X]: Decide where to store movies
[X]: What is the format of a movie?
[X]: Show the user the main interface and get their input
[X]: Allow users to add movies
[X]: Show all their movies
[X]: Find a movie
[X]: Stop running the program when they type 'q'
"""

"""
{
    'name': 'The Matrix',
    'director': 'Wachowskis',
    'year': '1994'
}
"""
movies = [
    {
        'name': 'The Matrix',
        'director': 'Wachowskis',
        'year': '1994'
    },
    {
        'name': 'Moneyball',
        'director': 'Bennett',
        'year': '2011'
    }
]


def menu():
    user_input = input(
        "Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command-please try again.')

        user_input = input(
            "Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit ")


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movie = {
        'name': name,
        'director': director,
        'year': year
    }

    movies.append(movie)


def show_movies():
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    print("------")
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")
    print("------")


def find_movie():
    print('Find movie by')
    print('1. Name')
    print('2. Director')
    print('3. Year')
    options = ['name', 'director', 'year']
    filter_option = input("Select a filter: ")
    filter_option = int(filter_option) - 1

    user_input = input("Enter a value to search: ")
    if filter_option >= 0 and filter_option <= 2:
        movies_result = [
            movie for movie in movies if movie[options[filter_option]] == user_input]

        for movie in movies_result:
            show_movie_details(movie)
    else:
        print('Unknown command-please try again.')


menu()
