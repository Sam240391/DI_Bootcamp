# Instructions
# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

# user_word = input('whats your word \n ')

# print(user_word)

# list_letter = {}

# for index, letter in enumerate(user_word):
#     if letter in list_letter:
#         list_letter[letter].append(index)
#     else:    
#         list_letter[letter] = [index]

# print(list_letter)


# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Examples

# The key is the product, the value is the price

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# ➞ ["Bread", "Fertilizer", "Water"]

# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 

# ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1" 

# ➞ "Nothing"



# items_purchase = {
#   "Water": 1,
#   "Bread": 3,
#   "TV": 1000,
#   "Fertilizer": 20
# }

# wallet = 0


# items_i_can_buy = []

# for keys, value in items_purchase.items():
#     if value <= wallet:
#         items_i_can_buy.append(keys)

# items_i_can_buy.sort()

# if items_i_can_buy:
#     print(items_i_can_buy)
# else:
#     print("Nothing")






