

# 🌟 Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.




# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age



# cat1 = Cat('kitty', 4)
# cat2 = Cat('jumy', 2)
# cat3 = Cat('baby', 7)




# def find_oldest_cat():
#     cats = [cat1, cat2, cat3]
#     oldest_cat = cats[0]
#     for cat in cats:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
#     return oldest_cat


# oldest_cat = find_oldest_cat()
        
# print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")



# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


# class dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height

#     def bark(self):
#         print(f'{self.name} goes woof')


#     def jump(self):
#         x = self.height * 2
#         print(f'{self.name} jumps {x} cm high')



# davids_dog = dog('rex', 50)

# print(f'David"s dog name is {davids_dog.name} and his height is {davids_dog.height} cm')

# davids_dog.bark()
# davids_dog.jump()


# sarahs_dog = dog('Teacup', 20)

# print(f'Sarah"s dog name is {sarahs_dog.name} and his height is {sarahs_dog.height} cm')

# sarahs_dog.bark()
# sarahs_dog.jump()


# def bigger_dog():
#     dogs=[davids_dog, sarahs_dog]
#     bigger_dog = dogs[0]
#     for dog in dogs:
#        if dog.height > bigger_dog.height:
#         bigger_dog = dog 
#     return bigger_dog

# bigg_dog = bigger_dog()

# print(f'the bigger dog is {bigg_dog.name} he"s {bigg_dog.height} cm')




# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


# class song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for element in self.lyrics:
#          print(f'{element}')


# my_fav_song = song(['Hey jude, don"be afraid,', 'don"be afraid'])

# my_fav_song.sing_me_a_song()


# stairway= song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])

# stairway.sing_me_a_song()



# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)


# class zoo:
#     def __init__(self, zoo_name):
#         self.zoo_name = zoo_name
#         self.animals = []

#     def add_animal(self, **new_animals):
#         for new_animal in new_animals:
#             if new_animal not in self.animals:
#                 self.animals.append(new_animal)

#     def get_animals(self):
#         print(self.animals)

#     def sell_animal(self, animal_sold):
#         if animal_sold in self.add_animal:
#             self.animals.remove(animal_sold)
#             print(f"{animal_sold} has been sold from {self.zoo_name}.")
#         else:
#             print(f"{animal_sold} is not in {self.zoo_name}.")

#     def sort_animals(self):
#         animal_groups = {}
#         for animal in self.animals:
#             first_letter = animal[0].lower()
#             if first_letter not in animal_groups:
#                 animal_groups[first_letter] = []
#             animal_groups[first_letter].append(animal)

#         sorted_groups = {}
#         for key, value in sorted(animal_groups.items()):
#             sorted_groups[key] = value

#         print("Sorted and grouped animals:")
#         group_dict = {}
#         group_number = 1
#         for key in sorted_groups:
#             group_dict[group_number] = sorted_groups[key]
#             group_number += 1
        
#         return group_dict

#     def get_groups(self):
#         group_dict = self.sort_animals()
#         print(group_dict)



        

# zoo_paris = zoo('zooparis')
# zoo_paris.add_animal('lion', 'cat', 'dog', 'girafe', 'gorille')


# zoo_paris.get_groups()



class zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = {}

    def add_animal(self, **new_animals):
        print(new_animals)


    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.add_animal:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from {self.zoo_name}.")
        else:
            print(f"{animal_sold} is not in {self.zoo_name}.")

    def sort_animals(self):
        animal_groups = {}
        for animal in self.animals:
            first_letter = animal[0].lower()
            if first_letter not in animal_groups:
                animal_groups[first_letter] = []
            animal_groups[first_letter].append(animal)

        sorted_groups = {}
        for key, value in sorted(animal_groups.items()):
            sorted_groups[key] = value

        print("Sorted and grouped animals:")
        group_dict = {}
        group_number = 1
        for key in sorted_groups:
            group_dict[group_number] = sorted_groups[key]
            group_number += 1
        
        return group_dict

    def get_groups(self):
        group_dict = self.sort_animals()
        print(group_dict)



        

zoo_paris = zoo('zooparis')
zoo_paris.add_animal(lion = 5, cat = 2, gorilla = 4)


zoo_paris.get_groups()