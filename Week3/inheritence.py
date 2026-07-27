class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()

# --------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

stud = Student("Netaji", 31)
stud.introduce()
stud.study()

# A Practical Example: Employees
print("-------------- A Practical Example: Employees ---------------")
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Developer(Employee):
    def code(self):
        print(f"{self.name} is writing code")

class Manager(Employee):
    def manage_team(self):
        print(f"{self.name} is managing team")

developer = Developer("Netaji", 32)
manager = Manager("Shivam", 22)

developer.show_details()
developer.code()
print("\n")
manager.show_details()
manager.manage_team()

# Practice Exercise
print("------------------ Practice Exercise ------------------")
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors):
        super().__init__(brand, model)
        self.number_of_doors = number_of_doors

    def drive(self):
        print(f"Car has {self.number_of_doors} doors")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def ride(self):
        print(f"Bike has {self.engine_cc} engine")

car = Car("Toyota", "Camry", 4)
car.show_details()
car.drive()

print("\nBike")
bike = Bike("Honda", "Shine", 125)
bike.show_details()
bike.ride()
