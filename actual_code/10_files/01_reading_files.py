file = None
try:
    file = open("test.txt", mode="r", encoding="utf-8")

    contents = file.read().split("\n")   # read the whole file as a string!
    print(contents)
    print(type(contents))

    file.seek(0)
    lines = [line.strip() for line in file.readlines()]
    print(lines)
    print(type(lines))

    if "cheese" in lines:
        print("Yummy!")

    file.seek(0)

    def get_batch_size(file, start=0, batch_size=2):
        file.seek(0)
        for _ in range(start * batch_size):
            file.readline()

        output = []
        for _ in range(batch_size):
            output.append(file.readline())

        return output



    batch_1 = get_batch_size(file)
    batch_2 = get_batch_size(file, start=2)
    batch_3 = get_batch_size(file, start=4)

    print(batch_1)
    print(batch_2)
    print(batch_3)

    # lines 3 and 4

    # while line:
    #     print(line.strip())
    #     line = file.readline()

except FileNotFoundError:
    print("File not found")
finally:
    if file is not None:
        file.close()