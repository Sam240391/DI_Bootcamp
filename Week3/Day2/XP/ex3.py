from dogcls import Dog 
import random



class PetDog(Dog):

    def __init__(self, name, age, weight,trained = False) :
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        super().bark()
        self.trained = True

    def play(self, *dog_names):

        dog_names_str = ", ".join(dog_names)
        print(f"{self.name} and {dog_names_str} all play together.")

    def do_a_trick(self):
        list_training = ['does a barrel roll','stands on his back legs','shakes your hand','plays dead']
        if self.trained == True:
            choice = random.choice(list_training)
            print(f'{self.name} {choice}')
        else:
            print(f'{self.name} is not trained')



my_dog = PetDog('Rex', 5, 22)
john_dog = PetDog('medor', 4, 36)
david_dog = PetDog('dede', 2, 12)
lea_dog = PetDog('kitty', 7, 18)

my_dog.play('medor', 'dede')

my_dog.do_a_trick()
my_dog.train()
my_dog.do_a_trick()
