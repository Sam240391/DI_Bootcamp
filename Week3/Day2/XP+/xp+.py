# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]


# 2. Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.


class Family:
    def __init__(self,last_name):
        self.last_name = last_name
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
         ]

    def born(self , **new_member, ):
        self.members.append(new_member)
        print(f'Congratulation Family {self.last_name} ')

    def is_18 (self, name):
        for member in self.members:
            if member['name'] == name and member['age'] > 18:
                return True 
            else:
                return False
            
    def family_presentation(self):
        family_name = []
        for member in self.members:
            family_name.append(member['name'])
        print(f'Last name"s Family : {self.last_name}, The member of the family are : {", ".join(family_name[0:-1])} and {family_name[-1]}')

    

# family_chemla = Family('Chemla')

# print(family_chemla.__dict__)

# family_chemla.born(name = 'David', age = 0, gender = 'Male', is_child = True)

# print(family_chemla.__dict__)

# print(family_chemla.is_18('David'))

# family_chemla.family_presentation()



# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.

# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# Add a method called incredible_presentation which :

# Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method)
# Prints all the members’ incredible name and power.

# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.


class TheIncredible(Family):
    def __init__(self,last_name):
        super().__init__(last_name)

        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
        ]
            
    def use_power(self, member_name):
        for member in self.members:
            if member['name'].lower() == member_name:
                if member['age'] >= 18:
                    print(f"{member_name}'s power is {member['power']}.")
                else:
                    raise ValueError(f"{member_name} is not over 18 years old and cannot use their power.")


    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
            try:
              print(f"{member['incredible_name']} ({member['name']}): {member['power']}")
            except:
             print (f"({member['name']}): {member['power']}")


family_amazing = TheIncredible('Amazing')
family_amazing.use_power('sarah')
family_amazing.incredible_presentation()
family_amazing.born(name='Jack', age=0, gender='Male', power='Unknown Power')
family_amazing.incredible_presentation()




