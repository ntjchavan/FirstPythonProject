# A Context Manager is an object that automatically manages resources.

# It ensures resources are:
# Opened correctly.
# Used safely.
# Closed or cleaned up automatically.

# Why use with instead of manually opening a file?
# -> Because it automatically closes the file, even if an exception occurs.

with open("sample.txt", "w") as file:
    file.write("hello sample")

print(file.closed) # True, becuase with will open file and close itself.

# Above code is similar like below
# file = open("sample.txt")

# try:
#     print(file.read())
# finally:
#     file.close()

# Creating Your First Context Manager
class Demo:
    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

with Demo():
    print("Inside block")
# O/p:
# Entering
# Inside block
# Exiting

# Returning an Object
class Database:
    def __enter__(self):
        print("Connected")
        return self

    def query(self):
        print("Executing Query")

    def __exit__(self, exc_type, exc, tb):
        print("Disconnected")

with Database() as db:
    db.query()


print("------------- Mini Exercise -------------")

# Task 1 - Bank Transaction Context Manager
# Create a context manager with this behavior:
# __enter__() prints:

# Inside the with block, perform a deposit.


class BankTransaction:
    def __enter__(self):
        print("Transaction Started")
        return self

    def deposit(self, amount):
        print(F"Deposited {amount}")

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            print("Transaction Committed")
        else:
            print("Transaction Rolled Back")

with BankTransaction() as trans:
    trans.deposit(5000)

# Task 2 – Logging Context Manager
from contextlib import contextmanager

@contextmanager
def logging_manager():
    print("=== Start Operation ===")

    try:
        yield
    finally:
        print("=== End Operation ===")

with logging_manager():
    print("In-progress")

# O/p:
# === Start Operation ===
# In-progress
# === End Operation ===

