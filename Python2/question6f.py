'''
Implement a program that reads user input for a password. Create a custom
exception WeakPasswordError to handle cases where the password is shorter
than 8 characters.
○
Hint: WeakPasswordError that inherits Exception class

'''


class WeakPasswordError(Exception): 
    """Raised when weakpassword is used"""
    pass 