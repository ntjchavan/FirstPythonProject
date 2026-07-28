from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int
    salary: float

employee = Employee("Netaji", 35, 56000)
print(employee) # Employee(name='Netaji', age=35, salary=56000)

# default values
@dataclass
class Student:
    name: str
    makrs: int
    age: int = 25 # default values


# Frozen Dataclasses (Immutable Objects)
@dataclass(frozen=True)
class Bank:
    name: str
    balance: float

bank = Bank("Alice", 24000)
print(bank)

# this becomes Immutable because of frozen = True
# bank.balance = 25000 # Error FrozenInstanceError

# Using field()
print("--------- Using field() ----------")
@dataclass
class BookTests:
    author_name: str
    book_list: list = field(default_factory=list)

books = BookTests("Shiv Prasad")
books.book_list.append(".Net")
books.book_list.append("C#")

print(books) # Books(author_name='Shiv Prasad', book_list=['.Net', 'C#'])

print("------------- Practice Exercise --------------")

@dataclass
class Book:
    title: str
    author: str
    price: float
    stock: int = 0

    def total_value(self):
        return self.price * self.stock

book = Book("Python basics", "Bob", 120.1, 5)

print(book)
print(book.total_value())


