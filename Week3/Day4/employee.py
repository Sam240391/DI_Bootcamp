class Employee :
    def __init__(self, firstname, lastname, age, job, salary, address):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
        self.__address = address


    @property
    def address(self) :
        return self.__address
    
    @address.setter
    def address(self) :
        if self.job == 'Developer':
            self.__address = self.address

    

    def __gt__(self, other):
        return self.salary > other.salary

    def __add__(self, other):
        total_salary = self.salary + other.salary
        return total_salary

    def __str__(self):
        return f"Employee: {self.get_fullname()}, Age: {self.age}, Job: {self.job}, Salary: {self.salary},"



    def get_fullname(self) :
        return f"{self.firstname} {self.lastname}"
    
    def happy_birthday(self):
        self.age += 1
    
    def get_promotion(self, new_promotion) :
        self.salary += new_promotion

    def show_info (self) :
        print(f"{self.get_fullname()} is {self.age} years old, his job is {self.job} and his salary is {self.salary}")
    


# Program should be a function
# that contains a few lists
# list of names, of job, of salary ect...
# create a program that create 10 employees with random information
# and save them into a list
# then call the show_info method for each of them


# --> random age from 18 to 67
# --> random salary from 10000 to 45000

# import random

# lst_names = ["John", "Lea", "Emma", "Josh", "Eli"]
# lst_lastnames = ["Cohen", "Smith", "Doe", "Sevi", "Swtazh"]
# lst_jobs = ["developer", "dancer", "cowboy", "tennis player", "doctor"]

# def programemployee():
#     list_employees = []

#     for _ in range(10):
#         first_name = random.choice(lst_names)
#         last_name = random.choice(lst_lastnames)
#         job = random.choice(lst_jobs)
#         age = random.randint(18, 67)
#         salary = random.randint(10000, 45000)
#         employee = Employee(first_name, last_name, job, age, salary)
#         list_employees.append(employee)

#     for employee in list_employees: 
#        employee.show_info()


# programemployee()


employee1 = Employee("John", "Doe", 30, "Software Engineer", 60000, '2 avenue de paris')
employee2 = Employee("Jane", "Smith", 28, "Data Analyst", 55000, '2 avenue de paris')

# if employee1 > employee2:
#     print(f"{employee1.get_fullname()} has a higher salary.")
# else:
#     print(f"{employee2.get_fullname()} has a higher salary.")

# total_salary = employee1 + employee2
# print(f"The total salary of {employee1.get_fullname()} and {employee2.get_fullname()} is {total_salary}")

print(employee1.address)
print(employee2)


# Exercise

# Using the Employee class add an attribute address  that should be private

# implement a method that return the address of the employee --> getter

# implement a method that modifies the address of the employee, only if his job is developer --> setter 

# Create an object and call all the methods