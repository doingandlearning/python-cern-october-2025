name= "Darja"
print(name)
name = 'Loic\n'
print(name)
# triple quotes ->
name = """My string
            can be 
            on multiple
            lines.
"""
#       01234567
name = "Emanuele"
print(name)
print(name[0])
print(name[0:3])
print(name[:3])
print(name[3:])
print(name[0:5:2])

print("Hello " + name + ", how are you?")
print("This course is " + str(4) + " days long.")
print(f"Hello {name}, how are you?") # interpolation
print(f"This course is {4} days long.")
print(f"1 + 1 = {1 + 1}")
print(f"Hello {name.upper()}, how are you?")
print(name)

print(name.find("ele"))
print(name.find("Kevin"))

print(name.replace("e", "q"))

user_color = input("Give me a colour? ").lower().strip()
print(user_color)
print(user_color == "green")



