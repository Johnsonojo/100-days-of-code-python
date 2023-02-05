def rollercoaster():
    height = int(input("How tall are you in cm? "))
    if height >= 120:
        age = int(input("How old are you? "))
        if age < 12:
            print("Please pay $5.")
        elif age <= 18:
            print("Please pay $7.")
        else:
            print("Please pay $12.")
    else:
        print("Sorry, you have some growing to do first!")


rollercoaster()
