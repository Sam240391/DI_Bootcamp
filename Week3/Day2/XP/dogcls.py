class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
         print(f"{self.name} is barking. WOUF WOUF!! ")

    def run_speed(self):
        run_speed = self.weight/self.age*10
        return run_speed
        
    def fight(self, other_dog):
        self.speed = self.run_speed()*self.weight
        other_dog_speed = other_dog.run_speed() * other_dog.weight
        if self.speed > other_dog_speed:
            print(f"{self.name} won the fight against {other_dog.name}")
        elif self.speed < other_dog_speed:
            print(f"{other_dog.name} won the fight against {self.name}")
        else:
            print("It's a draw; neither dog won the fight.") 