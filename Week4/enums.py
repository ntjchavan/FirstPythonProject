# Enum stands for Enumeration.
# An Enum is a collection of named constant values.

from enum import Enum

class AccountType(Enum):
    SAVING = 1
    CURRENT = 2
    FIXED = 3

print(AccountType.SAVING) # AccountType.SAVING
print(AccountType.CURRENT.value) # 2


for enum in AccountType:
    print(enum.name, enum.value)
# O/p:
# SAVING 1
# CURRENT 2
# FIXED 3

# Mini Exercise
print("------------ Mini Exercise ------------")
def create_account(account_type):
    print(f"Creating {account_type.value} Account")

create_account(AccountType.SAVING)

print("\n")

class TransactionStatus(Enum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"

def print_status(status):
    if status == TransactionStatus.SUCCESS:
        print("Transaction completed")
    else:
        print("Transaction failed")

print_status(TransactionStatus.PENDING)
print_status(TransactionStatus.SUCCESS)
print_status(TransactionStatus.FAILED)
