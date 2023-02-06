# Your are going to write a program that tests the compatibility between two people. We're going to use the super scientific method recommended by BuzzFeed. to work out the love score between two people: take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.


def love_calculator():
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? ").lower()
    name2 = input("What is their name? ").lower()

    combined_names = name1 + name2

    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    true = t + r + u + e

    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    love = l + o + v + e

    love_score = int(str(true) + str(love))
    if love_score < 10 or love_score > 90:
        print(
            f"Your score is {love_score}, you go together like coke and mentos.")
    elif love_score >= 40 and love_score <= 50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")


love_calculator()
