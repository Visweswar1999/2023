
# creating a sample function

# def hello():
#     print("Karnataka")
#
# b = hello()
# addition operation using functions

# def addition(a,b,c):
#     print(a+b)
#     print(a-b)
#
# abc = addition(2,3)


# positional arguments

#
# def new(z,y,t,a,q):
#
#     print(z/y)
#     print(z+y)
#
# abc = new(2,3,3,4,5)
#
# cs = new(y=2,z=3,q=1,a=2,t=2)

#keyword arguments


# def addition(a,b,c):
#     print(a+b)
#     print(a-c)
#
# a = addition(b= 2,a = 4,c = 2 )

#default arguments

# def employee(name,age,salary=20000):
#     print("employee details", name,age,salary)
#     # print("employee age",age)
#     # print("employee salary",salary)
# one = employee("kian",23)
# two = employee("ramu",23,"15000")
# three = employee("ramu",12,"10000")

# variable length arguments

# def addition(name,age):
#
#     a = ""
#     # for i in args:
#     #     a = a+i
#     #
#     # print(a)
#     print(name)
#
# abc = addition(name="kiran",age="muni")




# def addition():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     num3 = num2+num1
#     print(num3)
#
# addition()

# def sample(num1,num2,num3):
#     a = num1-num2
#     print(a)
#     # b = num3+num1
#     # print(b)
# sample(2,3,1)

# def keyword(num1,num2,num3,num4):
#     print(num1*num2)
#     print(num1-num2)
# keyword(num2=1,num1=3,num4=32,num3=12)

# add the list of numbers using the functions

# def addition(num1,num2):
#     a = num1 +num2
#     print(a)
#
# a = addition(2,3)


# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print("result of the two numbers is",a+b)


# a = [2,4,2,45,12,3]
#
# def add():
#     temp = 0
#     for i in a:
#         temp = temp+i
#     print(temp)
# output = add()


# a = int(input("Enter the first number: "))
# b = int(input("ENter the second number: "))
#
# print(a+b)


# def addition():
#
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     print("result of the two numbers is:",num1+num2)
#
# a = addition()
# b = addition()
# c = addition()

# num = 1234
# print("type of a is",type(a))
#
# b = str(a)
# print("type of b is",type(b))
# print("lenghth of the number is",len(b))

# num = 23
#
# b = str(num)
#
# length = len(b)
#
# temp = int(b[0])
#
# temp1 = int(b[1])
#
# result = temp**length+temp1**length
#
# if num == result:
#     print("its an amstrong number")
#
# else:
#     print("its not an amstrong number ")
#
# num = 123
#
# print(num//10)
# def new_file():
#     num1 = int(input("enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     print("multiplication of the two numbers is",num1*num2)
# new_file()
# new_file()
# new_file()
# new_file()





#example of the keyword arguments


# def addition(num1,num2):
#     print(num1-num2)
#
# addition(num2=3,num1=2)

#default arguments

# def employee(name,age=23):
#     print("employee name",name,"employee age is ",age)
#
# employee("kiran",12)
# employee("mahesh")

#variable length arguments

# *args

# def variable_lenghth(*args):
#     print(sum(args))
#
# variable_lenghth(2,2,3,4,5,1,2)


# def one(b,a=2,c=5):
#
#     print(a+b)
#     print(a-c)
#
# one(2,3)

# variable length arguments

def add(*args):
    print(sum(args))

add(2,1,2,1,0,1)


















