# An iterable is any object that can be looped over.

# An iterator is an object that returns one value at a time.

# Creating an Iterator
numbers  = [10, 20, 30]

iterator = iter(numbers)

print(iterator) # <list_iterator object at 0x0000021D8E5AABC0>

# numbers is a list.
# iterator is a list iterator.

print(next(iterator)) # 10
print(next(iterator)) # 20
print(next(iterator)) # 30

# Iterator Protocol
# For an object to be an iterator, it must implement:
# __iter__()
# __next__()

class Counter:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 5:
            raise StopIteration

        number = self.current
        self.current += 1
        return number
    
counter = Counter()
for num in counter:
    print(num) # 1 2 3 4 5

print("--------------- Mini Exercise ---------------")
# Task 1 – Transaction Iterator
# Create a custom iterator that returns transaction amounts one by one.

transactions = [5000, -1000, 2500, -500]

iterator_trans = iter(transactions)

print(next(iterator_trans)) # 5000
print(next(iterator_trans)) # -1000

# Task 2 – Account Number Iterator

class AccountNumberIterator:
    def __init__(self, start=1001, end=1005, prefix="ACC"):
        self.start = start
        self.end = end
        self.prefix = prefix

    def __iter__(self):
        self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        account_number = f"{self.prefix}{self.start}"
        self.start+=1
        return account_number

account_tier = AccountNumberIterator()

print(next(account_tier)) # ACC1001
print(next(account_tier)) # ACC1002
print(next(account_tier)) # ACC1003
print(next(account_tier)) # ACC1004
print(next(account_tier)) # ACC1005
print(next(account_tier)) # will throw  raise StopIteration

