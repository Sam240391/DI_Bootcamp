# Exercise 1: Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

# list1 = [1,2,3]
# list2 = [3,4,5]
# list1.extend(list2)
# print(list1)

# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.


# for x in range(1500, 2501):
#     if x % 5  == 0 and x % 7 == 0:
#         print(x)



# Exercise 3: Check The Index
# Instructions
# Using this variable

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1


# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# user_input = input('What is your name ?')

# if user_input in names:
#     print(names.index(user_input))
# else:
#     print('your name is not in the list')


# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.

# user_choice1 = input('Give me a number')
# user_choice2 = input('Give me a number')
# user_choice3 = input('Give me a number')

# greatestnumber = 0

# if user_choice1 >= user_choice2 and user_choice1 >= user_choice3:
#     greatestnumber = user_choice1
# elif user_choice2 >= user_choice3 and user_choice2 >= user_choice1:
#     greatestnumber = user_choice2
# else:
#     greatestnumber = user_choice3

# print(greatestnumber)


#     Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.


# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# for letter in alphabet:
#     if letter in 'aeiou':
#         print(f'{letter} is a vowel.')
#     else:
#         print(f'{letter} is a consonant.')



# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.


# words = []

# for word in range(7):
#     word = input('give me a word')
#     words.append(word)

# print(words)

# letter = input('choose a letter')

# for word in words:
#     if letter in word:
#         print(f'letter {letter} is in {word} and his index is : {word.index(letter)}')
#     else:
#         print(f'the letter {letter} is not in {word}')

# my_list = range(1, 1000001)

# print(max(my_list))
# print(min(my_list))
# print(sum(my_list))


# Exercise 8 : List And Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.

# list1 = input(f'Give me numbers separate with comma')
# print(list1)

# my_list = []

# for num in list1.split(','):
#     my_list.append(int(num))


# print(my_list)

# my_tuple = tuple(my_list)

# print(my_tuple)

# import random

# attempt = 0

# while True:
#     user_choice = int(input('Choose a number between 1 and 9 inculded'))
#     random_number = random.randint(1,9)
#     if user_choice == random_number:
#         print('Winner')
#         break
#     else:
#         attempt += 1
#         print(f'try again {attempt} attempt')
       



