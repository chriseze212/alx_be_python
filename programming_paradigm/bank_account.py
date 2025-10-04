class BankAccount:
    """A simple bank account class.

    Attributes:
        account_balance (float): current balance of the account.
    """

    def __init__(self, initial_balance=0):
        # initialize account_balance attribute (default 0)
        try:
            self.account_balance = float(initial_balance)
        except (TypeError, ValueError):
            raise ValueError("initial_balance must be a number")

    def deposit(self, amount):
        """Add amount to the account balance.

        Raises ValueError for non-positive or non-numeric amounts.
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Deposit amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.account_balance += amount

    def withdraw(self, amount):
        """Attempt to withdraw amount from the account.

        Returns True if the withdrawal succeeded, False otherwise (insufficient funds
        or non-positive amount). Does not modify balance on failure.
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return False
        if amount <= 0:
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        # always show two decimal places to match expected currency format
        print(f"Current Balance: ${self.account_balance:.2f}")
