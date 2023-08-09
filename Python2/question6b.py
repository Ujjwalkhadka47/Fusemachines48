'''
Implement a program that takes user input for a filename, opens the file in read
mode, and displays its contents. Handle the FileNotFoundError and display an error
message if the file is not found.

'''


file_name = input("Enter File Name:")

try: 
    with open(file_name, 'r'): 
        print("File has been read")
except FileNotFoundError: 
    print("File is not present")