# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****


# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****


# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *


# 1

# n = 3 

# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

# 2

# n = 5  

# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")

#     for k in range(i + 1):
#         print("*", end="")

#     print()
 

# 3

# n = 5 

# for i in range(n):
#     for j in range(i + 1):
#         print("*", end="")
#     print()

# for i in range(n, 0, -1):
#     for j in range(n - i ):
#         print(" ", end="")

#     for j in range(i):
#         print("*", end="")
        

#     print()



# Exercise 2
# Instructions
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

my_list = [2, 24, 12, 354, 233]  # we have define list
for i in range(len(my_list) - 1): # we make a for loop  for each element in the list
    minimum = i # we create a variable call minimum and  this variable will be increase for each loop 
    for j in range( i + 1, len(my_list)): # we initialize the comparaison on index in odrer to check wich element is smaller and it will take the value in mimimum
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)
