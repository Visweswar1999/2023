# import re
#
# string1 = "india is my country"
#
# a = re.findall("in",string1)
# b = re.search("in",string1)
# c = re.split("in",string1)
# # d = re.sub("in",2,string1)
#
# print(f"by using the findall method {a}")
# print(f"by using the search method {b}")
# print(f"by using the sub method {c}")


import re

# variable = re.findall("pattern",*string)

user_input = "India  EEEE is my country is and im living in 28088754785 india @"

a = re.findall("[a-zA-Z]",user_input)

#  (3,4,5)(8,9)

# (38,39,48,49,58,59)

print(a)
















