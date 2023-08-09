'''
Create a function convert_to_uppercase that takes a list of strings as input
and uses the map function to return a new list with all the strings converted to
uppercase.

'''

def convert_to_uppercase(strings): 
    """Converts the string in the List to the Uppercase 

    Args:
        strings (list): list of string 

    Returns:
        result(list): list of string with every string in upper case 
    """
    result = list(map(lambda x: x.upper(), strings))
    return result 


print(convert_to_uppercase(['ram', 'jon', 'hari']))