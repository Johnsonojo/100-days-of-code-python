# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason we have leap years is really fascinating, this video does it more justice:


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap_year(2020))
print(is_leap_year(2019))
print(is_leap_year(2009))
print(is_leap_year(2000))
print(is_leap_year(2100))
