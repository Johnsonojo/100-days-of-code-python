# Write a function that takes in a number as an argument and returns a list of prime numbers between 2 and that number
from prime_checker import prime_number_checker

user_input = int(input("Enter the number range: "))


def prime_finder(number):
    prime_number = []
    for i in range(2, number):
        if prime_number_checker(i) == True:
            prime_number.append(i)
    return prime_number


print(prime_finder(number=user_input))
