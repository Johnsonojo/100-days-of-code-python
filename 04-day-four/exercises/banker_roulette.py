# Write a program which will select a random name from a list of names. The person selected will have tp pay for everybody's food bill.

import random


def bank_roulette1():
    name_string = input(
        "Enter the names of each banker separated by comma. \n")

    names_list = name_string.split(',')
    names_list_length = len(names_list)

    random_index = random.randint(0, names_list_length-1)
    bill_payer = names_list[random_index]

    result = print(f"{bill_payer} is going to buy the meal today!")
    return result


bank_roulette1()


# Using the choices method
def bank_roulette2():
    name_string = input(
        "Enter the names of each banker separated by comma. \n")

    names_list = name_string.split(',')

    bill_payer = random.choice(names_list)

    result = print(f"{bill_payer} is going to buy the meal today!")
    return result


bank_roulette2()
