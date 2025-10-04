class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
            
        self.balance += amount
            
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return True
            
        else:
            return False

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")
