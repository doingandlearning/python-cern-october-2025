import csv
import random


class Movie:
    def __init__(self, title, year, genre, director):
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "director": self.director,
        }

    def __repr__(self):
        return f"Movie({self.title}, {self.year}, {self.genre}, {self.director})"

    def generate_random_rating(self):
        return random.randint(1, 5)


movies = []

with open("movies.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader)
    for row in reader:
        movies.append(Movie(row["title"], row["year"], row["genre"], row["director"]))

for movie in movies:
    print(f"{movie.title} got a rating of {movie.generate_random_rating()}")

with open("movies.backup", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "year", "genre", "director"])
    for movie in movies:
        writer.writerow(movie.to_dict())