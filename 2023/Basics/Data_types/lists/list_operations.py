#list operations in python

'''
1.append
2.extend
3.sort
4.insert
5.remove
6.pop
7.slice
8.reverse
9.len
10.min&max
11.count
12.concatinate
13.multiply
14.index
15.clear '''
#use of append method
'''
user_input = [2,3,5,6,0]

for i in range(1,10):
    user_input.append(i)
print(user_input)

#use of extend method

user_input = []

user_input.extend([2,3,4,6])

print(user_input) 

#use of sort method

user_input = [2,4,3,4,5,2,43]

user_input.sort()

print(user_input) 

#use of insert method

user_input = [2,3,4,5,1,1]

user_input.insert(0,1)

print(user_input) 

#use of remove method

user_input = [3,4,5,5,2,2,34,2]

user_input.remove(5)

print(user_input)

#use of pop method

user_input = [3,4,4,2,23,4,5]

user_input.pop(0)

print(user_input)

# use of slice method

user_input = [3,4,4,2,23,4,5]

a = user_input[:2]

print(a)

#use of reverse method

user_input = [3,4,4,2,23,4,5]

user_input.reverse()

print(user_input)

# use of len method

user_input = [3,4,4,2,23,4,5]

a = len(user_input)

print(a) 

#use of min and max methods

user_input = [3,4,4,2,23,4,5]

a = min(user_input)
b = max(user_input)

print(a)
print(b) 
 


#use of count method

user_input = [3,4,4,2,23,4,5]

a = user_input.count(4)

print(a)

#use of concatenate method
user_input = [3,4,4,2,23,4,5]
user_input1 = [5,3,2,4,4]

print(user_input+user_input1)


#use of multiply method
user_input = [3,4,4,2,23,4,5]

a = user_input*5 

#use of index method
user_input = [3,4,4,2,23,4,5]

# print(user_input.index(4))

print(user_input.index(2,0,6)) 

#use of clear method

user_input = [2,3,4,1,3,4,5]

user_input.clear()

print(user_input) 

#use of clear method in dictionay

user_input = {1:"one",2:"Two",3:"three"}

print(user_input)

user_input.clear()'''










user_input = [2,3,4,56,34,65,2,2,2,23,4]


user_input.clear()

print(user_input)













