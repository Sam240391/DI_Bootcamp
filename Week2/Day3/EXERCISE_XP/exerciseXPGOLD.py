# Exercise 1: Birthday Look-Up
# Instructions
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# Ask the user to give you a person’s name and store the answer in a variable.
# Get the birthday of the name provided by the user.
# Print out the birthday with a nicely-formatted message.


# birthdays = {
#     'Rick':'1992/03/12',
#     'John':'1998/06/05',
#     'Lea':'1987/04/15',
#     'David':'1985/11/24',
#     'Sarah':'1990/01/30',
# }

# print(f'{birthdays}')

# print(f'“You can look up the birthdays of the people in the list!”')

# user_input = input(f'give me a person"s name')

# if user_input in birthdays:
#     birthday = birthdays[user_input]
#     print(f"The birthday of {user_input} is {birthday}.")
# else:
#     print(f"Sorry, {user_input}'s birthday is not in the list.")


#     Exercise 2: Birthdays Advanced
# Instructions
# Before asking the user to input a person’s name print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)


# birthdays = {
#     'Rick':'1992/03/12',
#     'John':'1998/06/05',
#     'Lea':'1987/04/15',
#     'David':'1985/11/24',
#     'Sarah':'1990/01/30',
# }

# for name, birthday in birthdays.items():
#     print(f'{name}')

# print(f'“You can look up the birthdays of the people in the list!”')
# user_input = input(f'give me a person"s name')
# if user_input  not in birthdays:
#     print(f'Sorry, we don’t have the birthday information for {user_input}')
# else:
#     print(f'{user_input} : {birthdays[user_input]}')

# Exercise 3: Add Your Own Birthday
# Instructions
# Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.


# birthdays = {
#     'Rick':'1992/03/12',
#     'John':'1998/06/05',
#     'Lea':'1987/04/15',
#     'David':'1985/11/24',
#     'Sarah':'1990/01/30',
# }

# user_name = input(f'What is your name')
# user_birthday = input(f'What is your birthday : as YYYY/MM/DD')

# birthdays[user_name] = user_birthday


# print(birthdays)


# Exercise 4: Fruit Shop
# Instructions
# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
# Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
# items = {
#     "banana": {"price": 4 , "stock":10},
#     "apple": {"price": 2, "stock":5},
#     "orange": {"price": 1.5 , "stock":24},
#     "pear": {"price": 3 , "stock":1}
# }


# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# for key, value in items.items():
#     print(f'The price of {key} is {value}')


# items = {
#     "banana": {"price": 4 , "stock":10},
#     "apple": {"price": 2, "stock":5},
#     "orange": {"price": 1.5 , "stock":24},
#     "pear": {"price": 3 , "stock":1}
# }

# total_cost = 0

# for key, value in items.items():
#     cost_key = value['price'] * value['stock']
#     total_cost += cost_key

# print(f'{total_cost}')

