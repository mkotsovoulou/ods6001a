# THE BANK ACCOUNT CLASS
class BankAccount:
    #This is a class variable, common for all instances.
    annual_interest = 0.02

    # The constructor (if called with just a name the balance will be 0)
    def __init__(self, owner: str, balance: float = 0.0):
        self.balance = balance
        self.owner = owner

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
BankAccounts = []

# Open accounts.txt 
fhand = open('accounts.txt', 'r')

# For each line in accounts.txt 
#   Split using the comma and strip the empty characters
#   Create a BankAccount object with the owner and balance in the line
#   and add it in the BankAccounts list


# Modify the annual interest (class variable) to 3%

# Call the add interest method on all Bank Accounts

# Calculate the sum of all balances in the list and print it



