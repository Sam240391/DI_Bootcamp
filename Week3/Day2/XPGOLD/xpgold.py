# Exercise 1: Bank Account
# Instructions
# Part I:

# Create a class called BankAccount that contains the following attributes and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive


class BankAccount():
    def __init__(self, username='', password='', authenticated = False, balance= 0, minimum_balance = 0):
        self.balance = balance
        self.minimum_balance = minimum_balance
        self.username = username
        self.password = password
        self.authenticated = authenticated


    def deposit(self):
        ammount_to_deposit = int(input(f'What is the ammount to deposit'))
        
        if ammount_to_deposit > 0 and self.authenticated == True:
            self.balance +=ammount_to_deposit
        elif self.authenticated == False:
            raise Exception ('you have to be authenticated to make an action on this account')
        else:
            raise Exception ("The ammount should be positive")
        
        print(f'The Ammount {ammount_to_deposit} was deposit to your account, your balance is now : {self.balance}')

    def withdraw(self):
        ammount_to_withdraw = int(input(f'What is the ammount to withdraw'))
        if ammount_to_withdraw > 0 and (self.balance - ammount_to_withdraw) >= self.minimum_balance :
            self.balance -= ammount_to_withdraw
        elif ammount_to_withdraw < 0:
            raise Exception (f"The ammount should be positive")
        else:
            raise Exception (f"The balance connot be lesser than {self.minimum_balance}")

        print(f'The Ammount {ammount_to_withdraw} was withdraw to your account, your balance is now : {self.balance}')


    def authenticate(self):
        username = input(f'What is your username')
        password= input(f'What is your password')
        if username == self.username and password == self.password:
            self.authenticated = True
            print(f' you have succesfully login')
        else:
            print(f'wrong information start again')
            self.authenticate()


my_bank_account = BankAccount('samuel', 'password123')


my_bank_account.authenticate()
print(my_bank_account.authenticated)
my_bank_account.deposit()
my_bank_account.withdraw()
my_bank_account.deposit()


print(my_bank_account.balance)