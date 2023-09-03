
print("Exercise 1")

Number_miles = int(input('How much Miles you made: '))

Number_kilometer = Number_miles*1.609


print(f"Hello, you made {Number_kilometer} Kilometers ")


print('exercise2')

name = input("What your name")


if len(name) > 20:
    print(f"Name '{name}' is more than 20 chars long")
    length_description = 'long'
elif len(name) > 15:
    print(f"Name '{name}' is more than 15 chars long")
    length_description = 'semi long'
elif len(name) > 10:
    print(f"Name '{name}' is more than 10 chars long")
    length_description = 'semi long'
elif len(name) == 8 or  len(name) == 9 or len(name)  == 10:
    print(f"Name '{name}' is 8, 9 or 10 20 chars long")
    length_description = 'semi short'
else:
    print(f"Name '{name}' is a short name")
    length_description = 'short'


print('exercise3')

Number_of_invites = int(input('How much invite you have : '))


if Number_of_invites < 50:
    print(f" it must cost $4,000 dollars.")
elif Number_of_invites < 100:
    print(f"it must cost $10,000 dollars.")
elif Number_of_invites < 200:
    print(f"it must cost $10,000 dollars.")
else:
    print(f"it must cost $20,000 dollars.")