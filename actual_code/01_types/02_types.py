my_variable = 42

print(my_variable)
print(type(my_variable)) # int

print(my_variable.real)
print(my_variable.imag)

my_variable = 3.14
print(my_variable)
print(type(my_variable)) # float
print(my_variable.is_integer())
my_variable = 3.0
print(my_variable.is_integer())

my_variable = "Cedric"
print(my_variable)
print(type(my_variable)) # str

my_variable = True  # False
print(my_variable)
print(type(my_variable))  # bool
# double underscore -> dunder methods!

my_variable = None  # null, undefined, void
print(my_variable)
print(type(my_variable))
