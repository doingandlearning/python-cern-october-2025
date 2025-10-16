def add(a, b, c=0, d=0):
    return a + b + c + d

def add(name, *numbers):
    total = 0
    for number in numbers:
        total += number
    return f"{name} wanted to know the sum of {numbers} it is {total}"

print(add("Kevin", 1, 2))
print(add("Loic", 1,2,3))
print(add("Ada", 1,2,3,4))
print(add("Livia"))
print(add("Patricio", 1))

list_countries = ["Switzerland", "UK", "France", "Germany", "Romania", "Italy"]
first_country, second_country, *_ = list_countries

print(first_country)
print(second_country)
