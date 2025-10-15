"""
This is a utility module
- what's in here?
- what you need to know
- 3rd party libraries -> you need to have numpy installed ...
"""

def printer(some_object):
    print("I am the printer function")
    print(some_object)
    print("How did I do?")

class Shape:
    def __init__(self, type):
        self.type = type

default_shape = Shape("circle")

def main():
    print("I am the utils module")
    print(f"My name is {__name__}")

if __name__ == "__main__":
    main()