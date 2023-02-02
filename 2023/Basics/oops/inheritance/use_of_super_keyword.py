class Employee:
    def __init__(self):
        print("inside employee class")

class Student(Employee):

    def __init__(self):
        super().__init__()
        print("inside the Student class")

obj1 = Student()


