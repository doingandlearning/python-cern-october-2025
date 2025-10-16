def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, int | float):
        raise ValueError("Argument must be int or float")

    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("Argument must not be bool")

    return a + b

class MathFunctions:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, int | float):
            raise ValueError("Argument must be int or float")

        if isinstance(self.a, bool) or isinstance(self.b, bool):
            raise ValueError("Argument must not be bool")

        return self.a + self.b