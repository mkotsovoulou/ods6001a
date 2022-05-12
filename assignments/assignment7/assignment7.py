# THE BANK ACCOUNT CLASS
class BankAccount:
    annual_interest = 0.02

    # The constructor
    def __init__(self, owner: str, balance: float):
        self.balance = balance
        self.owner = owner

    # create below another constructor with just an owner name and zero balance
    


    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    # Create an add_interest method which will increase the balance by application of the annual interest class variable 
    def add_interest(self):
        pass

    def __str__(self):
        return f"BankAccount Owner: {self.owner}, Balance: {self.balance}"


# MAIN PROGRAM
nik_account = BankAccount("Nik")
nik_account.deposit(100)
nik_account.withdraw(44)

# Modify the annual interest to 3%

# Call the add interest method on nik account

# Print nik account balance



