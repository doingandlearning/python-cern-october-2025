class Quantity:
    def __init__(self, value):
        self.value = value

    def equal_to(self, other):
        if not isinstance(other, Quantity):
            return False
        return self.value == other.value

    def __eq__(self, other):
        if not isinstance(other, Quantity):
            return False
        return self.value == other.value

    def __add__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Can only add Quantity to Quantity")
        return Quantity(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Can only subtract Quantity to Quantity")
        if self.value < other.value:
            raise ValueError("Would result in a negative value")
        return Quantity(self.value - other.value)

    def __repr__(self):
        return f"Quantity({self.value})"

    def __lt__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Can only add Quantity to Quantity")
        return self.value < other.value



q1 = Quantity(20)
q2 = Quantity(10)

print(q1.equal_to(q2))
print(q1 == q2)

# q3 = q2.add(q1)
q3 = q1 + q2
print(q3.value)

q4 = q1 - q2
print(q4.value)

quantity_list = [q1, q2, q3, q4]
print(quantity_list)
quantity_list.sort()
print(quantity_list)
print(q1)
print([quantity > q1   for quantity in quantity_list])

total = Quantity(0)
for quantity in quantity_list:
    total += quantity
print(total)