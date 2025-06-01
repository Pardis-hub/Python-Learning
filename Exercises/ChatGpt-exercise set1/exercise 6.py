"""
Leap Year Checker
Write a function to check whether a given year is a leap year. A year is a leap year if it is divisible by 4
but not by 100, except if it is also divisible by 400.
"""

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
        return 'Leap Year'
    else:
        return 'Not Leap Year'