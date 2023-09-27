# Exercise 1 : When Will I Retire ?
# Instructions
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.

# current_year = 2023
# current_month = 9
# current_day = 26

# def get_age(year, month, day):
#     age = current_year - year
#     if current_month < month : 
#         age -= 1
#     elif current_month == month:
#         if current_day < day:
#             age -= 1
#     return age



# def can_retire(gender, date_of_birth):
#     date_of_birth = date_of_birth.split('/')
#     your_year = int(date_of_birth[0])
#     your_month = int(date_of_birth[1])
#     your_day = int(date_of_birth[-1])
    
#     if gender  == 'M' and get_age(your_year, your_month, your_day) > 67:
#         return True
#     elif gender == 'F' and get_age > 62:
#         return True
#     else:
#         return False

# gender = input(f' What is your gender').upper()
# date_of_birth = input(f'What is your birthday')

# if can_retire(gender, date_of_birth):
#     print(f"You can retire")
# else:
#     print(f'You are too young to retire')

# Exercise 2 : Sum
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

# Hint: treating our number as a int or a str at different points in our code may be helpful

# def sumx(X):
#     if isinstance(X, str):
#         print(f'Choose an int')
#         sum(X)
#     else:
#         X = X+(X*11)+(X*111)+(X*1111)
#     return X

# print(sumx(3))


# Exercise 3 : Double Dice
# Instructions
# Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
# Create a function called throw_until_doubles.
# It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
# For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# This function should return the number of times it threw the dice in total. In the example above, it should return 3.

# Create a main function.
# It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).

# After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
# Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
# For example:

# If the results of the throws were as follows (your code would do 100 doubles, not just 3):
# (1, 2), (3, 1), (5, 5)
# (3, 3)
# (2, 4), (1, 2), (3, 4), (2, 2)

# Then my output would show something like this:
# Total throws: 8
# Average throws to reach doubles: 2.67.


import random


def throw_dice():
    number = random.randint(1, 6)
    return number




def throw_until_doubles():

    attempt = 1

    while True:
        number_1 = throw_dice()
        number_2 = throw_dice()

        if number_1 == number_2:
            print(f'({number_1}, {number_2})')
            print(f'you made {attempt} attenmps')
            break
        else:
            print(f'({number_1}, {number_2})')
            attempt += 1

    return attempt


print(throw_until_doubles())

def main():
    collection = {}
    attemps = 0

    for i in range(1, 101):
        collection[i] = throw_until_doubles()

    for key, values in collection.items():
        attemps += values

    print(collection)
    print(f'{attemps/100}')

main()

