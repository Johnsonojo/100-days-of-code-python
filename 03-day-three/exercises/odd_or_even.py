# Write a program that works out whether if a given number is an odd or even number.

def odd_or_even1(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


print(odd_or_even1(5))


def odd_or_even2():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


odd_or_even2()
