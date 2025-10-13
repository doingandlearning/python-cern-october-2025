user_color = input("What is your favorite color? ")


match user_color:
    case "red":
        print("The color is red!")
    case "green":
        print("The color is green!")
    case "yellow" | "blue":
        print("The color is yellow!")
    case _:
        print("The color is unknown!")

if user_color == "red":
    print("The color is red!")
elif user_color == "green":
    print("The color is green!")
elif user_color == "yellow":
    print("The color is yellow!")
elif user_color == "blue" or user_color == "pink":
    print("The color is blue or pink!")
elif user_color.startswith("p") and not (user_color.endswith("e") or user_color.endswith("b")):
    print("Is the colour purple?")
else:
    print("The color is unknown!")