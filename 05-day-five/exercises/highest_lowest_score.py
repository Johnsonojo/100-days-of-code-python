# Write a program that calculates the highest score from a list of scores. you must not use the python min() and max() functions.
def highest_score():
    student_scores = input("Enter a list of student scores\n ").split()

    max_score = int(student_scores[0])

    for score in student_scores:
        int_score = int(score)
        if int_score > max_score:
            max_score = int_score

    print(f"The highest score in the class is: {max_score}")

    # 78 65 89 86 55 91 64 89


highest_score()


# Write a program that calculates the lowest score from a list of scores. you must not use the python min() and max() functions.
def lowest_score():
    student_scores = input("Enter a list of student scores\n ").split()

    min_score = int(student_scores[0])

    for score in student_scores:
        int_score = int(score)
        if int_score < min_score:
            min_score = int_score

    print(f"The lowest score in the class is: {min_score}")

    # 78 65 89 86 55 91 64 89


lowest_score()
