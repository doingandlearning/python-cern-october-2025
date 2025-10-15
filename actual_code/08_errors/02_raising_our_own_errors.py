import traceback

class InvalidColorError(Exception):
    def __init__(self, color, code = 404):
        msg = f"This was an invalid color (not red, green or blue) - {color}"
        super().__init__(msg)
        self.code = code

class CernError(Exception):
    pass

def get_valid_value():
    try:
        input_from_user = input("Give me a colour: ")

        if input_from_user not in ['red', 'green', 'blue']:
            raise CernError("Not an acceptable colour", "418")
    except ValueError as e:
        print("Valid colours are red, green and blue")
        print(e)

try:
    get_valid_value()
except InvalidColorError as e:
    print(e)
except Exception as e:
    print(e)

print("Still going!!!")