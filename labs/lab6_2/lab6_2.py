class BankAccount:
    # The constructor
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner


peters_account = BankAccount("Nik", 100.0)

print(peters_account.owner)
print(peters_account.balance)
