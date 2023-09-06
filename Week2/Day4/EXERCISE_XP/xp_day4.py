# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

# def display_message(course):
#     print('In this course we are learning ' + course)

# display_message('python')


# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.


# def favorite_book(title):
#     print('One of my favorite books is ' + title) 


# favorite_book('le petit prince')


# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.


# def describe_city(city = 'tlv', country = 'Israel'):
#     print(city + ' is in ' + country)

# describe_city('Reykjavik', 'Iceland')
# describe_city()


# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

# import random


# user_number = int(input("Enter a number between 1 and 100: "))

# def my_fuction(user_number):
#     if user_number < 1 or user_number > 100 :
#         return "Please enter a number between 1 and 100."
#     else:
#         return "Your number is {user_number}"
    
#  my_fuction(user_number)



# import random

# def compare_numbers(user_number):
#     if user_number < 1 or user_number > 10:
#         return "Please enter a number between 1 and 100."

#     random_number = random.randint(1, 10)

#     if user_number == random_number:
#         return "Success! You guessed the correct number: " + user_number
#     else:
#         return f"Fail! Your number: {user_number}, Random number: {random_number}"


# user_input = int(input("Enter a number between 1 and 10: "))
# result = compare_numbers(user_input)
# print(result)

# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.


# def make_shirt(size = 'Large', text= 'I love Python'):
#     print(f"The size of the shirt is " + size + " and the text is " + text)

# make_shirt('M', 'hello toi')
# make_shirt()
# make_shirt('Medium',)
# make_shirt('Extra Large', 'I love Javascipt')


# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.


# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(my_list):
#     for name in my_list:
#         print(name)

# show_magicians(magician_names)

# def make_great(my_list):
#     for name in range(len(my_list)):
#         my_list[name] = my_list[name] + ' the Great'
        

# make_great(magician_names)

# show_magicians(magician_names)





# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
# import random

# def get_random_temp(season):
#     if season == 'winter'.lower():
#         return round(random.uniform(-10, 16),1)
#     elif season == 'Spring'.lower():
#         return round(random.uniform(17, 23),1)
#     elif season == 'Summer'.lower():
#         return round(random.uniform(33, 40),1)
#     elif season == 'Autumn'.lower():
#         return round(random.uniform(24, 32),1)

# def main():
#     season_user = input('in which season are we \n')
#     random_temperature = get_random_temp(season_user)  
#     if random_temperature < 0:
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. Brrr, that’s freezing! Wear some extra layers today')
#     elif 0 <random_temperature < 16:
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. Quite chilly! Don’t forget your coat')
#     elif 17 <random_temperature < 23:
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. Very agreable temperature')
#     elif 24 <random_temperature < 32:
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. Summer is comming ')
#     else :  
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. very hot today ')
    

# main()

# --------
# BONUS PART 

# import random


# def get_random_temp():
#     month_input = int(input('in which month are we ? \n'))
#     if 3 <= month_input <= 5:
#          return round(random.uniform(17, 23),1)
#     elif 6 <= month_input <= 8:
#         return round(random.uniform(33, 40),1)
#     elif 9 <= month_input <= 11:
#         return round(random.uniform(24, 32),1)
#     elif  1 <= month_input <= 2 or month_input == 12:
#         return round(random.uniform(-10, 16),1)
    

# def main():
#     random_temperature = get_random_temp()  
#     if random_temperature < 0:
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. Brrr, that’s freezing! Wear some extra layers today')
#     elif 0 <random_temperature < 16:
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. Quite chilly! Don’t forget your coat')
#     elif 17 <random_temperature < 23:
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. Very agreable temperature')
#     elif 24 <random_temperature < 32:
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. Summer is comming ')
#     else :  
#         return print(f'The temperature right now is {random_temperature} degrees Celsius. very hot today ')
    

# main()

# -------



# 🌟 Exercise 5 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

import random


data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]



#

