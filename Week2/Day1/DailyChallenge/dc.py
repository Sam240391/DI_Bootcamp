
# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# HelloWorld


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod






# user_choice = input(f'Choose a string or your choice ": \n ' )
# len_user_choice = len(user_choice)

# print(f'{len_user_choice} \n')


# if len_user_choice < 10:
#     print('string not long enough')
# elif len_user_choice > 10:
#     print('string too long')
# else:
#     print('perfect string')

# first_char = user_choice[0]
# last_char = user_choice[-1]

# print(f"{first_char} {last_char}")


# charactere = ''

# for char in user_choice:
#     charactere += char
#     print(charactere)

# print(user_choice)



# *********
# BONUS

# import random

# user_input = input("Enter a string: ")

# char_list = list(user_input)

# print(f'{char_list}')

# random.shuffle(char_list)

# jumbled_string = ''.join(char_list)

# print("Jumbled string:", jumbled_string)