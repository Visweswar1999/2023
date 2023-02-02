# factorial of a 5 is 5*4*3*2*1



user_input = int(input("Enter the number: "))

temp = 1

for i in range(1,user_input+1):
    temp = temp*i

print("factorial of a",user_input,"is",temp)


