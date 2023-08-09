'''
Create a Python program that manages student records. The program should have the following functionalities:


-Create a function that can add new students to the records with their student_id,
name, age, and grade. The records should be saved to “json” file and each time
new record is added, it should be saved to same “json” file


-Allow searching for a student by student_id or name. The data should return age
and grade from the saved file.


-Allow updating a student's information by using student_id or name(age or grade)
Ensure to follow PEP8 Coding Guidelines for following criterias:

- Proper Indentation
- Maximum Line Length
- Prescriptive Naming conventions (Package and Module Names, Class Names,
- Exception Names, Global Variable Names, Function and Variable Names, Method
- Names and Instance Variables, Constants)
- Source File Encoding while accessing the JSON file
- Add NumPy Docstring to each function


'''

import json

class StudentRecordsManager:
    """Class to manage student records."""
    
    def __init__(self, filename='student_records.json'):
        """
        Initialize the StudentRecordsManager.

        Args:
            filename (str): Name of the JSON file to save records to.
        """
        self.filename = filename
        self.records = self._load_records()

    def _load_records(self):
        """
        Load records from the JSON file.

        Returns:
            dict: Loaded records from the JSON file.
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_records(self):
        """
        Save records to the JSON file.
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.records, file, indent=4)

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student record.

        Args:
            student_id (str): Student ID.
            name (str): Student's name.
            age (int): Student's age.
            grade (str): Student's grade.
        """
        self.records[student_id] = {
            'name': name,
            'age': age,
            'grade': grade
        }
        self._save_records()

    def search_student(self, query):
        """
        Search for a student by student_id or name.

        Args:
            query (str): Student ID or name to search for.

        Returns:
            dict: Student information (age and grade).
        """
        for student_id, info in self.records.items():
            if query.lower() in (student_id.lower(), info['name'].lower()):
                return {'age': info['age'], 'grade': info['grade']}
        return None

    def update_student_info(self, query, field, new_value):
        """
        Update a student's information.

        Args:
            query (str): Student ID or name to update.
            field (str): Field to update ('age' or 'grade').
            new_value (str): New value for the field.
        """
        for student_id, info in self.records.items():
            if query.lower() in (student_id.lower(), info['name'].lower()):
                info[field] = new_value
                self._save_records()
                break


def main():
    records_manager = StudentRecordsManager()

    while True:
        print("\n1. Add Student\n2. Search Student\n3. Update Student Info\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            records_manager.add_student(student_id, name, age, grade)
            print("Student record added successfully!")

        elif choice == '2':
            query = input("Enter student ID or name to search: ")
            student_info = records_manager.search_student(query)
            if student_info:
                print(f"Age: {student_info['age']}, Grade: {student_info['grade']}")
            else:
                print("Student not found.")

        elif choice == '3':
            query = input("Enter student ID or name to update: ")
            field = input("Enter field to update (age/grade): ")
            new_value = input("Enter new value: ")
            records_manager.update_student_info(query, field, new_value)
            print("Student information updated successfully!")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()