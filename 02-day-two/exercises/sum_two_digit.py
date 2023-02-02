# Write a function that takes a number as an argument and returns the sum of its digits. For example, if the input is 12345, the function should return 15 (which is 1 + 2 + 3 + 4 + 5).

def sum_digits1(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum


print(sum_digits1(12345))


# Write a function that takes a 2 digit number as an argument and returns the sum of its digits. For example, if the input is 12, the function should return 3 (which is 1 + 2).

def sum_digits2():
    entered_number = int(input("Enter a 2-digit number: "))
    if (entered_number < 10 or entered_number > 99):
        print("Invalid number 2-digit number")
    else:
        str_number = str(entered_number)
    result = int(str_number[0]) + int(str_number[1])
    return result


print(sum_digits2())


def sum_digits3():
    entered_number = input("Enter a 2-digit number: ")
    first_digit = int(entered_number[0])
    second_digit = int(entered_number[1])
    result = first_digit + second_digit
    return result


print(sum_digits3())
