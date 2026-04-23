class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_basic_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_details(self):
        print("********Student Details***********")
        self.display_basic_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

class Professor(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        print("************Professor Details*************")
        self.display_basic_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

student1 = Student("Likhitha", 21, "321136412057", "ECE")
professor1 = Professor("Bhanu Teja", 26, "PFS-VSP-001", "Python-Department")

student1.display_details()
professor1.display_details()
