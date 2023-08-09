'''
Given two lists of integers, create a list that contains the
product of each element of the first list with the corresponding element in the
second list using list comprehension.
'''


list1 = [1,5,6,7,8]
list2 = [5,6,7,4,2]



result = [x*y for x,y in zip(list1, list2)]
print(result)