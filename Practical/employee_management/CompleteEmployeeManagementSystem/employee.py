#print("------------------ Employee --------------------")
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

    def to_dict(self):
        return {
            "type": "Employee",
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department
        }
    
#print("------------------ FullTimeEmployee --------------------")
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
        return self.monthly_salary * 12

    def to_dict(self):
        return {
            "type": "FullTimeEmployee",
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "monthly_salary": self.monthly_salary
        }

#print("------------------ PartTimeEmployee --------------------")
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, department, hourly_rate, hours_worked):
        super().__init__(emp_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def __str__(self):
        return (
            super().__str__()
            + f" | Hourly Rate: {self.hourly_rate}"
            + f" | Hours_worked: {self.hours_worked}"
        )

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def to_dict(self):
        return {
            "type": "PartTimeEmployee",
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "hourly_rate": self.hourly_rate,
            "hours_worked": self.hours_worked
        }

#print("------------------ ContractEmployee --------------------")
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, department, project_name, project_fee):
        super().__init__(emp_id, name, department)
        self.project_name = project_name
        self.project_fee = project_fee

    def __str__(self):
        return (
            super().__str__()
            + f" | Project Name: {self.project_name}"
            + f" | Project Fee: {self.project_fee}"
        )

    def calculate_salary(self):
        return self.project_fee

    def to_dict(self):
        return {
            "type": "ContractEmployee",
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "project_name": self.project_name,
            "project_fee": self.project_fee
        }
