# class Employee:
#
#     def __init__(self,name,age,id,address):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.address = address
#
#     def show(self):
#         print(self.name,self.age)
#
#     def output(self):
#         print(self.id,self.address)
#
# obj1 = Employee("kiran",23,"N12","somewhere")
#
# obj1.output()


# class Employee:
#
#     def show(self):
#         print("no constructor")
#
#     def second_fun(self):
#         print("second function")
#
# obj1 = Employee()
#
# obj1.second_fun()


#
# class Employee:
#     def __init__(self,age,name= 23):
#         self.name = "kiran"
#         self.age = age
#
#     def show(self):
#         print(self.name,self.age)
#
#
# abc = Employee(19)
# abc.show(23,"kiran")

class Employee:
    def __init__(self,age,name= "ramu"):
        #instance variable
        self.name = "mahesh"
        self.age = 23
    def show(self):
        print(self.name,self.age)
abc = Employee(20)
abc.show()



#create an employee class and pass three arguments print the address,colony,pincode








