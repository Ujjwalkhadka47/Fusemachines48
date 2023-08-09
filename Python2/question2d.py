'''
Write a Python function filter_long_strings that takes a list of strings as
input and uses the filter function to return a new list containing strings with more
than 5 characters.
'''

def is_long(string) : 
    if len(string)>5:
        return True 
    return False 

def filter_long_strings(list_of_string): 
    """Returns a string which has more than 5 characters 

    Args:
        list_of_string (list): list of strings 

    Returns:
        result(list): string with more than 5 characters 
    """
    result = list(filter(is_long, list_of_string ))
    return result 

print(filter_long_strings(['a', 'Programming', 'framework', 'rice']))