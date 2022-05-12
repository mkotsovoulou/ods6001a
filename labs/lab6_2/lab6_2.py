# THE BANK ACCOUNT CLASS
class BankAccount:
    # The constructor
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

    # create here the deposit method 

    # create here the withdraw method 

    # create here the __str__ method


# MAIN PROGRAM
nik_account = BankAccount("Nik", 100.0)

print("Owner: ", nik_account.owner)
print("Balance:", nik_account.balance)
