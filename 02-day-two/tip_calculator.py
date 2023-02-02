def tip_calculator():
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill? $"))
    tip_percentage = int(
        input("What percentage tip would you like to give? 10, 12, or 15? "))
    number_of_persons = int(input("How many persons to split the bill? "))
    total_tip_amount = (total_bill * (tip_percentage / 100))
    each_person_pays = (total_bill + total_tip_amount) / number_of_persons
    print(f"Each person should pay: ${each_person_pays:.2f}")


tip_calculator()
