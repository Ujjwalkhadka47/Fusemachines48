'''
Write a Python program that takes two integers as input and performs division (num1
/ num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
display appropriate error messages.

'''


try : 
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    result = a/b

except ZeroDivisionError: 
    print("Division by zero is invalid ")
except ValueError: 
    print("Enter a valid Number")