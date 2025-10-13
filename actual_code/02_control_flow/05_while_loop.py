user_name = ""
while not user_name:
    user_name = input("What is your name? ")

user_input = input("What is your age? ")

while not user_input.isdigit():  # defensive programming!
    print("Please enter a positive number")
    user_input = input("What is your age? ")

# while not user_input.isdigit() or not (user_input[0] == "-" and  user_input[1:].isdigit()):
#     print("Please enter a valid number")
#     user_input = input("What is your age? ")

user_input = int(user_input)

while user_input > 100 or user_input < 0:
    print("Please enter a number between 0 and 100")
    user_input = input("What is your age? ")



"""
False:
- 0
- None
- ""



"""