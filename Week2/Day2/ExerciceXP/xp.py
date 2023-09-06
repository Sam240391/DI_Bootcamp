# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# --------------

# 1.

# my_fav_numbers = {4,14,24,26,29}
# 2.

# my_fav_numbers.update([9, 13])
# print(my_fav_numbers)

# 3.
# my_fav_numbers_list = list(my_fav_numbers)
# print(my_fav_numbers_list)
# my_fav_numbers_list.pop()
# print(my_fav_numbers_list)
# my_new_set = set(my_fav_numbers_list)
# print(my_new_set)

# 4.
# friend_fav_numbers = {1,2,3,4,5}

# 5.

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# No, it is not possible to add more integers (or any other elements) to an existing tuple in Python. Tuples are immutable, which means their elements cannot be changed, added, or removed after the tuple is created.



# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
# -----------------------

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append('Kiwi')
# print(basket)

# basket.insert(0, "Apples")
# print(basket)
# number_apples = basket.count("Apples")
# print(f'We have {number_apples} apples in our basket')

# basket.clear()
# print(basket)


# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# ----------------


# A float, short for "floating-point number," is a data type in programming that represents real numbers (both rational and irrational) with a decimal point. Floats are used to represent numbers that can have fractional parts. In Python, floats are represented using the float data type. For example, 3.14 or 0.5 are float values.

# An integer represents whole numbers without decimal or fractional parts, while a float can represent numbers with decimal or fractional components.


# float_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5 ,5]
# print(float_list)



# sequence = []


# for number in range(1, 5):
#     number = number + 1
#     sequence.append(number)

# print(sequence)


# for number in range(1, 5):
#     number = number + 0.5
#     sequence.append(number)

# print(sequence)

# sequence.sort()
# print(sequence)


# sequence = []

# for number in range(1, 6):
#     float = number + 0.5
#     sequence.extend(number, float)

# sequence = sequence[1:-1]
# print(sequence)



# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
# -------------

# for number in range(1, 22):
#     print(number)


# for number in range(1, 22):
#     if number % 2 == 0:
#         print(number)


numbers = list(range(1, 21))

for num in range(len(numbers)):
    if num % 2 == 0:
        print(numbers[index]) 

# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.


# user_name = ''

# while user_name != 'Samuel': 
#     user_name = input("Please enter your name: ")

# print(f"Hello, {user_name}! You have entered the correct name.")


# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.


# favorite_fruits_user = input("Enter your favorite fruit(s) separated by a space : ")
# favorite_fruits = favorite_fruits_user.split()
# print(favorite_fruits)
# fruit_name = input("Enter the name of any fruit of your choice: ")

# if fruit_name in favorite_fruits:
#     print('“You chose one of your favorite fruits! Enjoy!”')
# else:
#     print('“You chose a new fruit. I hope you enjoy”')


# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

# pizza_price = 10
# toppings = []

# while True:
#     topping = input("Enter a pizza topping (or 'quit' to finish): ")
#     if topping.lower() == 'quit' :
#         break
#     else:
#         toppings.append(topping)
#         pizza_price += 2.5


# print(f'you have {" ".join(toppings)} on your pizza it will cost you {pizza_price} Dollar')




# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.






# price_total = []


# while True:
#     age = input("Enter the age of a family member (or 'quit' to finish): ")
    
#     if age.lower() == "quit":
#         break
    
#     age = int(age)
    
#     if age < 3:
#         ticket_price = 0
#     elif 3 <= age <= 12:
#         ticket_price = 10
#     else:
#         ticket_price = 15
        
#     price_total.append(ticket_price)

# family_price_total = sum(price_total)

# if price_total:
#     print(f"Total cost for the family's tickets: ${family_price_total}")
# else:
#     print("No family members entered.")


# teenagers = ["Alice", "Bob", "Charlie", "David", "Eva"]

# index = 0
# print(len(teenagers))

# while index < len(teenagers):
#     age = int(input(f"Enter the age of {teenagers[index]}: "))
    
#     if 16 <= age <= 21:
#         removed_teenager = teenagers.pop(index)
#         print(f"Sorry, {removed_teenager} is not permitted to watch the movie.")
#     else:
#         index += 1

# print(f'Allowed teenagers to watch the movie: {" ".join(teenagers)}')



# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# finished_sandwiches = []
# index = 0

# print(len(sandwich_orders))

# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_order = sandwich_orders.remove("Pastrami sandwich")


# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop(0)  
#     finished_sandwiches.append(current_sandwich)  
#     print(f"Making {current_sandwich}")


# print("\nList of finished sandwiches:")
# for sandwich in finished_sandwiches:
#     print(f'I made your {sandwich}')


# print(sandwich_orders)

# print(finished_sandwiches)

