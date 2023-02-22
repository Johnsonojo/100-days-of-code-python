# Write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.

def sum_evens_1():
    sum = 0
    for number in range(0, 101, 2):
        sum += number
    print(sum)


sum_evens_1()


def sum_evens_2():
    sum = 0
    for number in range(1, 101):
        if number % 2 == 0:
            sum += number
    print(sum)


sum_evens_2()
