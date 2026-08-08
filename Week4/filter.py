# Syntax:
# filter(function, iterable)

# Example 1 – Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = filter(lambda x: x % 2 == 0, numbers)
print(list(even_num))
# output with map: [False, True, False, True, False, True, False, True, False, True]
# output with filter: [2, 4, 6, 8, 10]

# filter() with None
# If you pass None instead of a function, filter() removes all falsy values.
values = [
    0,
    "",
    None,
    False,
    5,
    "Python",
    [],
    [1, 2]
]
result = filter(None, values)
print(list(result)) # [5, 'Python', [1, 2]]

# Real-World Example 1 – Active Users
users = [
    { "name": "John", "active": True},
    { "name": "Bob", "active": False},
    { "name": "Charlie", "active": False},
    { "name": "Alice", "active": True},
    { "name": "Netaji", "active": True},
]
active_users = filter(lambda u: u['active'], users) # if no condition then it will consider as True
# active_users = filter(lambda u: u['active'] == False, users) # will return active = False users
print(list(active_users))

# Mini Exercise
balances = [500, 1500, 25000, 800, 45000, 12000]
balance_more_than_10k = list(filter(lambda x: x > 10000, balances))
print(balance_more_than_10k)

# Add 5% bonus
balance_with_bonus = map(lambda x: x + (x * 5 / 100), balance_more_than_10k)
print(list(balance_with_bonus))

