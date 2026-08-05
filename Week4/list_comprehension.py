# A List Comprehension is a concise way to create a new list from an existing iterable.
# A concise way to create a new list by iterating over an iterable and optionally filtering or transforming elements.

# Syntax:
# [expression for item in iterable]

# with if condition
# [expression for item in iterable if condition]

# with if else condition
# [
#     expression_if_true
#     if condition
#     else expression_if_false
#     for item in iterable
# ]

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# you can write like below
square_comprehension = [number ** 2 for number in numbers]
print(square_comprehension)

# List Comprehension with if
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [even for even in numbers if even % 2 == 0]
print(even_numbers)

# List Comprehension with if else
odd_even = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(odd_even)

# Real-World Example 2 – Active Employees
employees = [
    {"name": "John", "active": True},
    {"name": "Alice", "active": False},
    {"name": "Bob", "active": True}
]
active_employees = [emp['name'] for emp in employees if emp['active']]
print(active_employees) # ['John', 'Bob']

# Mini Exercise
accounts = [
    {"name": "Amit", "balance": 5000},
    {"name": "Neha", "balance": 15000},
    {"name": "Raj", "balance": 30000},
    {"name": "Pooja", "balance": 8000}
]

# 1 Create a list of customer names with balances greater than or equal to ₹10,000.
higher_balances = [acc['name'] for acc in accounts if acc['balance'] >= 10000]
print(higher_balances)

# 2 Create a new list where every balance has 5% interest added.
balances_5percent_interest = [acc['balance'] + (acc['balance'] * 5 / 100)  for acc in accounts]
print(balances_5percent_interest)

