empty_dictionary = {}
print(empty_dictionary)
print(type(empty_dictionary))

cities = {
    "France": ["Paris", "Lyon", "Saint Genis"],
    "Poland": "Krakow",
    "Italy": "Rome",
    "Romania": "Bucharest"
}

print(cities["France"])
print(cities.get("France", "I don't know that."))

# table = {
#    "Employee1": {"name": "Kevin", "hours_worked": 2, "rate_of_pay": 5},
#    "Employee2": {
#         "name": "Kevin",
#         "hours_worked": 2, },
#
# }

cities["Germany"] = "berlin"
cities.update({"Germany": "Berlin"})
from pprint import pprint
pprint(cities)


pprint(list(cities.keys()))
print(list(cities.values()))
print(list(cities.items()))

print("Germany" in cities)
print("Berlin" in cities.values())

for country, city in cities.items():
    print(f"The capital of {country} is {city}")
