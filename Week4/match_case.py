# match / case was introduced in Python 3.10.

# It provides structural pattern matching, which is much more powerful than a simple replacement for if/elif.

command = "deposit"

match command:
    case "deposit":
        print("Deposit selected")

    case "withdraw":
        print("Withdraw selected")

    case "balance":
        print("Balance selected")

    case _:
        print("Unknown command")

# Multiple Values in One Case
command = "exit"

match command:
    case "deposit":
        print("Deposit")

    case "withdraw":
        print("Withdraw")

    case "quit" | "exit":
        print("Exiting")

    case _:
        print("Invalid command")

# Matching Lists
numbers = [1, 2, 3]

match numbers:
    case [1, 2, 3]:
        print("Exactly 1, 2, 3")

    case _:
        print("Something else")

# Capturing Dictionary Values
user = {
    "name": "Bob",
    "role": "Admin"
}

match user:
    case {"name": name, "role": role}:
        print(name)
        print(role)

# Combining Pattern + Condition
transactions = ("withdraw", 11000)

match transactions:
    case ("withdraw", amount) if amount > 10000:
        print("Large withdrawal requires approval")

    case ("withdraw", amount):
        print(f"Withdrawing {amount}")

    case ("deposit", amount):
        print(f"Depositing {amount}")

    case _:
        print("Unknown status")

print("------------------- Practice Exercise Bank Application ------------")

from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"

transaction = (TransactionType.TRANSFER, 10500)

match transaction:
    case (TransactionType.WITHDRAW, amount):
        print(f"Withdraw amount {amount}")

    case (TransactionType.DEPOSIT, amt):
        print(f"Deposited amount {amt}")

    case (TransactionType.TRANSFER, a):
        print(f"Transfer amount {a}")

    case _:
        print("Invalid transaction")

    
# Mini Project Exercise
print("----------- Mini Project Exercise --------------")
transactions = [
    ("withdraw", 5000),
    ("deposit", 8500),
    ("transfer", 3050),
    ("withdraw", 2100)
]

for trans in transactions:
    match trans:
        case ("withdraw", a):
            print(f"Withdrawal {a}")

        case ("deposit", amt):
            print(f"Deposited {amt}")

        case ("transfer", amount):
            print(f"Transfered {amount}")

        case _:
            print("Invalid transactions")

