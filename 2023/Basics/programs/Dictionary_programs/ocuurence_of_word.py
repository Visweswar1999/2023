user_input = "india is my country and im living in india"

a = user_input.split()

d1 = {}

for i in a:
    if i not in d1.keys():
        d1[i] = 0
    d1[i] = d1[i]+1

print(d1)

