'''
Create a Python function check_leap_year that takes a year as input and uses a
ternary operator to determine if it's a leap year. Return "Leap Year" if it is, otherwise
"Not a Leap Year." (A leap year is divisible by 4, except for years divisible by 100
but not divisible by 400).

'''


def check_leap_year(year): 
    """Checks whether a year is a leap year or not 

    Args:
        year (int): year

    Returns:
        str: Leap Year is its leap year else Not a Leap Year
    """
    return "Leap year" if (year%4==0 and year%100!=0) or (year%400==0) else "Not a Leap Year"


print(check_leap_year(2000))
print(check_leap_year(1900))