# A decorator is a function that takes another function as input, adds some extra behavior, and returns a new function.

# Functions are First-Class Objects
def greet():
    print("Hello")

say_hello = greet
say_hello()

# Passing a Function as an Argument
def greet():
    print("hello, how are you?")

def exec(fun):
    fun()

exec(greet)

# Returning a Function
def outer():
    def inner():
        print("Inner function executed")

    return inner

result = outer()
result()

# Real-World Example 1 – Login Required
logged_id = True
def login_required(func):

    def wrapper():
        if not logged_id:
            print("Access denied")
            return

        func()

    return wrapper

@login_required
def view_balance():
    print("balance 50k")

view_balance()

# Real-World Example 2 – Bank Transaction Logging - Decorators with Parameters
def log_transaction(func):
    def wrapper(*args, **kwargs):
        print("Transaction Started!")

        result = func(*args, *kwargs)

        print("Transaction Completed")

        return result

    return wrapper

@log_transaction
def deposit(amount):
    print(f"Deposited: {amount}")

deposit(10000)

# Real-World Example 3 – Authorization
role = 'admin'
def admin_only(func):

    def wrapper():
        if role != 'admin':
            print("Permission denied!")
            return

        func()

    return wrapper

@admin_only
def delete_account():
    print("Account Deleted")

delete_account() # Permission denied!, becuase role is admin else Account Deleted message will print

print("--------------- Mini Exercise -----------------")

# Task 1:
# Write a decorator that logs:
# Transaction started
# Transaction completed

def deposit_transaction(func):

    def wrapper(*args, **kwargs):
        print("Transaction started!")

        result = func(*args, **kwargs)

        print("Transaction completed!")

        return result

    return wrapper

@deposit_transaction
def deposit(account, amount):
    print(f"Deposited ₹{amount} into Account {account}")


deposit('Acc-01', 5000)