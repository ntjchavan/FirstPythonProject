class EmployeeTest:
    company = "OpenAI"

    @classmethod
    def show_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name


EmployeeTest.show_company()

EmployeeTest.change_company("AI Solutions")

EmployeeTest.show_company()

print("----------- Alternative Constructors -------------")
class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    @classmethod
    def from_string(cls, data):
        name, age, department = data.split("-")
        return cls(name, int(age), department)
        # return Employee(name, int(age), department) # we can write like this as well

employee = Employee.from_string("Netaji-33-Developer")
print(employee.name)
print(employee.age)
print(employee.department)

print("------------- Complete Example --------------")
class Product:
    store = "ABC Store"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name} - {self.price}")

    @classmethod
    def change_store(cls, new_name):
        cls.store = new_name

    @classmethod
    def from_string(cls, data):
        name, price = data.split(",")
        return cls(name, float(price))

product = Product.from_string("Laptop, 50000")
product.show()

print(product.store)

product.change_store("XYZ Store")
print(product.store)
# we can use like below as well
# Product.change_store("XYZ Store")
# print(Product.store)

print("---------------- Practice Exercise ----------------")
class Student:
    school = "ABC Public school"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

    @staticmethod
    def is_valid_age(age):
        return 5 <= age <= 100

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, age)

student = Student.from_string("Netaji-34")
student.introduce()

print(Student.school)

Student.change_school("XYZ School")

print(Student.school)

print(Student.is_valid_age(20))
