programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Printing the value of a key
print(programming_dictionary["Bug"])

# adding items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Editing the value of a key
programming_dictionary["Bug"] = "A moth in your computer."

print(programming_dictionary)

for key in programming_dictionary:
    print({key: programming_dictionary[key]})
print(programming_dictionary[key])

# Nesting a Dictionary inside a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
# Accessing nested value
print(travel_log["France"]["cities_visited"][1])

# Nesting a Dictionary inside a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]
