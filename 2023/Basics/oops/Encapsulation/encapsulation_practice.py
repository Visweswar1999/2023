
# Access modifiers in python
#use of public method
# class Worker:
#     def __init__(self,name,work):
#         self.name = "viswa"
#         self.work = "painter"
#     def result(self):
#         print(self.name,self.work)
# obj1 = Worker("kiran","carpenter")
# print(obj1.work)

#use of private method

# class Employee:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def show(self):
#         print(self.name,self.__age)
#
# a = Employee("viswa",23)
#
# print(a._Employee__age)
#to access the members in the private methods we will be calling the same function inside the class or by name pilling



# class Labour:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#
#     def output(self):
#         print(self.name,self.__age)
#
# a = Labour("ramu",23)

# class Company:
#
#     def __init__(self):
#
#         self._project = "AI"
#
# class Employee(Company):
#
#     def __init__(self,name):
#         self.name = name
#         Company.__init__(self)
#
#     def output(self):
#         print(self.name)
#         print(self._project)
#
# a = Employee("my_company")
#
# a.output()


#09-03-2023

















