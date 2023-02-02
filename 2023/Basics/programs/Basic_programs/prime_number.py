#check the given number is prime or not

user_input = 23

for num in range(2,user_input):
    if user_input%num == 0:
        print("its not an prime number")
        break

    else:
        print("its an prime number")
        break