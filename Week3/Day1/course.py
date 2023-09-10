# add comments in the play function

class Dog :
    # WE INITIALIZE THE CLASS DOG
    def __init__(self, dog_name, dog_age, dog_color = "black", dog_energy = 100) :
        self.name = dog_name
        self.age = dog_age
        self.color = dog_color
        self.energy = dog_energy

    # method happybirthday increment the age by one
    def happy_birthday(self) :
        self.age += 1

    def show_info (self) :
        print(f"The dog name is {self.name}, his age is {self.age}, he is of color {self.color}")

    def go_to_groomer(self, owner_color) :
        self.color = owner_color


    # FUNCTION THAT MAKES THE DOG PLAYS

    def play (self, activity) :
        # WE CREATE A CONDITION IF THE DOG HAS ENOUGH ENERGY TO PLAY ACTIVITY
        if self.energy >= 10:
            # IF ENERGY BIGGER THAN 10 SO THE DOG CAN PLAYS WITH THE BALL 
            if self.energy >= 10 and activity == "ball" :
                self.energy -= 10
                print(f"{self.name} is playing ball - he has {self.energy} energy left")
            # IF ENERGY BIGGER THAN 30  SO THE DOG CAN PLAYS WITH THE FRISBEE 
            elif self.energy >= 30 and activity == "frisbee":
                self.energy -= 30
                print(f"{self.name} is playing frisbee - he has {self.energy} energy left")
                # IF ENERGY BIGGER THAN 70  SO THE DOG CAN PLAYS WITH ANOTHER DOG 
            elif self.energy >= 70 and activity.energy >= 70 and isinstance(activity, Dog) :
                self.energy -= 70 #lea_dog energy
                activity.energy -= 70 #activity is dan_dog
                print(f"{self.name} and {activity.name} are playing together - {self.name} has {self.energy} energy left - - {activity.name} has {activity.energy} energy left")
            else :
                print(f"You have {self.energy} left - You don't have enough energy to play {activity} \n")
                self.play(input("Please choose another activity between ball, frisbee and play date \n"))
        else :
            self.sleep()
    
    def sleep (self) :
        self.energy = 100
        print(f"{self.name} slept, he has {self.energy} energy")

lea_dog = Dog("Spock", 2)
dan_dog = Dog("Rex", 4, "white")
lea_dog.play(dan_dog)






class Employee :
    # WE INITIALIZE THE CLASS EMPLOYEE
    def __init__(self, employee_firstname, employee_lastname, employee_age, employee_job, employee_salary) :
        self.firstname = employee_firstname
        self.lastname = employee_lastname
        self.age = employee_age
        self.job = employee_job
        self.salary = employee_salary


    def get_fullname(self):
        print(f'{self.firstname} {self.lastname}')

    def happy_birthday(self):
        self.age =+ 1

    def get_promotion(self, promotion_amount):
        self.salary =+ promotion_amount

    def show_info (self) :
        print(f"The Employye name is {self.firstname} {self.lastname}, {self.firstname} is {self.age} old, {self.firstname} is {self.job} and {self.firstname} won {self.salary} Shekel / month")

    

employee1 = Employee('David', 'Schartz', 20, 'project manager', 20000)
employee2 = Employee('Lea', 'Smith', 30, 'developper', 25000)

employee1.show_info()




