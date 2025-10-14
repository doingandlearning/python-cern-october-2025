def say_message(message, divider_symbol, divider_length=10, ):
    print(divider_symbol * divider_length)
    print(f"🗣️ {message}")
    print(divider_symbol * divider_length)

say_message("Hello", "*", 20)
say_message("Bonjour", "-*-", 15)
say_message("Gutentag", divider_symbol="%")
print(say_message("Ciao", "-+-"))
