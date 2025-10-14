cities = {"Paris", "Rome", "Geneva", "Oslo", "London", "Rome", "Paris", "Paris", "London", "Belfast"}

print(cities)
print(type(cities))

# cities[0] -> can't do this!

print("Paris" in cities)

for city in cities:
    print(city)

cities.remove("Paris")
print(cities)

cities.add("Paris")
cities.add("Belgrade")
print(cities)
cities.add("Belgrade")
print(cities)

if "Budapest" in cities:
    cities.remove("Budapest")

user_list = ["rose", "tulip", "tulip", "rose", "daffodil"]


cities.add(frozenset({1,2,3,4}))

unique_list = []

for flower in user_list:
    if flower not in unique_list:
        unique_list.append(flower)

# user_input = input("Give me a flower: ")
#
# while user_input != "quit":
#     user_list.append(user_input)
#     user_input = input("Give me a flower: ")

