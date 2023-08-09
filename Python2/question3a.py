'''
Write a Python function called check_odd_even that takes an integer as input and
uses a ternary operator to return "Even" if the number is even, and "Odd" if the
number is odd.

'''


'''
Ternary Operator : value_if_true if condition else value_if_false

'''



def check_odd_even(num): 
    """Determines if the numbers is odd or even 

    Args:
        num (int): number

    Returns:
        str: Even if its even and Odd otherwise 
    """
    return "Even" if num%2==0 else "Odd" 


print(check_odd_even(-2))
print(check_odd_even(55))