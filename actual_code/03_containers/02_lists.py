empty_list = []  # list()
print(empty_list)
print(type(empty_list))

empty_tuple = tuple(empty_list)

beatles_list = ["John", "Paul", "George", "Ringo"]
print(beatles_list[1])
print(len(beatles_list))

beatles_list.append("Ada")
print(beatles_list)

beatles_list.extend(("Clement", "Darja", "John"))
print(beatles_list)

beatles_list.insert(2, "Patricio")
print(beatles_list)

while "John" in beatles_list:
    beatles_list.remove("John")

print(beatles_list)

band_member = beatles_list.pop()
print(band_member)
print(beatles_list)

for member in beatles_list:
    print(f"{member} is in the band.")

del beatles_list[1]
print(beatles_list)

# beatles_list.sort() -> changes the original list
sorted_list = sorted(beatles_list, reverse=True, key=lambda member: len(member))
print(beatles_list)
print(sorted_list)


