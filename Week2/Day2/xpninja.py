# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:18,22,24

import math

# C = int(input(f'Enter a number as C'))
# D = int(input(f'Enter a number as D'))
# H = int(input(f'Enter a number as H'))

# Q = math.sqrt((2 * C * D) / H)

# print(Q)

# C = 50
# H = 30

# D = int(input(f'Enter a number as D'))
# Q = math.sqrt((2 * C * D) / H)

# print(Q)

# result = []

# user_input = input(f'Enter a comma_separated string of number')
# numbers_user = user_input.split(',')

# print(numbers_user)
# result = []

# for D in numbers_user:
#     D = int(D)
#     Q = math.sqrt((2 * C * D) / H)
#     Q = round(Q)
#     result.append(Q)


# result = [str(nombre) for nombre in result]
# result_str = ', '.join(result)

# print(result_str)
    

# Exercise 2 : List Of Integers
# Instructions
# Given a list of 10 integers to analyze. For example:

# my_list1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# print(my_list1)

# print(sorted(my_list1, reverse=True))

# print(sum(my_list1))

# my_list2 = [my_list1[0], my_list1[-1]]

# print(my_list2)

# my_list3 = [number for number in my_list1 if number > 50]
# print(my_list3)
# my_list4 = [number for number in my_list1 if number < 10]
# print(my_list4)

# my_list5 = []
# for number in my_list1 :
#     squarednumber = number*number
#     my_list5.append(squarednumber)

# print(my_list5)


# print(list(set(my_list1)))


# print(len(my_list1))



# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.



# my_paragraph = 'Python is used for server-side web development, software development, mathematics, and system scripting, and is popular for Rapid Application Development and as a scripting or glue language to tie existing components because of its high-level, built-in data structures, dynamic typing, and dynamic binding. Python is used for server-side web development, software development, mathematics, and system scripting, and is popular for Rapid Application Development and as a scripting or glue language to tie existing components because of its high-level, built-in data structures, dynamic typing, and dynamic binding.'
# import re

# print(my_paragraph)
# print(len(my_paragraph))

# my_sentences = my_paragraph.split('.')
# print(my_sentences)
# print(len(my_sentences) - 1)

# print(f'We have {len(my_paragraph.split())} words in the paragraphe')

# my_paragraphnet = re.sub("\!|\.|\,","",my_paragraph)
# print(my_paragraphnet)
# my_words = my_paragraphnet.split()
# print(my_words)
# unique_words = []

# for words in my_words:
#     if words not in unique_words:
#         unique_words.append(words)


# print(unique_words)
# print(len(unique_words))

# Exercise 4
# Instructions
# Write a program that prints the frequency of the words from the input.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1


# user_input = input(f' Enter a sentence')

# user_input_list = user_input.split()
# print(user_input_list)

# for word in user_input_list:
#     print(f'{word} : {user_input_list.count(word)}')