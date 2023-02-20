# Write a program that calculates the average student height from a list of heights. You must not use the python sum() and len() functions.

def average_height_calculator():
    student_heights = input("input a list of student heights\n ").split()
    sum_of_heights = 0
    number_of_students = 0

    for height in student_heights:
        sum_of_heights += int(height)
        number_of_students += 1
    average_height = round(sum_of_heights/number_of_students)
    print(f"The average student height is {average_height}")


average_height_calculator()
