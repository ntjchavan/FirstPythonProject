class Student:
    def __init__(self): # need to pass variable to instructor
        print("Student object created")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} old")
        print(f"My income is {self.salary}")

# stud = Student()
stud1 = Student("Netaji", 35, 58900)
# print(f"Name: {stud1.name}, Age: {stud1.age}, Salary: {stud1.salary}")
stud1.introduce()


# ------------------------------------------------------------------------
print("\nEmployee")
class Employee:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def show_details(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"My role is {self.role}")

    def work(self):
        print(f"{self.name} is working")

emp = Employee("Shivam", 21, "Developer")
emp.show_details()
emp.work()

#---------------------------------------------------------
print("\nBook")
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

book = Book("Python basics", "John smith", 500)
book.show_details()

