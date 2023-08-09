'''
Write a Python function concat_strings that takes any number of strings as
arguments and returns a single concatenated string.
'''


def concat_str(*args): 
    """This Functions uses the join to effectively concatinate the strings passed to the function as arguments 

    Returns:
        str: concatenated string of the strng passed 
    """
    # args are in the form of the list so we can use the join 
    return "".join(args)



print(concat_str("Hello", "Hi", "Hey"))