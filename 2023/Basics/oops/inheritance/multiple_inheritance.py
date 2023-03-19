# parent class

# class Organization:
#
#     def org_details(self,name,address):
#         print(name,address)
#
# class Employee:
#
#     def emp_details(self,ID,salary):
#         print(ID,salary)
#
# class Person(Organization,Employee):
#
#     def Person_details(self,age):
#         print(age)
#
# abc = Person()
#
# abc.Person_details(23)
# abc.emp_details("2H",2000)



# class Employee:
#
#     def __init__(self,name,age,ID):
#         self.name = name
#         self.age = age
#         self.id = ID
#
#     def show(self):
#         print(self.name,self.age,self.id)
#
# class Student(Employee):
#
#     def __init__(self,name,age):
#         super().__init__(name,age,id)
#     def output(self):
#         print(self.name,self.age)
#
# abc = Student("kiran",20)
#
# abc.show()





# class Student:
#
#     def __init__(self):
#         print("inside the parent class")
#
#
#
# class Child(Student):
#
#     def __init__(self):
#         super().__init__()
#         print("Inside the child class")
#
# a = Child()

#And the 2nd one, where I have used 2 constructors in 2 classes, can you please check if my Code is correct



class Employee:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def show_details(self):
        print(self.name)
        print(self.address)

class Organization(Employee):
    def __init__(self,name, address, ID):
        self.ID=ID
        Employee.__init__(self, name, address)
    def show_details_1(self):
        print(self.name)
        print(self.address)
        print(self.ID)

Emp = Employee("Name of Employee: Rajesh","Location of Employee: Mumbai" '\n')
Emp.show_details()
Org = Organization("Name of Employee: Pratik","Location: Banalore","Employee Code: \Emp09")
Org.show_details_1()














