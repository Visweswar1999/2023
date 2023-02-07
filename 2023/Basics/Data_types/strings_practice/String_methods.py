# capitalize()	    --> Converts the first character to upper case
# casefold()        --> Converts string into lower case
# center()	        --> Returns a centered string
# count()	        --> Returns the number of times a specified value occurs in a string
# encode()      	--> Returns an encoded version of the string
# endswith()	    --> Returns true if the string ends with the specified value
# expandtabs()	    --> Sets the tab size of the string
# find()	        --> Searches the string for a specified value and returns the position of where it was found
# format()	        --> Formats specified values in a string
# index()	        --> Searches the string for a specified value and returns the position of where it was found
# isalnum()	        --> Returns True if all characters in the string are alphanumeric
# isalpha()	        --> Returns True if all characters in the string are in the alphabet
# isascii()	        --> Returns True if all characters in the string are ascii characters
# isdecimal()	    --> Returns True if all characters in the string are decimals
# isdigit()     	--> Returns True if all characters in the string are digits
# isidentifier()	--> Returns True if the string is an identifier
# islower()	        --> Returns True if all characters in the string are lower case
# isnumeric()	    --> Returns True if all characters in the string are numeric
# isprintable()	    --> Returns True if all characters in the string are printable
# isspace()     	--> Returns True if all characters in the string are whitespaces
# istitle()     	--> Returns True if the string follows the rules of a title
# isupper()     	--> Returns True if all characters in the string are upper case
# join()	        --> Converts the elements of an iterable into a string
# ljust()	        --> Returns a left justified version of the string
# lower()	        --> Converts a string into lower case
# lstrip()	        --> Returns a left trim version of the string
# maketrans()	    --> Returns a translation table to be used in translations
# partition()	    --> Returns a tuple where the string is parted into three parts
# replace()	        --> Returns a string where a specified value is replaced with a specified value
# rfind()	        --> Searches the string for a specified value and returns the last position of where it was found
# rindex()	        --> Searches the string for a specified value and returns the last position of where it was found
# rjust()	        --> Returns a right justified version of the string
# rpartition()	    --> Returns a tuple where the string is parted into three parts
# rsplit()	        --> Splits the string at the specified separator, and returns a list
# rstrip()      	--> Returns a right trim version of the string
# split()	        --> Splits the string at the specified separator, and returns a list
# splitlines()      -->	Splits the string at line breaks and returns a list
# startswith()	    --> Returns true if the string starts with the specified value
# strip()	        --> Returns a trimmed version of the string
# swapcase()	    --> Swaps cases, lower case becomes upper case and vice versa
# title()	        --> Converts the first character of each word to upper case
# translate()   	-->Returns a translated string
# upper()	        -->Converts a string into upper case
# zfill()	        --> Fills the string with a specified number of 0 values at the beginning



#use of capialize method
'''
char1 = "kiran"

abc = char1.capitalize()

print(char1)

print(abc)

'''

# use of casefold method

'''
user_input = "KIRAN kumar"

a = user_input.casefold()

print(a) '''

# use of center method
'''

user_input = "Center method"

print(f"before using the center method")

print(user_input)

a = user_input.center(15)

print(f"after using the center method")
print(a)
'''

#use of count method

'''

user_input = "harish "

b = user_input.count("a")

print(b) '''

# use of encode method

'''

user_input = "Encode method 𝖛𝖎𝖘𝖜𝖆"

abc = user_input.encode()

print(abc) '''

# use of ends with method


'''
user_input = "visweswar pamujula"

a = user_input.endswith("a")
print(a)
 
'''


#use of expand tab method


'''
abc = "visweswar pamujula"
user_input = "visweswar\tpamujula"

abc = user_input.expandtabs(4)

print(abc)
print(user_input)
'''

#use of find method

'''
user_input = "Mahesh 123"

a = user_input.find("1")

print(a)

'''


#use of format method


'''

# it will format the secified value 

user_input = "Mahesh{number} "

a = user_input.format(number = "4")

print(a) 

'''

#use of index method

'''
user_input = "Mahesh"

a = user_input.index("h")

print(a)

'''

# use of alnum method
'''
#it will return true or false if all the charecters in the string is alfa numeric

user_input = "Mahesh 12"

a = user_input.isalnum()

print(a) '''


#use of isalpha method

'''
user_input = "Mahesh12"

a = user_input.isalpha()

print(a)

'''

#

#use of isascii method

'''

abc = "Mahesh "

b = abc.isascii()

print(b)

'''

#use of isdecimal

'''
# use isdecimal  method

user_input = "12312"

a = user_input.isdecimal()

print(a)

'''


#use of isdigit method

'''

user_input = "Mahesh"

abc = user_input.isdigit()

print(abc)

'''

