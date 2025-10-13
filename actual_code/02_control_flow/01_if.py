from http.cookiejar import user_domain_match

user_color = input("Give me a colour? ").lower().strip()

if user_color == "green":
    print("You must like grass.")
    print("And also leaves in the summer")


if user_color.startswith("r"): print("hello")