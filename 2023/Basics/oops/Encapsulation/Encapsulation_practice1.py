# class Employee:
#
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#
#     def show(self):
#         print(self.__name,self.age)
#
# Employee1 = Employee("ramu",23)
#
# Employee1.show()
































class Employee:

    def __init__(self,name,salary):
        self.name =name
        self.__salary = salary

    def output(self):
        print(self.name,self.__salary)

obj1 = Employee("hari",23)

obj1.output()



















