# print("------------------- Employee --------------------")
class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def calculate_salary(self):
        pass

    def __str__(self):
        return (
            f"ID: {self.emp_id} | "
            f"Name: {self.name} | "
            f"Department: {self.department}"
        )

# print("------------------- FullTimeEmployee --------------------")
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, department, monthly_salary):
        super().__init__(emp_id, name, department)
        self.monthly_salary = monthly_salary

    def __str__(self):
        return (
            super().__str__()
            + f" | Monthly Salary: {self.monthly_salary}"
        )
    
    def calculate_salary(self):
        return self.monthly_salary

# print("------------------- PartTimeEmployee --------------------")
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, department, hourly_rate, hours_worked):
        super().__init__(emp_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def __str__(self):
        return (
            super().__str__()
            + f" | Hourly Rate: {self.hourly_rate}"
            + f" | Hours: {self.hours_worked}"
        )

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# print("------------------- ContractEmployee --------------------")
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, department, project_name, project_fee):
        super().__init__(emp_id, name, department)
        self.project_name = project_name
        self.project_fee = project_fee

    def calculate_salary(self):
        return self.project_fee

    def __str__(self):
        return (
            super().__str__()
            + f" | Project Fee: {self.project_fee}"
        )

# print("------------------- EmployeeManager --------------------")
class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employees(self, employee):
        self.employees.append(employee)

    def view_employees(self):
        if not self.employees:
            print("No employees")

        for employee in self.employees:
            print(employee)

    def search_employees(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee

        return None

    def delete_employees(self, emp_id):
        employee = self.search_employees(emp_id)

        if employee:
            self.employees.remove(employee)
            return True

        return False

    def total_employees(self):
        return len(self.employees)

    def find_by_department(self, department):
        print("Search by department")
        list = []
        for employee in self.employees:
            if employee.department == department:
                list.append(employee)

        if not list:
            return None

        return list

    def total_payroll(self):
        total = 0
        for employee in self.employees:
            total += employee.calculate_salary()

        return total

    def highest_paid_employee(self):
        if not self.employees:
            return None

        highest = self.employees[0]
        for employee in self.employees:
            if (
                highest.calculate_salary() < employee.calculate_salary()
            ):
                highest = employee

        return highest

print("----------------- Add Employees --------------")
manager = EmployeeManager()
manager.add_employees(
    FullTimeEmployee(101, "Netaji", "IT", 50000)
)
manager.add_employees(
    PartTimeEmployee(102, "Alice", "HR", 600, 100),
)
manager.add_employees(
    ContractEmployee(103, "Bob", "IT", "ABC Project", 35000)
)

# print("-" * 80)
print("----------------- Employee list --------------")
manager.view_employees()

print("----------------- Search Employee by ID --------------")
print(manager.search_employees(101))

print("----------------- Delete Employee --------------")
# print(manager.delete_employees(103))

print("----------------- Total Employee --------------")
print("Total employees:", manager.total_employees())

print("----------------- Search Employee by Department --------------")
employees = manager.find_by_department("IT")
if employees:
    for employee in employees:
        print(employee.name)
else:
    print("No employee found in department 'IT'")

print("----------------- Total payroll of all employees --------------")
print(manager.total_payroll())

print("----------------- Highest Employee Salary --------------")
highest = manager.highest_paid_employee()
print(highest)
print(f"Highest: {highest.calculate_salary():,.2f}")
