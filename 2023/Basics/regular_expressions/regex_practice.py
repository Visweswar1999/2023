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

user_input = "im from india and im living in india 13987653245678 34 "

a = re.findall("[a-zA-Z]",user_input)
#

print(a)
















