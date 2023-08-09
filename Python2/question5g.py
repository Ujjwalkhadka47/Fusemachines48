'''
Given a list of numbers, create a set using set
comprehension that contains only unique even numbers.

'''


list1 = [13,41,13, 22,22, 15,15,17, 24 , 16,16]



set_list = {x for x in list1 if x%2==0}



print(set_list)