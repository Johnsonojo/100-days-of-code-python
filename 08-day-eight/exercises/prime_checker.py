# You are painting a wall.
# Prime numbers are numbers that can only be divisible by itself and one.
# You need to write a function that checks whether a number passed into it is a prime number or not.

# user_input = int(input("Enter a number: "))


# def prime_number_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It;s not a prime number")


# prime_number_checker(number=user_input)


def prime_number_checker(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True


prime_number_checker(97)
