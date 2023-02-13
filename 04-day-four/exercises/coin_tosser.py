# Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random


def coin_toss():
    random_toss = random.randint(0, 1)
    print(random_toss)
    if random_toss == 1:
        print("Heads")
    else:
        print("Tails")


coin_toss()
