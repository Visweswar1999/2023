#amstrong number is base of n

# 123 --> 1 qube + 2 qube and 3 qube

#check weather the given number is astrong or not

# a = 153
# b = str(a)
# c = len(b)
# temp = 0
# for num in b:
#     g = int(num) ** c
#     temp += g
#
# if temp == a:
#     print("the given number is amstrong number")
#
# else:
#     print("given number is not amstrong number")

#print the amstrong numbers from the range 1-60


# for num in range(1,100):
#     a = str(num)
#     b = len(a)
#     for i in a:
#         result = int(a)**b
#         print(result)

# amstrong numbers range from 1-1000

#
# for i in range(1, 1000):
#
#     result = 0
#
#     num = i
#
#     n = len(str(i))
#
#     while i != 0:
#         digit = i % 10
#         result = result + digit ** n
#         i = i // 10
#     if num == result:
#         print(num)



# num = 153
# length = len(str(num))
# abc = 0
# temp = num
# while temp>0:
#     last = temp%10
#     abc += last ** length
#     temp //= 10
# if num == abc:
#     print("this is an amstrong number")
# else:
#     print("its not an amstrong number")


# num = 6
#
# temp = 1
#
# for i in range(1,num+1):
#
#     temp = temp*i
#
#     print("temp value is",temp)
#
# print(temp)

# fibonacci series

# num1 = 23
#
# num2 = 23.9
#
# print(num1+num2)
#implicit
#explicit
# a = 23
# print("type of a is",type(a))
#
# b = float(a)
# print("type of b is",type(b))








# a = 235
#
# b = str(a)
# temp = a
# print(len(b))
#
# adiition = 0
#
# while temp>0:





#amstrong number range from 1-1000

for i in range(1,1000):

    addition = 0

    length = len(str(i))

    temp = i

    while temp>0:

        last_digit = temp%10

        addition += addition**length

        remove = temp//10

    if addition == i:
        print(i)




























