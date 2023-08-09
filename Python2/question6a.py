'''

Write a Python program that takes two integers as input and performs division
(num1 / num2). Handle the ZeroDivisionError and display a custom error message
when the second number is zero.
'''

num1 = int(input("Enter a First Number"))
num2 = int(input("Enter a second Number:"))


try : 
    result = num1/num2 # the portion of code  which generates the error kept in try block 
except ZeroDivisionError : 
    print("Division by Zero is not Allowed")

print(result)