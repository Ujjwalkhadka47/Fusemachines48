'''
Implement a function called concatenate_strings that takes a list of
strings as input and uses the reduce function to return a single string containing the
concatenation of all the elements.

'''
from functools import reduce 




def concatenate_string(l_string): 
    """COncatenates the String from the list 

    Args:
        l_string (list): list of string

    Returns:
        result(str): concatenated strong from the list of the string 
    """
    result = reduce(lambda x, y: x+y, l_string)

    return result


print(concatenate_string(["hello","ram", 'John',"!"]))