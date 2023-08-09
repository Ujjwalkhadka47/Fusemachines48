
'''
Write a Python program that takes user input for age. Create a custom exception
InvalidAgeError to handle cases where the age is below 0 or above 120.
○
●
Hint: Create new class InvalidAgeError that inherits Exception class

'''


class InvalidAgeError(Exception): 
    """Raised When invalid age is used"""
    pass 


age = int(input("Enter your age: "))
if age < 0 or age > 120: