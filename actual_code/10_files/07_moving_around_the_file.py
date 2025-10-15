with open("movies.csv", "r", newline="") as file:
    file.seek(10)

    print(file.tell())

    file.seek(file.tell() + 10)

    print(file.tell())

    print(file.read())

