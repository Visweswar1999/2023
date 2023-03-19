
# single inheritance
#
# parent class
#
# class Organization:
#     def org_details(self,name,number):
#         self.name = name
#         self.number = number
#     def org_show(self):
#         print("organization name is",self.name,"organization number is",self.number)
# #parent class
# class Employee():
#     def Emp_details(self,name,id):
#         self.name = name
#         self.id = id
#     def emp_show(self):
#         print("employee name is ",self.name,"employee id is",self.id)
#
# #child class
# class Kiran(Organization,Employee):
#     def kiran_class(self):
#         print("inside the kiran class")
#
# object1 = Kiran()
# object1.org_details("dell","2345")
# object1.Emp_details("ramesh","876")
# object1.emp_show()
# object1.org_show()
#
#
#
#
# single inheritance
#
# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name,self.age)
# class Student:
#     def student_class(self):
#         print("inside student class")
#
# class Details(Employee,Student):
#
#     def details1(self):
#         print("inside the details class")
#         print(self.name)
#
# object1 = Details("kiran",23)
# object1.student_class()
# object1.show()
# object1.details1()
#
# '''
# class Employee:
#     def __init__(self,name,number):
#         self.name = name
#         self.number = number
#         self.another_class = self.Organization()
#     def output(self):
#         print(self.name,self.number)
#
#     class Organization:
#         def inside_org(self):
#             print("inside the origanization class")
#
#         def senond_one(self):
#             print("second function")
#             print(Employee)
#
# obj1 = Employee(number=23,name="kiran") '''



# class Employee:
#
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#
#     def show(self):
#         print(self.name,self.id)
#
# class Organization(Employee):
#
#     def __init__(self,name,address):
#         Employee.__init__(self,name,id)
#         self.name = name
#         self.address = address
#
#     def details_organization(self):
#         print(self.name,self.address)
#
# child = Organization


# class BaseClass:
#     body of the base class
#
# class Derivedclass(BaseClass):
#     Body of the derived class




















































