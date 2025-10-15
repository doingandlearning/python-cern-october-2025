file = open("test.txt", mode="w", encoding="utf-8")

file.close()


# Context handler  (try-with-resources)
with open("test1.txt", mode="w", encoding="utf-8") as other_file:
    other_file.write("Hello\n")
    other_file.write("Hello\n")