# person1 = {
#     "name": "Patricio",
#     "age": 22,
#     "gender": "Male",
#     "height": 180,
# }
#
# person2 = {
#     "nme": "Ada",
#     "ag": 23,
#     "height": 180,
#     "gender": "Female",
# }
#
# people = [person1, person2]
#
# # for person in people:
# #     print(person["name"])
#
# class Person:
#     """
#     This is a class for a person ...
#     """
#     def __init__(self, name, age, gender, height):
#         if not isinstance(gender, str):
#             raise TypeError("gender must be a string")
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.height = height
#
#     def __str__(self):
#         return f"Person called {self.name}, age: {self.age}, gender: {self.gender}, height: {self.height}"
#
#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age}, gender='{self.gender}', height={self.height})"
#
#     def say_hello(self):
#         print(f"Hi, I'm {self.name}, ca va?")
#
#     def height_in_meters(self):
#         return self.height / 100
#
#     def __len__(self):
#         return len(self.name)
#
#
# person3 = Person("Clement", 24, "Male", 180)
# person4 = Person(name="Camille", age=25, height=180, gender="Male")
# print(person3)  # __str__()  -> __repr__()
# print([person4])  # __repr__()
#
# person3.say_hello()
# person4.say_hello()
# print(person3.height_in_meters())
# print(person3.height)
# print(person4.height_in_meters())
#
#
#
# class Temperature:
#     pass
#
# temp1 = Temperature()
# temp2 = Temperature()
# #
# # temp1 < temp2
#
#
from math import sqrt as square_root
square_root()

def sqrt():
    pass

def print():
    pass