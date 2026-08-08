# A closure is an inner function that remembers and can access variables from its enclosing (outer) function, 
# even after the outer function has finished executing.

# Outer Function Starts
#         │
#         ▼
# Creates Variable
#         │
#         ▼
# Creates Inner Function
#         │
#         ▼
# Returns Inner Function
#         │
#         ▼
# Outer Function Ends
#         │
#         ▼
# Inner Function STILL remembers the variable of Outer function

def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner

greet = outer()

greet()

print("----------- Another Example --------------")
def multiplier(number):

    def multiply(value):
        return number * value

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10)) # 20
print(triple(10)) # 30

print("------------- Real-World Example 1 Bank Account ------------------")
def bank_account(balance):

    def deposit(amount):
        nonlocal balance

        balance += amount

        return balance

    return deposit

account = bank_account(1000)

print(account(500)) # 1500
print(account(200)) # 1700
print(account(100)) # 1800

print("------------------------ Mini Exercise ---------------------")
# Task 1 Withdrawal Closure:
# Create a function that returns a withdraw() function.

def create_account(balance):
    def withdraw(amount):
        nonlocal balance

        if amount > balance:
            return "Insufficient balance"

        balance -= amount

        return balance

    return withdraw

account = create_account(5000)

print(account(1000))
print(account(500))
print(account(4000))

