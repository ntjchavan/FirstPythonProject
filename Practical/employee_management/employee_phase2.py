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
]

def add_employee():
    emp_id = int(input("Enter employee ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))

    for emp in employees:
        if emp.emp_id == emp_id:
            print("\nEmployee ID already exists:", emp_id)
            return
        
    new_employee = Employee(emp_id, name, age, department, designation,salary)
    employees.append(new_employee)
    print("\nEmployee added successfully!")

def view_employees():
    if not employees:
        print("No employees found!")
        return

    print("\nEmployee List")
    for employee in employees:
        print(employee)
        
def search_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    for employee in employees:
        if employee.emp_id == emp_id or employee.name == name:
            print("\nEmployee found!")
            print(employee)
            return

    print(f"\nEmployee not found with id {emp_id}")

def update_employee():
    emp_id = int(input("Enter Employee ID to update employee: "))

    for emp in employees:
        if emp.emp_id == emp_id:
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            designation = input("Enter Designation: ")
            salary = float(input("Enter Salary: "))

            emp.name = name
            emp.department = department
            emp.designation = designation
            emp.salary = salary

            print("\nEmployee update successfully!")
            return

    print(f"\nEmployee not found with id {emp_id}")

def delete_employee():
    emp_id = int(input("Enter Employee ID to Delete: "))
    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("\nEmployee deleted successfully!")
            return

    print(f"Employee not found with ID: {emp_id}")

def total_employees():
    print(f"Total Employees: {len(employees)}")

while True:
    print("\n============ Employee Management System ============")
    print("1. Add employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Total Employee")
    print("7. Exit")

    choice = int(input("Enter you choice: "))
    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employees()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        update_employee()

    elif choice == 5:
        delete_employee()

    elif choice == 6:
        total_employees()

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice, please enter correct choice")