# reduce() → combines all elements into one final value.
# reduce() repeatedly applies a function to the elements of an iterable until only one value remains.
# Syntax:
# reduce(function, iterable)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)

print(total) # 15

# parameters:
# x = accumulated value
# y = current element

# In backend
# Numbers:
# [1, 2, 3, 4]

# Step 1:
# 1 + 2 = 3

# Step 2:
# 3 + 3 = 6

# Step 3:
# 6 + 4 = 10

# Step 4:
# 10 + 5 = 15

# Final Result:
# 15

# Example – Find Maximum
numbers = [3, 6, 2, 9, 7, 6]

max_num = reduce(lambda x, y: x if x > y else y, numbers)

print(max_num)

# Example – Join Strings
words = [
    "hello",
    "welcome",
    "how are you"
]
sentence = reduce(lambda x, y: x + ", " + y, words)

print(sentence)

# With an initial value:
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers, 10)
print(result) # 25

# behind the schene
# Start = 10
# 10 + 1 = 11
# 11 + 2 = 13
# 13 + 3 = 16
# 16 + 4 = 20
# 20 + 5 = 25

# Mini Exercise
transactions = [
    5000,
    -1200,
    2500,
    -300,
    1000,
    -500
]
# 1 Uses filter() to keep only deposits (positive amounts).
positive_deposits = list(filter(lambda x: x > 0, transactions))
print(positive_deposits) # [5000, 2500, 1000]

# 2 Uses map() to add a 2% cashback to each deposit.
cashback = list(map(lambda x: x + (x * 2 / 100), positive_deposits))
print(cashback)

# 3 Uses reduce() to calculate the total credited amount.
total_credit = reduce(lambda x, y: x + y, cashback, 0)
print(total_credit)