# encapsulation

#public

# class Labour:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# object = Labour("sathvik",24)
#
# print(object.age)


#private

# class Employee:
#
#     def __init__(self,desig,work):
#         self.abc = desig
#         self.__bcd = work
#
#     def output(self):
#         print(self.abc,self.__bcd)
#
# object1 = Employee("TL","something")
#
# object1.output()


#protected

# class Organization:
#
#     def __init__(self):
#         self._name = "dinesh"
#
# class Employee(Organization):
#
#     def __init__(self,name,follower):
#         self.name = name
#         self.followr = follower
#         Organization.__init__(self)
#
#     def output(self):
#         print(self.name,self.followr)
#         print(self._name)
#
#
# object1 = Employee("santhosh",23)
# object1.output()


#setter and getter methods


