""" 
 Write a Python function that takes an arbitrary number of positional
arguments and returns the sum of all the numbers. Test your function with various
input cases.

"""



def func1(*args): 
    """SUms all the argument passed to the function 

    Returns:
        sum: sum of the arguments passed tot the args 
    """
    sum = 0 
    for item in args: 
        sum+=item 
    return sum 





print(func1(1,4,5,6,7,8))