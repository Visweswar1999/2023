user_input = int(input("Enter the number: "))

a = str(user_input)

result = 0

for i in a:
    temp = int(i)

    output = 1

    for j in range(1,temp+1):

        output = output*j

    # print(result)

    result += output

print(result)
















