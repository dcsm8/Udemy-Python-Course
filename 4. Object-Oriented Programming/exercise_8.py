# Movie class exercise


class Movie:
    def __init__(self, name, director):
        self.name = name
        self.director = director


my_movie = Movie('The Matrix', 'Wachowski')

print(my_movie.name)
print(my_movie.director)
