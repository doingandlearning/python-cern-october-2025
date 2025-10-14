s1 = {"apple", "orange", "grapefruit"}
s2 = {"grapefruit", "apple", "lime"}

print("Union")
print(s1 | s2)
print(s1.union(s2))

print("Intersection")
print(s1 & s2)
print(s1.intersection(s2))

print("Difference")
print(s1 - s2)
print(s1.difference(s2))

print("Symmetric difference")
print(s1 ^ s2)
print(s1.symmetric_difference(s2))