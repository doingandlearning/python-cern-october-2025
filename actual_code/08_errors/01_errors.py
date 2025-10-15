

def get_number_from_user():
    number = None
    while number is None:
        try:
            number = 100 / int(input("Enter a number: "))
        except ValueError as e:
            print("That was not a valid number.")
            print(e)
        except ZeroDivisionError:
            print("You can't divide by zero.")
            number = None
        except Exception as e:
            print("Something unexpected went wrong.")
            print(e)
        else:  # on_success
            print("You have entered a number.")
        finally:
            print("Thank you for using this program.")
    return  number

number = get_number_from_user()

print(number)
print("The program keeps going!!")