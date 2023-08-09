'''
Implement a program that reads a CSV file named "data.csv," containing columns
"Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
individuals who are 18 years or older.
'''


import csv

# Read data from the original CSV file
with open('data.csv', 'r') as input_file:
    reader = csv.DictReader(input_file)
    data = list(reader)
# print(data)

# writing the adult in the adult.csv
with open('adult.csv', 'w') as output_file: 
    fieldnames = ['Name', 'Age']
    writer= csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    for record in data: 
        if int(record['Age'])>=18: 
            writer.writerow(record)