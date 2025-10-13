user_color = input("Give me a colour? ").lower().strip()

if user_color == "green":
    print("You must like grass.")
    print("And also leaves in the summer")

elif user_color.startswith("r"):
    print("Colours that begin with r in English are red, rose, ... ")

elif user_color.endswith("n"):
    print("Could be green or marooon or brown")

else:
    print("Invalid colour. Don't understand that command. Fallback.¡")

print("This is a fun activity about colours!")
