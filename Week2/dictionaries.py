employee = {
    "name": "Netaji",
    "age": 35,
    "role": "Developer"
}
print(employee)

# using dict():
student = dict(
    name="Alice",
    marks=90,
    passed=True
)
print(student)

# Accessing Values
print(student["name"])
print(student.get("age")) # None, will not throw error if used get

# Removing Items
employee = {
    "name": "Netaji",
    "age": 24
}
del employee["age"]
print(employee)

# Iterating Through Keys
employee = {
    "name": "Netaji",
    "age": 35,
    "role": "Developer"
}
for key in employee:
    print(key)

# Iterating Through Values
for val in employee.values():
    print(val)

# Iterating Through Key-Value Pairs
for key, value in employee.items():
    print(key, value)

# List of Dictionaries
employees = [
    {
        "name": "Alice",
        "salary": 80000
    },
    {
        "name": "Bob",
        "salary": 90000
    }
]
for val in employees:
    print(val["name"])

print("--------------- Real-World Example: Word Count ------------------")
text = "python is fun python is powerful"
word_count = {}

for word in text.split(' '):
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

# dictionary comprehension
squares = {
    num: num * num for num in range(1, 11)
}
print(squares)

# Print only employees whose salary is greater than 90000.
employees = [
    {"name":"Alice","salary":80000},
    {"name":"Bob","salary":120000},
    {"name":"Charlie","salary":97000}
]

higher_sal_emp = [
    emp for emp in employees if emp.get("salary") > 90000
]
print(higher_sal_emp)

print("----------------- Mini Project: Employee Management System ----------------")
employees = [
    {
        "id":101,
        "name":"Alice",
        "salary":80000,
        "experience":5
    }
]

while True:
    print("--------------- Employee Management System -----------------")
    print("1. Add employee")
    print("2. Display all employees")
    print("3. Search employee by ID")
    print("4. Update salary")
    print("5. Delete employee")
    print("6. Exit")

    choice = input("Enter your choice between 1-6: ")
    if choice == "1":
        id = int(input("ID: "))
        name = input("Name: ")
        sal = int(input("Salary: "))
        exp = float(input("Experience: "))
        employees.append({
            "id": id,
            "name": name,
            "salary": sal,
            "experience": exp
        })

    elif choice == "2":
        for emp in employees:
            print(f"Emp ID: {emp["id"]}, Name: {emp["name"]}, Salary: {emp["salary"]} Exp: {emp["experience"]}")

    elif choice == "3":
        emp_id = int(input("Enter employee Id: "))
        emp_found = False
        for emp in employees:
            print(emp["id"], emp_id, emp["id"] == emp_id)
            if emp["id"] == emp_id:
                print(f"Employee Found:\n Emp ID: {emp["id"]}, Name: {emp["name"]}, Salary: {emp["salary"]} Exp: {emp["experience"]}")
                emp_found = True

        print(emp_id)
        if emp_found == False:
            print(f"Employee not found with id: {emp_id}")

    elif choice == "4":
        emp_id = int(input("ID: "))
        sal = float(input("Salary: "))
        emp_found = False
        for emp in employees:
            if emp["id"] == emp_id:
                emp["salary"] = sal
                print("Salary updated")
                emp_found = True
        if emp_found == False:
            print("Employee not found for id: ", emp_id)

    elif choice == "5":
        emp_found = False
        emp_id = int(input("Enter employee id: "))
        for i, emp in enumerate(employees):
            if emp["id"] == emp_id:
                del employees[i]
                emp_found = True
                print("Employee deleted")
                break
        if emp_found == False:
            print("Employe not found with id:", emp_id)

    elif choice == "6":
        break
    else:
        print("Invalid choice, please choose correct choice between 1-6")


