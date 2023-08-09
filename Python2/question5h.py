'''
Given a list of words, write a Python program to create a set
using set comprehension that contains all the unique characters present in the
words.

'''

list1 = ["Hello", "Hi", "Programming"]



set_list = {char for word in list1 for char in word} 
print(set_list)