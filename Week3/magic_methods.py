
class Student:
    def __init__(self, name):
        self.name = name

    # def __str__(self):  # No need to call it seperately
    #     return f"Student(Name = {self.name})" # Student(Name = Netaji)

    def __repr__(self):
        return f"Student ('{self.name}')" # Student ('Netaji')

# If __str__() is missing, Python often falls back to __repr__().
# above method str or repr, give priority to __str__ method and ingore __repr__ method
student = Student("Netaji")
print(student) 

print("------------- len ------------")
class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)

library = Library([
    "Python",
    "Java",
    "DotNet",
    "JavaScript"
])
print(len(library)) # 4

print("------------ eq ------------")
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

s1 = Student("Netaji")
s2 = Student("Netaji")
print(s1 == s2) # True, without __eq__() method, will return False

print("------------ add ------------")
class Salary:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

salary1 = Salary(100)
salary2 = Salary(200)

print(salary1 + salary2)

print("------------ getItem --------------")
class Classroom:
    def __init__(self):
        self.students = [
            "Netaji",
            "Alice",
            "Bob"
        ]

    def __getitem__(self, index):
        return self.students[index]

classroom = Classroom()
print(classroom[1])

print("---------- Practical Example ----------")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee(Name={self.name}, Salary={self.salary})"

    def __eq__(self, value):
        return self.name == value.name

    def __add__(self, other):
        return self.salary + other.salary

emp1 = Employee("Netaji", 4500)
emp2 = Employee("Netaji", 4300)
emp3 = Employee("Priya", 4800)

print(emp1)
print(emp1 == emp2)
print(emp1 == emp3)
print(emp1 + emp3)
# output
# Employee(Name=Netaji, Salary=4500)
# True
# False
# 9300

print("------------- Practice Exercise ------------")
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book(Title={self.title}, Author={self.author}, Price={self.price})"

    def __eq__(self, value):
        return self.title == value.title

    def __add__(self, other):
        return self.price + other.price

    def __lt__(self, other):
        return self.price < other.price

book1 = Book("Python Basics", "John", 340)
book2 = Book("Python Basics", "Alice", 390)
book3 = Book("Java", "Bob", 410)

print(book1)
print(book1 == book2)
print(book1 + book3)
print(book1 < book3)
