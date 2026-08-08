# yield is a keyword used inside a function to make it a generator function.

# yield is a keyword that turns a function into a generator function. 
# It returns a value and pauses execution until the next value is requested.

# Counting
def count():
    yield 1
    yield 2
    yield 3

print(list(count())) # [1, 2, 3], this is not correct way to read values, just fo testing purpose

for cnt in count():
    print(cnt) # 1 2 3 each in new line

# Even Numbers
def EvenNumbers(limit):
    for even in range(limit):
        if even % 2 == 0:
            yield even

for value in EvenNumbers(10):
    print(value) # 0 2 4 6 8

print("------------ Mini Exercise ----------------")
transactions = [
    5000,
    -1000,
    2000,
    -500,
    7000
]

# 1 Create a generator function that yields one transaction at a time.
def transaction_generator():
    for trans in transactions:
        yield trans

for amount in transaction_generator():
    print(amount)

# 2 Create a generator function that yields one transaction at a time.
def positive_trans_generator():
    for trans in transactions:
        if trans > 0:
            yield trans

for amount in positive_trans_generator():
    print(amount)


