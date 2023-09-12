# 🌟 Exercise 1: Currencies
# Instructions


# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     #Your code starts HERE


#     def __str__(self):
#         currency_name = self.currency
#         if self.amount > 1:
#             currency_name += "s"
#         return f"{self.amount} {currency_name}"
    
#     def __int__(self):
#         return self.amount
    
#     def __repr__(self):
#         currency_name = self.currency
#         if self.amount > 1:
#             currency_name += "s"
#         return f"{self.amount} {currency_name}"
    
#     def __add__(self, other):
#         if isinstance(other, Currency) and self.currency == other.currency:
#             return self.amount + other.amount
#         elif isinstance(other, (int, float)):
#             return self.amount + other
        
#     def __iadd__(self, other):
#         if isinstance(other, (int, float)):
#             self.amount += other
#         elif isinstance(other, Currency) and self.currency == other.currency:
#             self.amount += other.amount
#         else:
#             raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#         return self

    
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1)) 
# print(int(c1))
# print(repr(c1))

# print(c1 + 5)  
# print(c1 + c2)  

# print(c1)

# c1 += 5
# print(c1)

# c1 += c2
# print(c1)

# c1 + c3


# 🌟 Exercise 2: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn



# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

# import random
# import string

# def generate_random_string(length):
#     characters = string.ascii_letters  
#     random_string_lst = []
#     for _ in range(length):
#         random_string_lst.append(random.choice(characters))
#         random_string = ''.join(random_string_lst)
#     return random_string

# random_string = generate_random_string(5)
# print(random_string)


# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.


# import datetime

# def display_current_date():
#     current_date = datetime.datetime.now()
#     formatted_date = current_date.strftime("%Y-%m-%d")  
#     print("Current Date:", formatted_date)

# display_current_date()

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

# import datetime

# def time_until_january_1st():
#     current_datetime = datetime.datetime.now()

#     next_year = current_datetime.year + 1
#     target_date = datetime.datetime(next_year, 1, 1)

#     time_left = target_date - current_datetime

#     days = time_left.days
#     seconds = time_left.seconds
#     hours, seconds = divmod(seconds, 3600)
#     minutes, seconds = divmod(seconds, 60)

#     print(f"The 1st of January is in {days} days and {hours}:{minutes}:{seconds} hours.")

# time_until_january_1st()

# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument 
# (in the format of your choice), then displays a message stating how many minutes the user lived in his life.


# import datetime

# def minutes_lived(birthdate):
#     birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")  # Adjust the format as needed
#     current_datetime = datetime.datetime.now()
#     time_difference = current_datetime - birthdate
#     minutes_lived = time_difference.total_seconds() / 60
#     return int(minutes_lived)


# minutes = minutes_lived('1991-03-24')
# print(f"You have lived for {minutes} minutes.")


# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.



