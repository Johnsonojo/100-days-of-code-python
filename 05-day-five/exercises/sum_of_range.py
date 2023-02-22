# Write a program that sums all the numbers withing a range.


def sum_of_range(num_range):
    sum = 0
    for num in range(0, num_range+1):
        sum += num

    print(sum)


sum_of_range(100000)


def sum_numbers(n):
    sum = n*(n+1)/2
    print(int(sum))


sum_numbers(100000)
