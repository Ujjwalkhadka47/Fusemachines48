'''
Write a Python function square_numbers that takes a list of integers as
input and uses the map function to return a new list containing the square of each
element.

'''

# from typing import List

def square_numbers(nums): 
    """Returns the Square of the List of the Numbers provided to it

    Args:
        nums (list): list of numbers 

    Returns:
        list: list of square of the numbers passed as an arguments 
    """
    '''
    Blue print of the map 
    map(function_to_apply, list_of_inputs)

    '''


    result =list(map(lambda x:x**2, nums)) # map generaters and iterator object so it needs to be converted to the list 
    return result

print(square_numbers([1,2,3]))