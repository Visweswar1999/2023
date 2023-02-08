
# list1 = [2,4,56,7,8,90,9]
#
# for j in list1:
#
#     if j % 2 == 0:
#         print(j,"even number")
#
#     else:
#         print(j,"odd number")



# for i in range(10):
#
#     if i % 3 != 0:
#         print(i)
#
#     else:
#         print(i,"divisible by 3 ")

# user_input = [2,3,4,4,57,88,9,2]
#
# output = []
#
# for num in user_input:
#     if num not in output:
#         print(num)
#         output.append(num)
# print(output)


#factorial of a number
# 5 --> 5*4*3*2*1
# num = 5

# temp = 1
# for i in range(1,num+1):
#     temp *= i
# print(temp)
    # if num-i:
    #     print(num*num-1)

num = 15

if num>1:

    for i in range(2,num):
        if (num%i) == 0:
            print("not prime")
            break

        else:
            print("prime")
else:
    print("not prime")