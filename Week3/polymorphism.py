# Same Method, Different Classes
class Car:
    def start(self):
        print("Car engine starts")

class Bike:
    def start(self):
        print("Bike engine starts")

car = Car()
bike = Bike()

car.start()
bike.start()

# A Real-World Example: Payment System
print("----------- Payment system ------------")
class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using credit card")

class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class Cash:
    def pay(self, amount):
        print(f"Paid {amount} using cash")


def process_payment(payment_method, amount):
    payment_method.pay(amount)

credit_card = CreditCard()
upi = UPI()
cash = Cash()

process_payment(credit_card, 100)
process_payment(upi, 130)
process_payment(cash, 85)

print("---------- Method Overriding --------------")
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog bark")


animal = Animal()
dog = Dog()

dog.sound()

print("-------------- Practical Example: Employee Management ------------")
class Employee:
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 20000

def show_salary(employee):
    print(employee.calculate_salary())

full_time = FullTimeEmployee()
part_time = PartTimeEmployee()

show_salary(full_time)
show_salary(part_time)
