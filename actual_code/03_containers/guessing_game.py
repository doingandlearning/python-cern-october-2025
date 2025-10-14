import random

MAX_NUMBER_OF_GUESSES = 4
keep_going = True

while True:
    number_to_guess = random.randint(1, 10)
    number_of_guesses = 0
    guessed_correctly = False
    while True:
        user_guess = input(f"Guess a number between 1 and 10 (guess number {number_of_guesses+1}): ").strip()

        while not user_guess.isnumeric():
            print("Not a valid input - try again")
            user_guess = input("Guess a number between 1 and 10: ").strip()
        user_guess = int(user_guess)

        if user_guess ==  999:
            print(f"Ssh! The number was {number_to_guess}.")
            continue

        if not (0 <= user_guess <= 10):
            print("Out of range, try again.")
            continue

        number_of_guesses += 1

        if user_guess == number_to_guess:
            print("Congratulations, you guessed it!")
            guessed_correctly = True
            break
        elif user_guess > number_to_guess:
            print("Too high!")
        elif user_guess < number_to_guess:
            print("Too low!")

        if number_of_guesses == MAX_NUMBER_OF_GUESSES:
            break


    if guessed_correctly:
        print(f"You guessed the number {number_to_guess} in {number_of_guesses} guesses.")
    else:
        print(f"The actual number was {number_to_guess}. Better luck next time.")

    print("Do you want to play again?")
    user_choice = input("Play again? (y/n): ").lower()
    if user_choice == "y":
        continue
    else:
        break