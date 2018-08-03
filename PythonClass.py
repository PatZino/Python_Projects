class Employee:
    """Common base class for all employee"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


"""This would create first object of employee class"""
emp1 = Employee("Zara", 2000)
"""This would create first object of employee class"""
emp2 = Employee("Pat", 3500)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

print("_"*60)


class Student:
    numberOfStudent = 0

    def __init__(self, matricNumber, sex, degree, name):
        self.matricNumber = matricNumber
        self.sex = sex
        self.degree = degree
        self.name = name
        Student.numberOfStudent += 1

    def display_total_student(self):
        print("Total number of student = %d" % Student.numberOfStudent)

    def display_student_details(self):
        print("name: ", self.name, ", matric number: ", self.matricNumber, "sex: ", self.sex, "degree: ", self.degree)


student1 = Student(170084567, "female", "postgraduate", "Kate")
student2 = Student(170084577, "male", "postgraduate", "Henry")
student3 = Student(170084597, "male", "postgraduate", "Kayode")
student4 = Student(170084527, "female", "postgraduate", "Susan")
student5 = Student(170084507, "male", "postgraduate", "Matthew")
student6 = Student(170084537, "female", "postgraduate", "Bola")

student1.display_student_details()
student2.display_student_details()
student3.display_student_details()
student4.display_student_details()
student5.display_student_details()
student6.display_student_details()

print("Total number of student = %d" % Student.numberOfStudent)

