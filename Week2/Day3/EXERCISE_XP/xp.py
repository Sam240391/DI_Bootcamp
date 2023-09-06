# 🌟 Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# ---------------


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# all = zip(keys, values)

# dict1 = dict(all)

# print(dict1)


# 🌟 Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).


# ---------------

# prices = {
#     'baby' : 0,
#     'child' : 10,
#     'adult': 15,
# }


# family_cost = 0

# family = {}

# while True :
#     name = input("Whats your name ?")
#     if name.lower()  == 'quit' :
#         break
#     age = input("what's your age ? ")
#     family[name] = int(age)


# print(family)

# for name, age in family.items():
#     if age < 3 :
#         family_cost += prices['baby']
#         print(f'{name} has {age} old so he will pay {prices["baby"]} dollars')
#     elif 4 <= age <=12:
#         family_cost += prices['child']
#         print(f'{name} has {age} old so he will pay {prices["child"]} dollars')
#     else :
#         family_cost += prices['adult']
#         print(f'{name} has {age} old so he will pay {prices["adult"]} dollars')


# print(f'the cost for the family will be {family_cost} dollars')





# 🌟 Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

# --------------------

# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?


# zara = {
#     'name': 'Zara',
#     'creation_date': 1975,
#     'creator_name': 'Amancio Ortega Gaona',
#     'type_of_clothes': ['men', 'women', 'children', 'home'],
#     'international_competitors': ['Gap', 'H&M', 'Benetton'],
#     'number_stores': 6000,
#     'major_color': {
#         'France': 'blue',
#         'Spain': 'red',
#         'US': ('pink', 'green')}
# }


# print(zara['major_color'].items())

# client = zara['type_of_clothes']
# client.pop(-1)
# print(client)

# print(f"Zara was created in {zara['creation_date']} by {zara['creator_name']} there major clients are , {' and '.join(client)}")

# zara['country_creation'] = 'Spain'

# print(zara)

# if 'international_competitors' in zara:
#     zara['international_competitors'].append('Desigual')

# print(zara)

# del zara['creation_date']

# print(zara)


# print(f"The last international competitor is: {zara['international_competitors'][-1]}")

# print(f"The major clothes colors in the US are {' and '.join(zara['major_color']['US'])}")


# print("The number of key-value pairs in the dictionary is:", len(zara))


# print("Keys in the dictionary:", zara.keys())


# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000,
# }

# zara.update(more_on_zara)

# print("The value of the key 'number_stores' is:", zara['number_stores'])



#  the value has been updated


# ---------------
# Exercise 4 : Disney Characters
# Instructions
# Use this list :
# -----------

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.




users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_user_A = {}

for i in range(len(users)):
    disney_user_A[users[i]] = i

print(disney_user_A)


disney_user_B = {}

for i in range(len(users)):
    disney_user_B[i] = users[i]

print(disney_user_B)


list_order_alpha_key = list(disney_user_A.keys())
list_order_alpha_value = list(disney_user_A.values())
print(list_order_alpha_key)
print(list_order_alpha_value)
list_order_alpha_key.sort()
print(list_order_alpha_key)


disney_users_C = dict(zip(list_order_alpha_key, list_order_alpha_value))


print(disney_users_C)




users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_user_A = {}

# first way to fo that with len

# for i in range(len(users)):
#     if "i" in users[i]:
#        disney_user_A[users[i]] = i
    

# print(disney_user_A)

# another way with startwith
 

for i, name in enumerate(users):
    if name.startswith(('M' , 'P')):
       disney_user_A.update({name:i})
    
print(disney_user_A)