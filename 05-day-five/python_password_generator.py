import random


def password_generator():
    password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%(^)&*?"
    print("Welcome to the PyPassword generator!")

    number_of_letters = int(
        input("How many letters would you like in your password?\n"))
    number_of_symbols = int(input("How many symbols would you like?\n"))
    number_of_digits = int(input("How many numbers would you like?\n"))
    password_length = number_of_letters+number_of_symbols+number_of_digits

    generated_password = ''
    start_index = 1

    while start_index <= password_length:
        random_index = random.randint(0, len(password_characters))
        random_character = password_characters[random_index]
        generated_password += random_character
        start_index += 1
    print(generated_password)


password_generator()
