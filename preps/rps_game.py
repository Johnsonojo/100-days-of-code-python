import random


def get_choice():
    options = ["rock", "paper", "scissors"]
    player_choice = random.choice(options)
    # player_choice = input("Choose rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    player_choices = {"player": player_choice, "computer": computer_choice}
    return player_choices


def check_winner(player, computer):
    print(f"Player chose {player} and computer chose {computer}.")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! Player wins"
        else:
            return "Paper covers rock! Computer wins"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! Player wins"
        else:
            return "Scissors cuts paper! Computer wins"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! Player wins"
        else:
            return "Rock smashes scissors! Computer wins"


choices = get_choice()

winner = check_winner(choices["player"], choices["computer"])

print(winner)
