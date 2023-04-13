from random import randint

from art import logo


def guess_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    max_number = 100
    random_number = randint(1, max_number)
    difficulty = {"easy": 10, "hard": 5}
    difficulty_chosen = input(
        "Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_chosen not in difficulty:
        print("invalid input")
        return
    attempts_remaining = difficulty[difficulty_chosen]

    while attempts_remaining != 0:
        print(
            f"You have {attempts_remaining} attempts remaining to guess the number")
        user_choice = int(input("Make a guess: "))
        attempts_remaining -= 1
        if user_choice > random_number:
            print("Too high.")
        elif user_choice < random_number:
            print("Too low.")
        else:
            print(f"You got it! The answer was {random_number}")
            return

    if attempts_remaining == 0:
        print(
            f"Sorry, you ran out of attempts. The answer was {random_number}.")


guess_number()
