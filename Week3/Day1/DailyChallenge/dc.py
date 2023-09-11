
class Farm:
        def __init__(self, farm_name):
            self.name = farm_name
            self.animals = {}

        def add_animal(self, new_animal, x = 1):
                if new_animal not in self.animals:
                    self.animals[new_animal] = x
                else:
                    self.animals[new_animal] += x

        def get_info(self):
            info =f'{self.name}"s farm \n \n' 
            for key, values in self.animals.items():
                info += f'{key} : {values} \n'
            info += f'\n \n   E-I-E-I-O'
            return info
        

        def get_animal_types(self):
            animal_types = []
            for key, values in self.animals.items():
                animal_types.append(key)
                animal_types = sorted(animal_types)
            return animal_types
        
        def get_short_info(self):
             list_animal = self.get_animal_types()
             animals = ", ".join(list_animal[0:-1])
             sentence = print(f'{self.name}"s farm has {animals}s and {list_animal[-1]}')
             return sentence


         
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print(macdonald.get_animal_types())

macdonald.get_short_info()