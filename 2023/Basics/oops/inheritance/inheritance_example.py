# single
# multiple
#multi-level

'''
Single --> it will acquare properties of one parent -->

multiple --> it will acquare the two properties of two parent classes --> A ,B ,C(A,B)

multi-level --> -->
'''

# class Organization:
#     def __init__(self,name,adress):
#         self.name = name
#         self.address = adress
#     def show_details(self):
#         print(self.name,self.address)
#
# class Employee(Organization):
#     # def __init__(self,name,Id):
#     #     self.name = name
#     #     self.ID = Id
#     def Employee_details(self):
#         print(self.name,self.ID)
# obj1 = Employee()

'''
Multiple inheritance 
#syntax 
class Parent1:
    properities 
    
class Parent2:
    properties

class Child(Parent1,Parent2):
    properties
'''
# class Parent1:
#     def details_parent1(self,name,staying):
#         print("inside the parent1 class")
#         print(name,staying)
#
# class Parent2:
#     def details_parent2(self,current_staying):
#         print("inside the parent class2")
#         print(current_staying)
#
# class Child(Parent1,Parent2):
#     def details_of_child_class(self,name,standard):
#         print(name,standard)
#
# obj1 = Child()
#
# obj1.details_parent1("kiran","delhi")
# obj1.details_parent2("Heyderabd")


# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =  age
#     def show(self):
#         print(self.name,self.age)
# class Organization(Employee):
#     def __init__(self,ID,address,name,age):
#         self.id = ID
#         self.address = address
#         Employee.__init__(self,name,age)
# abc = Organization("2A","banglore","kiran",23)
# abc.show()


# class Student:
#
#     def __init__(self,name,ID):
#         self.name = name
#         self.id = ID
#
#     def details(self):
#         print(self.name,self.id)
#
#
# class Employye(Student):
#     def employee_details(self,adress):
#         self.address = adress
#         print(self.address)
#         print(self.id)
#
#
# abc = Employye("ramu","2H")
#
# abc.employee_details("address")


#
# class Organization:
#
#     def org_details(self,name,adress):
#         self.name = name
#         self.adress  = adress
#         print(self.name,self.adress)
#
# class Employee:
#     def emp_details(self,name,salary):
#         self.name  = name
#         self.salary = salary
#         print(self.name,self.salary)
#
# class person(Organization,Employee):
#
#     def Person_details(self,identification):
#         self.id = identification
#         print("peson details")
#
# abc = person()
# abc.org_details("HP","banglore")




















