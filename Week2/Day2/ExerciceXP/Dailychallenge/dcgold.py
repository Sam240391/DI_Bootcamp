# Ask the user for their birthdate in the format DD/MM/YYYY
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

# Extract the year from the birthdate
year = int(birthdate[-4:])

# Determine if it's a leap year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Extract the last digit of the user's age to determine the number of candles
age = int(input("Enter your age: "))
last_digit_of_age = age % 10

# Define the cake and candles
cake = """
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

candles = "i" * last_digit_of_age

# Display the cake with candles
if is_leap_year:
    print(cake)
    print("|" + candles + " " + candles + "  |")
    print("|" + candles + " " + candles + "  |")
    print("|" + candles + " " + candles + "  |")
else:
    print(cake)
    print("|" + candles + " " + candles + " " + candles + "|")