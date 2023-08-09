'''
Create a Python class to represent a University. The university should have
attributes like name, location, and a list of departments. Implement encapsulation to
protect the internal data of the University class. Create a Department class that
inherits from the University class. The Department class should have attributes like
department name, head of the department, and a list of courses offered. Implement
polymorphism by defining a common method for both the University and
Department classes to display their details.
'''
class University: 
    def __init__(self, name, location = None): 
        self.__name = name 
        self.__location = location
        self.__departments= []  

    def add_department(self, department):
        self.__departments.append(department)

    def display_details(self):
        print(f"University: {self.__name}")
        print(f"Location: {self.__location}")
        print("Departments:")
        for department in self.__departments:
            print("Print the Department Details ")
class Department(University): 
    def __init__(self, name , hod, courses): 
        super.__init__(name) 
        self.__hod = hod 
        self.__courses = courses
    def add_course(self, course):
        self.__courses.append(course)

    def display_details(self):
        print(f"Department: {self.get_name()}")
        print(f"Head of Department: {self.__hod}")
        print("Courses offered:")
        for course in self.__courses:
            print(f"- {course}")


university = University("Tribhuvan University", "Lalitpur")
university.display_details()