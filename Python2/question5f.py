'''
Create a dictionary using dictionary comprehension
to represent the ASCII values of lowercase alphabets (a-z) where the keys are the
alphabets, and the values are their corresponding ASCII values.

'''


# print(ord("a"))
# print(chr(97))

# dict_alpha = {k:v for k:v in }



dict_alpha = {chr(i):i for i in range(ord('a'), ord('z')+1)}
print(dict_alpha)