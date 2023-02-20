import random


def rock_paper_scissors():
    choices = ["Rock", "Paper", "Scissors"]
    user_choice_number = int(input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
    if (user_choice_number > 2):
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
        return rock_paper_scissors()

    user_choice = choices[user_choice_number]
    computer_choice_number = random.randint(0, 2)
    computer_choice = choices[computer_choice_number]

    if (user_choice == computer_choice):
        return ("It's a draw!")
    elif (user_choice == "Rock"):
        if (computer_choice == "Scissors"):
            return ("Rock smashes scissors! You Win!")
        else:
            return ("Paper covers rock! You loss!")
    elif (user_choice == "Paper"):
        if (computer_choice == "Rock"):
            return ("Paper covers rock! You Win!")
        else:
            return ("Scissors cuts paper! You loss!")
    elif (user_choice == "Scissors"):
        if (computer_choice == "Paper"):
            return ("Scissors cuts paper! You Win!")
        else:
            return ("Rock smashes scissors! You loss!")


print(rock_paper_scissors())
