'''
Write a function find_bigger_number that takes three integers as input and uses a
ternary operator to return the larger number. If all numbers are equal, return
"Equal."

'''

def find_bigger_number(num1, num2, num3):
    """find the biggest among three numbers 

    Args:
        num1 (int): number
        num2 (int): number
        num3 (int): number

    Returns:
        str or num: high number and incase if all equal returns Equal 
    """

    result = num1 if num1 >= num2 and num1 >= num3 else num2 if num2 >= num3 else num3
    return result if result != num1 or result != num2 or result != num3 else "Equal."


print(find_bigger_number(1,6,7))
print(find_bigger_number(4,4,4))