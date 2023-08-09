'''
Given two lists - one containing keys and another
containing values, create a dictionary using dictionary comprehension.

'''

keys = ["apple", "mango", "tomato"]
values = [120, 100,80]


dict_result = {k:v for k,v in zip(keys,values)}
print(dict_result)