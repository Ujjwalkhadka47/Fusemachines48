'''
Given a list of strings, create a new list that contains only the
strings with more than 5 characters using list comprehension.

'''



'''
list comprehension 

[expression for item in iterable if condition == True]

'''
eg_string = ["Programming", "Bat", "Batman", "Superman"]

final_str = [item for item in eg_string if len(item)>5]
print(final_str)