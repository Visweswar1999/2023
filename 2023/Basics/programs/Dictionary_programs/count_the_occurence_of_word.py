a = "india is my country and and im living in india"

b = a.split()

d1 = {}

for i in b:

    if i not in d1.keys():
        d1[i] = 0
    d1[i] = d1[i]+1

print(d1)