'''
Write a Python function calculate_factorial that takes an integer as input
and uses the reduce function to return the factorial of that number.
'''


'''
reduce -> used to perform some computations of a list 
eg. 

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24

'''

from functools import reduce 



def calculate_factorial(num): 
    """Calculates Factorial of a numbers

    Args:
        num (int): numbers

    Returns:
        result(int): factorial of a number
    """
    result = reduce(lambda x,y: x*y, list(range(1,num+1)))  
    return result 

print(calculate_factorial(9))