
def fizz_buzz(n):
    for numb in range(n+1):
        if numb % 3 == 0 and numb % 5 == 0:
            print("FizzBuzz")
        elif numb % 3 == 0:
            print("Fizz")
        elif numb % 5 == 0:
            print("Buzz")
        else:
            print(numb)


fizz_buzz(20)


def fizz_buzz(n):
    for numb in range(1, n+1):
        if numb % 15 == 0:
            print("FizzBuzz")
        elif numb % 3 == 0:
            print("Fizz")
        elif numb % 5 == 0:
            print("Buzz")
        else:
            print(numb)


fizz_buzz(100)
