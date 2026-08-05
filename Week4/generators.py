# A Generator is a special type of iterator that produces values one at a time, only when needed, 
# instead of creating all values at once.
# A generator doesn't produce everything immediately.
# First Generator Example
# List comprehensive
numbers = [x for x in range(5)]
print(numbers) # [0, 1, 2, 3, 4]

# Using generator
# A generator doesn't produce everything immediately.
numbers = (x for x in range(5))
print(next(numbers)) # 0
print(next(numbers)) # 1
print(next(numbers)) # 2
print(next(numbers)) # 3

# Even numbers
even = (x for x in range(20) if x % 2 == 0)

for e in even:
    print(e) # will print event numbers lik 2, 4, 6 ... 18

# Consuming a Generator
num = (x for x in range(3))
print(list(num)) # [0, 1, 2]

print("-------------- Mini Exercise ---------------")
transactions = [
    5000,
    -1200,
    2500,
    -500,
    8000,
    -300
]
# 1 Create a generator expression that produces only deposit amounts (positive values).
positive_trans = (trans for trans in transactions if trans > 0)
print(list(positive_trans)) # [5000, 2500, 8000]

# Create another generator that adds 2% cashback to every deposit.

trans_2percent_cashback = (trans + (trans * 2 / 100) for trans in transactions if trans > 0)
print(list(trans_2percent_cashback))


