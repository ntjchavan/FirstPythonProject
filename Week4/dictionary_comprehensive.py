# A concise way to create or transform dictionaries using a single expression.
# Syntax
# Basic
# {key: value for item in iterable}
# With condition
# {key: value for item in iterable if condition}

# squares
numbers = [1, 2, 3, 4, 5]

result = {
    number: number ** 2 for number in numbers
}

print(result) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Word → Length
languages = ["Python", "Java", "DotNet"]

result = {word: len(word) for word in languages}

print(result) # {'Python': 6, 'Java': 4, 'DotNet': 6}

# Dictionary Comprehension with if
# Suppose we only want students who scored at least 60.
marks = {
    "Jonh": 65,
    "Bob": 82,
    "Charlie": 55,
    "Alice": 83
}

result = {name: mark for name, mark in marks.items() if mark >= 60 }

print(result) # {'Jonh': 65, 'Bob': 82, 'Alice': 83}

# Using if-else
# Suppose we want to assign grades.

grades = {name: "Pass" if mark >= 60 else "Fail" for name, mark in marks.items()}

print(grades)
{'Jonh': 'Pass', 'Bob': 'Pass', 'Charlie': 'Fail', 'Alice': 'Pass'}

# Creating a Dictionary from Two Lists
names = ["Netaji", "John", "Bob"]
ages = [23, 25, 28]

people = {name: age for name, age in zip(names, ages)}

print(people) # {'Netaji': 23, 'John': 25, 'Bob': 28}

# Mini Exercise
print("--------------- Mini Exercise -------------------")
accounts = {
    "ACC101": 12000,
    "ACC102": 8000,
    "ACC103": 25000,
    "ACC104": 5000
}

# 1. Create a new dictionary where every account balance includes 5% interest.
account_with_5per_interest = {name: amount + (amount * 5 / 100) for name, amount in accounts.items()}

print(account_with_5per_interest) # {'ACC101': 12600.0, 'ACC102': 8400.0, 'ACC103': 26250.0, 'ACC104': 5250.0}

# 2. Create another dictionary containing only premium accounts, defined as balances of ₹10,000 or more.
balances_more_than_10k = {name: amount for name, amount in accounts.items() if amount > 10000}

print(balances_more_than_10k) # {'ACC101': 12000, 'ACC103': 25000}





