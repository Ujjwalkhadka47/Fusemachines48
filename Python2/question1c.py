'''
Write a Python function calculate_total_cost that calculates the total
cost of items purchased from a store. The function should accept multiple keyword
arguments, where the key is the item name, and the value is the item's price. The
function should return the total cost of all items.

'''



def calculate_total_cost(**kwargs): 
    """Calculates the Total oost of the Items 

    Returns:
        int: total cost 
    """
    total_cost = 0 
    for key, item in kwargs.items(): 
        total_cost += item 
    return total_cost



print(calculate_total_cost(apple=10, mango =20, banana = 30))