# num1 = 10
#
# num2 = 0
#
# print(num1/num2)

# try:
#     num1 = 20
#     num2 = 2
#     print(num1/num2)
#
# except:
#     print("not divided by zero")
#
# finally:
#     print("this is final block")

# try:
#
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     a = num1/num2
#     print(a)
#
# except ValueError:
#     print("You enterd the string value")
#
# except ZeroDivisionError:
#     print("zero is not divided")
#
# finally:
#     print("this block is executed")

# try:
#
#     list1 = [2,4,5,6,7,"abc"]
#     print(list1[9])
#
# except IndexError:
#     print("santhosh")
# try:
#     a = 23
#     b = 1
#     print(a/b)
#
# except (ValueError,ZeroDivisionError,TypeError):
#     print("except block")
#
# else:
#     print("else block")
#
# finally:
#     print("this is finally block")


# try:
#     a = int(input("enter the first number "))
#     b = int(input("enter the second number"))
#
# except :
#     print("enter correct values")
#
# finally:
#     print("finally block is executed")


#
try:
    num1 = 12
    num2 = "abc"
    print(num1/num2)
except (ZeroDivisionError,TypeError):
    print("This is except block")












