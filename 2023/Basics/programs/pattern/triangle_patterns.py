# '''
# *
#
# * *
#
# * * *
#
# * * * *
#
# * * * * *
# '''
#
# user_input = int(input("Enter the number: "))
#
# for lines in range(1,user_input):
#
#     for rows in range(lines,lines+1):
#

'''

* * *
* * *
* * *

'''

# star pattern

'''
n = 3

for i in range(n):

    for j in range(n):

        print("*",end = ' ')

    print() 
'''


'''
# left angle triangle 

* 
* * 
* * *

'''
'''
n = 3
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''

#reverse left angle triangle

'''
* * * * 

* * * 

* * 

*

'''

'''
n = 4
for i in range(n):
    for j in range(i,n):
        print("*",end = '')
    print() 
'''

# spaces with triangle

'''
      *
    * *
  * * *
* * * *

'''

'''
n = 4

for i in range(n):

    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i+1):
 
        print("*",end= " ")

    print()
'''

'''   
****
 ***
  **
   *
'''

'''
n = 4

for i in range(n):

    for j in range(i):
        print(" ",end = " ")

    for j in range(i,n):
        print("*",end=" ")

    print()
'''

'''
                   * 
                  *  *
                *  *   * 
                
'''

'''
n = 4

for i in range(n):
    

    for j in range(i,n):
        print("", end = " ")

    for j in range(i+1):

        print("*", end= " ")

    print()
    
'''


'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

'''

'''
n = 5
for i in range(n):
    for j in range(i):
        print("",end=" ")
    for j in range(i,n):
        print("*",end = " ")
    print() 
'''



# n = 4
#
# for i in range(n):
#
#     for j in range(i,n):
#         print("",end=" ")
#
#     for j in range(i+1):
#         print("*",end=" ")
#
#     print()







'''

* * * * 
* * * *
* * * * 
* * * *

*
* * 
* * * 
* * * *

'''


'''
* * * * 

* * * * 

* * * * 

* * * *

'''

# num = 4
#
# for i in range(num): #  4 times
#     for j in range(num):
#         print("#",end = " ")
#     print()

'''
* 
* * 
* * * 
* * * *
'''
# num = 4
#
# for i in range(num):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()



'''
* * * *

* * * 

* * 

*
'''
# num = 4
#
# for row in range(num):
#     for column in range(num-row):
#         print("*",end=" ")
#     print()

'''
      *
    * * 
  * * *
* * * *

'''

'''
* * * * 

* * * * 

* * * * 

* * * *

* 
* * 
* * * 
* * * *

* * * *
* * * 
* * 
*

      *
    * *
  * * *
* * * *
'''


try:
    print(5/"kkr")

except (TypeError,ZeroDivisionError):
    print("Here type error occured")










