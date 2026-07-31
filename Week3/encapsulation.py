class BankAccountTest:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance

account = BankAccountTest(12000)
account.deposit(3000)

print(account.get_balance())
account.withdraw(2000)

print(account.get_balance())

# ------------------------------------------------
print("------------- Encapsulation with Get & Set ------------")

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

student = Student("Netaji", 34)
print(student.get_name())
print(student.get_age())

student.set_age(25)
print(student.get_age())

# -----------------------------------------------------
print("--------------- Encapsulation with Inheritance --------------")
class Parent:
    def __init__(self):
        self.__value = 100

    def get_value(self):
        return self.__value

class Child(Parent):
    def show_value(self):
        print("Value of parent class", self.get_value())

ch = Child()
ch.show_value()

# ----------------------------------------
print("---------- Public vs Protected vs Private ------------")

class Example:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"


print("------------- Practice Exercise --------------")
class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance = amount

    def get_balance(self):
        return self.__balance

    def show_details(self):
        print(f"Account Holder Name: {self.__account_holder} & Balance: {self.__balance}")

account = BankAccount("Netaji", 10000)
account.deposit(5000)
account.withdraw(2000)

print(account.get_balance())
