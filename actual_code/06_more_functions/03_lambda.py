# lambda function

def square(n):
    print(f"I'm about to calculate a square of {n}")
    return n * n

# DRY -> Don't Repeat Yourself

print(square(3))
print(square(-4))

square = lambda n: n * n
print(square(3))


