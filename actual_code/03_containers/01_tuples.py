empty_tuple = ()  # tuple()

print(empty_tuple)
print(type(empty_tuple))

name_tuple = ("Cedric", "Loic", "Clement", "Darja", "Akrit")

print(name_tuple[3])
print(name_tuple[2:])

print("Kevin" in name_tuple)  # check for membership
print("Cedric" in name_tuple)

if "Kevin" not in name_tuple:
    print("Why did you leave Kevin out? He's sad now.")

for person in name_tuple:
    print(f"{person} works at CERN and is learning Python this week.")

print(name_tuple.count("Cedric"))
print(name_tuple.count("Kevin"))

print(name_tuple.index("Clement"))
print(name_tuple.index("Darja"))

if "Ada" in name_tuple:
    print(name_tuple.index("Ada"))

another_tuple = ("Emanuele", "Camille", name_tuple, ("Patricio", "Livia", "Ada"))
print(another_tuple)
print(another_tuple[3][1])