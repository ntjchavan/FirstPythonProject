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
    

# employee_fulltime = FullTimeEmployee(101, "Netaji", "IT", 50000)
# print(employee_fulltime.calculate_salary())

# employee_parttime = PartTimeEmployee(102, "Bob", "HR", 500, 120)
# print(employee_parttime.calculate_salary())

# employee_contract = ContractEmployee(103, "Alice", "Account", "Bank Management", 53000)
# print(employee_contract.calculate_salary())
# OR
# ----------- start -------------
employess = [
    FullTimeEmployee(101, "Netaji", "IT", 50000),
    PartTimeEmployee(102, "Bob", "HR", 500, 120),
    ContractEmployee(103, "Alice", "Account", "Bank Management", 53000)
]

for emp in employess:
    # print(emp.name, end=" | ")
    # print(emp.calculate_salary())
    print(emp)
    print(f"Salary: {emp.calculate_salary()}")

print("-" * 80)
# ----------- end -------------
