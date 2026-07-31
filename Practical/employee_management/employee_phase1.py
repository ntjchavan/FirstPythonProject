class Employee:
    company: str = "ABC Technologies"

    def __init__(self, emp_id, name, age, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.designation = designation
        self.salary = salary

    def __str__(self):
        return (
            f"ID: {self.emp_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Department: {self.department} | "
            f"Designation: {self.designation} | "
            f"Salary: {self.salary} | "
            f"Company: {self.company} | "
            f"Annual Salary: {self.annual_salary}"
        )

    @property
    def annual_salary(self):
        return self.salary * 12

employees = [
    Employee(101, "Netaji", 33, "IT", "Developer", 87000),
    Employee(102, "Priya", 29, "HR", "HR Manager", 59200),
    Employee(103, "Bob", 2459, "IT", "Delivery Manager", 93080)
]
# employees.append(
#         Employee(101, "Netaji", 33, "IT", "Developer", 87000)
#     )
# employees.append(
#         Employee(102, "Priya", 29, "HR", "HR Manager", 59200)
#     )
# employees.append(
#         Employee(103, "Bob", 2459, "IT", "Delivery Manager", 93080)
#     )

print("Employee List")
print("-" * 80)
for employee in employees:
    print(employee)

print("------------------ Update salary ------------------")
for employee in employees:
    if employee.emp_id == 102:
        employee.salary = 61300
        break

for employee in employees:
    print(employee)
