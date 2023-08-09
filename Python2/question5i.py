'''
Given two strings, write a Python program to create a set
using set comprehension that contains all the characters that are common in both
strings.

'''

string_1 = "test"
string_2 = "talk"

common_chars = {char for char in string_1 if char in string_2}

print(common_chars)