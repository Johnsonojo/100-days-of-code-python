def rollercoaster2():
    height = int(input("How tall are you in cm? "))
    bill = 0
    if height >= 120:
        age = int(input("How old are you? "))
        if age < 12:
            bill = 5
            print("Child tickets are $5.")
        elif age <= 18:
            bill = 7
            print("Youth tickets are $7.")
        elif age >= 45 and age <= 55:
            print("Everything is going to be ok. Have a free ride on us!")
        else:
            bill = 12
            print("Adult tickets are $12.")
        wants_pic = input("Do you want a picture? Y or N. ")
        if wants_pic == "Y":
            bill += 3
        print(f"Your final bill is ${bill}.")
    else:
        print("Sorry, you have some growing to do first!")


rollercoaster2()
