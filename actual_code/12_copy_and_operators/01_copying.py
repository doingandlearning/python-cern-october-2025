list_a = ["a", "b", "c"]
list_b = list_a.copy()


list_b.append("d")

print(list_a)
print(list_b)

from copy import deepcopy

list_a = [[1,2,3], [4,5,6], [7,8,9]]
list_b = deepcopy(list_a)

list_a[0].append(10)
print(list_a[0])
print(list_b[0])

