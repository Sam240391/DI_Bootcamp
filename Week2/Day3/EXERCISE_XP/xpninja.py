# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

my_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
my_list = my_string.split(', ')

print(my_list)

print(f' We have {len(my_list)} manufacturers in the list')

print(f' {sorted(my_list, reverse=True)}')


list_with_o = [name for name in my_list if 'o' in name]
print(list_with_o)

# Find out how many manufacturers’ names have the letter ‘o’ in them.

print(len(list_with_o))

list_without_i = [name for name in my_list if 'i' not in name]
print(list_without_i)
