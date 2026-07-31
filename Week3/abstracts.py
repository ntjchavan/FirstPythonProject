from abc import ABC, abstractmethod

class Animal(ABC):

    def eat(self):
        print("Animal is eating")

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()

# ----------------------------------------------------------
print("---------- Practical Example: Payment System --------------")
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit payment")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI payment")

credit = CreditPayment()
upi = UpiPayment()

credit.pay(130)
upi.pay(95)

# ----------------------------------------------
print("------------ Practice Exercise ----------------")
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        area = 3.14 * (self.radius ** 2)
        print(f"Area of circle: {area:.2f}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print(f"Area of rectangle: {area}")

circle = Circle(5)
rectangle = Rectangle(10, 5)

circle.calculate_area()
rectangle.calculate_area()
