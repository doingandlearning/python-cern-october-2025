import csv

# with open("movies.csv", mode="a", newline="") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Superman", 2025, "Sci-Fi", "James Gunn"])

with open('movies.csv', 'a', newline='') as csvfile:
    fieldnames = ['movie', 'year', 'genre', 'director']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    movie = {
        'movie': 'KPop Demon Hunters',
        'year': 2025,
        'genre': 'Animation',
        'director': 'Maggie Kang',
    }

    writer.writerow(movie)