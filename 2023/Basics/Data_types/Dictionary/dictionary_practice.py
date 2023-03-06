#use of clear method


'''
user_input = {1:"kiran",2:"ramu"}

user_input.clear()

print(user_input)

'''

#use of copy method
'''
user_input = {1:"kiran",2:"ramu"}

print("before using the copy method")

print(user_input)

b = user_input.copy()

print("after usinig the copy method")

print(b)
'''

# use of fromkeys

'''

user_input = {1:"kiran",2:"ramu",3:"manoj",4:"chaithu"}

temp = "tem value"

b = dict.fromkeys(user_input,temp)

print(b) 

'''

#use of get method

'''
user_input = {1:"employee",2:"mahesh","3":"kiran"}

b = user_input.get("3")

print(b) 

'''

#use of items method

'''
user_input = {1:"employee",2:"mahesh","3":"kiran"}
c = user_input.copy()
b = user_input.items()
print("by using the copy method")
print(c)
print("by using the items method")
print(b)

'''

#use of keys method

'''
user_input = {1:"employee",2:"mahesh","3":"kiran"}

a = user_input.keys()

print(a)

'''

#use of pop method

'''

user_input = {1:"employee",2:"mahesh","3":"kiran"}

print(user_input.pop(2))

print(user_input) 

'''

#use of popitem

'''

user_input = {1:"employee",2:"mahesh","3":"kiran"}

b = user_input.popitem()

print(user_input)

print(b)

'''

# setdefault

'''
user_input = {1:"employee",2:"mahesh","3":"kiran"}

b = user_input.setdefault(1,"abc")

print(b)
print(user_input) '''

# use of update method

# by using this method it will update the dictionary and add the element at the ending of the dictionary
# if the key is presented in the dictionry the value will be updated


'''
user_input = {1:"employee",2:"mahesh","3":"kiran"}

user_input.update({"3":"madhu"})

print(user_input)

'''

# use of values method

'''

user_input = {1:"employee",2:"mahesh","3":"kiran"}

b = user_input.values()

print(b) 

'''

# user_input = {"employee":"kiran",3:"ramu",2:"ramesh","somu":"mahesh","two":"jai","one":"hari"}

#dict

# user_input.update({"newkey":"new value"})
#
# print(user_input)



user_input = {1:"value1",2:1.3,"key3":"value3"}

a = user_input.values()

print(a)
