# Annotations that describe expected types for variables, parameters, and return values. 
# They improve readability and tooling but are not enforced by Python itself.


def add(a: int, b: int) -> int:
    return a + b

result = add(10, 20)
print(result)

numbers: list[int] = [1, 2, 3, 4]

# Dictionary Type
marks: dict[str, int] = {
    "maths": 93,
    "physics": 96
}

# Tuple Type
points: tuple[int, int] = (10, 12)

# Set types
roles: set[str] = { "Admin", "Manager" }

# Optional Values
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if(user_id == 1):
        return "Alice"
    
    return None

print(find_user(1))

def find_student(user_id: int) -> str | None: # requires Python 3.10+
    if(user_id == 2):
        return "Bob"
    
    return None

print(find_student(2))

# Use TypedDict: can validate keys and value types
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

user: User = {
    "name": "Netaji",
    "age": 30
}

# Generic Functions
from typing import TypeVar

T = TypeVar("T")

def first_item(items: list[T]) -> T:
    return items[0]

print(first_item([1, 2, 3]))
print(first_item(["A", "B", "C"]))

print("------------ Real-World Example 1 Employee ----------------")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self) -> float:
        return self.salary * 12

employee = Employee("Bob", 24590.12)
print(employee.annual_salary())


# Mini Exercise
print("-------------- Mini Exercise ----------------")

class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if 0 < amount < self.balance:
            self.balance -= amount
            return True

        return False

    def get_balance(self) -> float:
        return self.balance

bank_account = BankAccount("Acc-01", 5000)
bank_account.deposit(2500)
print(bank_account.get_balance())
status = bank_account.withdraw(2000)
print(f"{ "Withdrawal successfull" if status else "Failed"}")
print(bank_account.get_balance())
status = bank_account.withdraw(6000)
print(f"{ "Withdrawal successfull" if status else "Failed"}")


class Transactions(TypedDict):
    account_no: str
    amount: float
    transaction_type: str

transactions: list[Transactions] = [
    {"account_no": "Acc-01", "amount": 123.56, "transaction_type": "Saving" },
    {"account_no": "Acc-02", "amount": 234.11, "transaction_type": "Fixed" },
    {"account_no": "Acc-03", "amount": 223.01, "transaction_type": "Current" },
]
