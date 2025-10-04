import sys
from bank_account import BankAccount


def main():
    # start with an example balance of 100; user can change this if desired
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            # print without trailing zeros when not needed
            if float(amount).is_integer():
                print(f"Deposited: ${int(amount)}")
            else:
                print(f"Deposited: ${amount}")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            if float(amount).is_integer():
                print(f"Withdrew: ${int(amount)}")
            else:
                print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
