import os
import random

from hangman_art import logo, stages
from hangman_words import word_list


def hangman():
    random_word = random.choice(word_list)
    word_length = len(random_word)

    end_of_game = False
    lives = 6

    print(logo)
    print(random_word)

    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        user_guessed = input("Guess a letter: ").lower()

        # Clearing the Screen
        os.system('cls')
        if user_guessed == "":
            print("You entered an empty character.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        for position in range(word_length):
            letter = random_word[position]
            if letter == user_guessed:
                display[position] = letter
        if user_guessed in display:
            print(f"You've already guessed {user_guessed}")

        if user_guessed not in random_word:
            print(
                f"You guessed {user_guessed}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])


hangman()
