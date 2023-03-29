# syntax of the constructor
'''


def __init__():
    #body of the constructor

'''

# creating a sample constructor

'''
class Employee:

    # constructor

    # initialise instance variables

    def __init__(self, name, number):
        # inside the constructor these values are there
        self.name = name
        self.number = number

    # instance method

    def show(self):
        print(self.name,self.number)


# creating the object using the constructor

employee1 = Employee("mahesh", 234)

employee1.show()

'''

# creating a default constructor

'''

class Student:

    def show(self):
        print("addition of 2+3 is",2+3)


student1 = Student()
student1.show()

'''

# non_parameterized constructor

'''

class Company:
    # no argument constructor
    def __int__(self):
        self.name = "kiran"
        self.address = "123456"

    # method for printing the data members
    def show(self):
        print(self.name, self.address)
# creating the object of the clas


company1 = Company()

# calling the instance method using the object

company1.show()

'''

# parameterized constructor

'''

class Organization:
    # parameterized constructor
    def __init__(self,name, number, state):
        self.name = name
        self.number = number
        self.state = state

    # display object

    def show(self):
        print(self.name,self.number,self.state)


employee = Organization("kiran",123,"u.p")

employee.show()
'''

# constructor with default values
'''
class Employee:

    def __init__(self,address,name="kiran"):
        self.name = name
        self.address = address

    def show(self):
        print(self.name,self.address)


abc = Employee("209")
abc.show()
'''

# class Student:
#
#     def __init__(self):
#         print("abc")
#
# abc = Student()


# non parameterrized constructor


# class Student:
#
#     def __init__(self):
#         self.name = "kiran"
#         self.number = "09876"
#
#     def output(self):
#         print(self.name, self.number)
#
# abc = Student()
#
# abc.output()


# parameterized constructor

# class Oraganization:
#
#     def __init__(self,employee,number):
#         self.employee = employee
#         self.number = number
#
#     def result(self):
#         print(self.employee,self.number)
#
# a = Oraganization("kiran","0987")
#
# a.result()

# comprehensions


# write a code in a consided way is called comprehension

# for i in range(1,20):
#     if i%2 == 0:
#         print(i,"even")
#
#
# a =  [x for x in range(1,20) if x%2 == 0]
#
#
# print(a)

#
# num1 = input(' ')
#
# if num1%2 == 0:
#     print("this is even number")
#
# else:
#     print("it is odd number")


# class Employee:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
#
# abc = Employee("kian",23)

#
# def div(a,b):
#     print(a/b)
#
# def decorator(func):
#
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#
#         return func(a,b)
#
#     return inner()
#
# div1 = generator(div)
#
# div = (2,4)

'''
def add(a,b):
    return a+b

def multiplication(func,a,b):
    return func(a,b)

abc = multiplication(add,2,4)

print(abc)

'''

# single inheritance

# class vehicle():
#
#     def vehicle_info(self):
#
#         print("inside the vehicle class")
#
# class car(vehicle):
#
#     def car_info(self):
#
#         print("inside the car class ")

# a = car()
#
# a.vehicle_info()
#
# a.car_info()


# multiple inheritance
#
# class employee:
#
#     def emp_details(self,name,age):
#         print(name,age)


# user_input = [2,3,4,5,6]
#
# output = []
# for num in user_input:
#     output.append(num**2)
#
# print(output)
#
# a = [x for x in range(1,10) if x%2 ==0]
#
# print(a)



# for i in range(1,10):
#
#     if i%2 == 1:
#         print(i,"even")
#     else:
#         print(i)
#
#
#
# a = [i for i in range(1,10) if i%2 == 0]
#
# print(a)



# a = [2,3,4,5,6,5]
#
# for num in a:
#     print(num**4)
#
# abc = [num**2 for num in a]
#
# print(abc)



#single inheritance
#
# class Employee:
#
#     def show(a,name,id):
#         print(name,id)
#
# class Details(Employee):
#
#     def output(a,address,contact_number):
#         print(address,contact_number)
#
# abc = Details()
#
# abc.show("kiran","JLL9")
#
# abc.output("banglore",654)

# class Student:
#     def __init__(self,name,address,age,gender,ID,Section,bloodgroup):
#         self.name = name
#         self.adress = address
#         self.age = age
#         self.gender = gender
#         self.id = ID
#         self.section = Section
#         self.blood = bloodgroup
#     def Student_personaldetails(self):
#         print(self.name,self.adress,self.gender,self.blood)
#     def Student_school_details(self):
#         print(self.name,self.age,self.id,self.section)
#     def Alldetails(self):
#         print("name",self.name,self.adress,self.age,self.gender,self.id,self.section,self.blood)
#
# Student1 = Student("ramu","banglore",23,"Male","24","A","B+")
# Student2 = Student("kiran","hyd",20,"Male","2H","A","A+")
# #print(personal_setails(Student2)
# Student2.Alldetails()



