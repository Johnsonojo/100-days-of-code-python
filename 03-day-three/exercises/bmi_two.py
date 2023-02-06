# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

def bmi_calculator2():
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))

    bmi = weight / (height * height)
    result = int(bmi)
    print(result)

    if result < 18.5:
        return f"Your BMI is {result}, you are underweight."
    elif result < 25:
        return f"Your BMI is {result}, you have a normal weight."
    elif result < 30:
        return f"Your BMI is {result}, you are slightly overweight."
    elif result < 35:
        return f"Your BMI is {result}, you are obese."
    else:
        return f"Your BMI is {result}, you are clinically obese."


print(bmi_calculator2())
