import datetime

today = datetime.date.today()
year = today.strftime("%Y")

print(year)

user_birthdate = input('what is your birthdate DD/MM/YYYY')

user_birthdate_year = user_birthdate.split('/')
user_birthdate_year = user_birthdate_year[-1]
print(user_birthdate)
print(user_birthdate_year)

your_age = int(year) - int(user_birthdate_year)
print(f'you are {your_age}')

nombre_de_bougie = your_age % 10


bougies = ''

for x in range(nombre_de_bougie):
    bougies += 'i'



print(f'_____{bougies}_____')
print(' |:H:a:p:p:y:| ')
print("__|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print('~~~~~~~~~~~~~~~~~~~')
