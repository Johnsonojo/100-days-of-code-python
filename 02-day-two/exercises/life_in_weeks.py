# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:


def life_in_weeks():
    current_age = input("What is your current age? ")
    final_age = 120

    remaining_years = final_age - int(current_age)
    days_remaining = remaining_years * 365
    weeks_remaining = remaining_years * 52
    months_remaining = remaining_years * 12

    result = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left."
    return result


print(life_in_weeks())
