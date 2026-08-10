
age = 2

if age <= 0:
    raise ValueError(f"Age cannot be negative: {age}")

else:
    print(f"Valid age: {age}")

def deposit(amount: float):

    if amount <= 0:
        raise ValueError("Amount should be greater that zero(0)")

    print(f"Deposited amount: {amount}")

try:

    deposit(-500)

except ValueError as err:
    print(f"Deposit failed: {err}")


def process_data():

    try:

        number = int("abc")

    except ValueError:
        print("Error occurred while processing data")
        raise

try:

    process_data()

except ValueError as err:
    print(f"\nError: {err}")

print("------------- Example with both ------------")
def set_salary(salary):

    if not isinstance(salary, (int, float)):
        raise TypeError("Salary must be a number")

    if salary < 0:
        raise ValueError("Salary cannot be negative")

    print(f"Salary: {salary}")

set_salary("-9")