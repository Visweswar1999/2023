#to print the series of fibonacci numbers

user_input = int(input("Enter the number: "))

first = 0

second = 1

# for i in range(user_input):
#     print(first)
#     temp = first
#     first = second
#     second = temp + second


for i in range(user_input):
    print(first)
    temp = first
    first = second
    second = temp+second

