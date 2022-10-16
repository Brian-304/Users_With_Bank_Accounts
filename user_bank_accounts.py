class User: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def deposit(self, amount):
        self.account.make_deposit(amount)
        return self

class BankAccount:		
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def yield_interest(self):
        self.account_balance *= (self.int_rate + 1)
        return self
    def display_account_info(self):
        print("\n Net Available Balance=", self.account_balance)
        return " "


brian = User("Brian", "Tabios")
monty = User("Monty", "Python")


monty.deposit(100)
monty.deposit(200)
# monty.yield_interest()


brian.deposit(100)
brian.deposit(500)
# brian.yield_interest()

print(brian.first_name, brian.last_name, brian.account.display_account_info()) 
print(monty.first_name, monty.last_name, monty.account.display_account_info())











    

