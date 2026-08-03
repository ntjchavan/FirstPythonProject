# Syntax
# map(function, iterable)
# function -> Function to apply to each item.
# iterable -> List, tuple, set, etc.

numbers = [1, 2, 3, 4, 5]

squares = []
for num in numbers:
    squares.append(num * num)

print(squares)

# Instead of above code, you can write like below

squares_map = map(lambda num: num * num, numbers)

print(list(squares_map))

# Convert to upper case
names = ["Bob", "Netaji", "Alice"]
names_upper_case = map(lambda name: name.upper(), names)
print(list(names_upper_case))

# String Length of each words
print(list(map(len, names))) # [3, 6, 5]

# Mapping Multiple Iterables
num1 = [1, 2, 3]
num2 = [10, 20, 30]

result = map(lambda x, y: x * y, num1, num2)
print(list(result)) # [10, 40, 90]

# Unequal Length Iterables
num2 = [10, 20, 30, 40]
result = map(lambda x, y: x * y, num1, num2)
print(list(result)) # [10, 40, 90] - map() stops when the shortest iterable is exhausted.


# Important: Iterators Are Consumed
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result)) # [2, 4, 6, 8, 10]
print(list(result)) # []

# A map object is an iterator. Once you've gone through it, it's exhausted. 
# If you need the values again, either recreate the map object or store the result in a list.
numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))

print(result) # [2, 4, 6]
print(result) # [2, 4, 6]

# Mini Exercise
balance = [1000, 2500, 3000, 5000, 10000]
result = map(lambda x: x + ( x * 5 / 100), balance)
print(list(result))

