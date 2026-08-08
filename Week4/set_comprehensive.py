# A Set Comprehension is a concise way to create a set from an iterable.
# The order may vary because sets are unordered

# Syntax:
# Basic
# {expression for item in iterable}
# With a condition
# {expression for item in iterable if condition}

numbers = [1, 2, 3, 4]

square = {num ** 2 for num in numbers}

print(square) # {16, 1, 4, 9}

# Remove Duplicate Names
names = ["Netaji", "Alice", "Bob", "Alice"]
unique_name = {name for name in names}
print(unique_name) # {'Bob', 'Netaji', 'Alice'}

# Set Comprehension with if
numbers = [1, 2, 2, 3, 4, 5, 6]

even_num = {num for num in numbers if num % 2 == 0}
print(even_num) # {2, 4, 6}

# Unique Email Domains
emails = [
    "john@gmail.com",
    "alice@yahoo.com",
    "bob@gmail.com",
    "raj@outlook.com"
]
unique_domains = {email.split("@")[1] for email in emails}
print(unique_domains)

print("------------ Mini Exercise --------------")
transactions = [
    {"account": "ACC101", "type": "Deposit"},
    {"account": "ACC102", "type": "Withdrawal"},
    {"account": "ACC103", "type": "Deposit"},
    {"account": "ACC104", "type": "Transfer"},
    {"account": "ACC105", "type": "Withdrawal"}
]

# Create a set containing all unique transaction types.
unique_trans = {trans["type"] for trans in transactions}
print(unique_trans) # {'Transfer', 'Withdrawal', 'Deposit'}

customer_ids = [
    101,
    102,
    103,
    101,
    104,
    102,
    105
]
uni_cust_id = {id for id in customer_ids}
print(uni_cust_id)


