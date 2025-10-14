number_of_tries = 0
player_name = "Kevin"

def handle_player_name():
    player_name = "Bob"
    # number_of_tries = globals()["number_of_tries"]
    global number_of_tries
    number_of_tries += 1
    player_age = 42
    print(player_name)
    print(f"Number of tries inside the function: {number_of_tries}")

handle_player_name()
print(player_name)
# print(player_age)
print(f"Number of tries outside the function: {number_of_tries}")