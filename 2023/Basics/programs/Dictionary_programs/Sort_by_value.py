# import operator
#
# user_input = {"one":2,"two":1,"three":3}
#
# sorted_d = sorted(user_input.items(),key=operator.itemgetter(1))
#
# # sorted_da = dict( sorted(user_input.items(),key=operator.itemgetter(1),reverse=True))
#
# print(sorted_d)

user_input = {"bne":2,"cwo":1,"ahree":3}

b = sorted(user_input.items(),reverse=False)

print(b)

