'''
Given a dictionary with students' names as keys and
their respective scores as values, create a new dictionary that contains only the
students who scored more than 80 using dictionary comprehension.

'''

keys = ["Jon", "Sam", "Hari"]
values = [120, 40,80]



dict_result = {k:v for k,v in zip(keys,values) if v>40 }
print(dict_result)