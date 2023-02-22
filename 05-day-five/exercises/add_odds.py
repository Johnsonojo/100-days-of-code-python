# Write a program that calculates the sum of all the odd numbers from 1 to 100, including 1 and 100.

def add_odds_1():
    sum = 0
    for number in range(1, 101, 2):
        sum += number
    print(sum)


add_odds_1()


def add_odds_2():
    sum = 0
    for number in range(1, 101):
        if number % 2 != 0:
            sum += number
    print(sum)


add_odds_2()
