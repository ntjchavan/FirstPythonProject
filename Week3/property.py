class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    @property
    def annual_salary(self):
        return self.monthly_salary * 12

emp = Employee(5000)
print(emp.annual_salary) 
# annual_salary is a method, but we didn't used brackets/parentheses () to call it because it is marked as @property

print("------------ Property Setter ---------")

class FullTimeEmployee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value
        else:
            print("Salary mu be positive")

fulltime_emp = FullTimeEmployee(12000)
print(fulltime_emp.salary)

fulltime_emp.salary = 12500
print(fulltime_emp.salary)

print("----------- Student complete example -----------")
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
             self._marks = value
        else:
            print("Marks must be between 0 to 100.")

    @property
    def result(self):
        if self._marks >= 40:
            return "Pass"
        else:
            return "Fail"

student = Student(45)
print(student.marks)
print(student.result)

student.marks = 35
print(student.marks)
print(student.result)

print("----------- Practice Exercise ---------")
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if 0 < price:
            self._price = price
        else:
            price("Price should be grater that 0")

    @property
    def discounted_price(self):
        return self._price - ((10 / 100) * self._price)

product = Product("Laptop", 50000)
print(product.price)
print(product.discounted_price)

product.price = 60000
print(product.discounted_price)
