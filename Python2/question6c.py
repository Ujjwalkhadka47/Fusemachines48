'''
Write a Python program that takes a user input and converts it to an integer. Handle
the ValueError and display a custom error message when the input cannot be
converted to an integer.

'''


# print(int("Test")) # Raises ValueError


try: 
    usr_input = int(input("Enter a number"))

except ValueError: 
    print("Not valid Number")