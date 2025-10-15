with open("movies.csv") as file:
    file.readline()
    line = file.readline()
    while line:
        print(line.split(","))
        line = file.readline()

import csv

with open("movies.csv") as file:
    reader = csv.reader(file)
    next(reader) # skips a line (for the header)
    for title, release_year, genre, director in reader:
        print(f"{title} was released in {release_year} in {genre} genre and director {director}.")

with open("movies.csv") as file:
    fieldnames = ['movie', "year", "genre", "director"]
    reader = csv.DictReader(file, fieldnames=fieldnames)

    for row in reader:
        print(f"{row["movie"]} was released in {row["year"]}")