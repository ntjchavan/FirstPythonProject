# Employee Management System – Phase 5: Data Persistence with JSON
# In this final phase, we'll solve that by saving employee data to a JSON file and loading it back when the program starts.
# By the end of this phase, you'll have a project that behaves much more like a real application.
import json
import logging
import csv

from employee import FullTimeEmployee, PartTimeEmployee, ContractEmployee

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employees(self, employee):
        self.employees.append(employee)
        logging.info(
            f"Employee Added: {employee.emp_id} - {employee.name}"
        )

    def view_employees(self):
        if not self.employees:
            print("No employees available")

        for employee in self.employees:
            print(employee)

    def search_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee

        return None

    def delete_employee(self, emp_id):
        employee = self.search_employee(emp_id)

        if employee:
            self.employees.remove(employee)
            logging.info(
                f"Employee deleted: {emp_id}"
            )
            return True

        return False
    
    def total_payroll12(self):
        total = 0
        for employee in self.employees:
            total += employee.calculate_salary()

        return total

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

    def salary_report(self):
        highest = self.highest_paid_employee()
        total_payroll = self.total_payroll()
        average = total_payroll / len(self.employees)

        print(f"Total Employees: {len(self.employees)}")
        print(f"Highest Salary: {highest.calculate_salary()}")
        print(f"Total Salary: {total_payroll}")
        print(f"Average Salary: {average:.2f}")

    def sort_by_name(self):
        self.employees.sort(key=lambda employee: employee.name)

    def save_data(self, filename="employee.json"):
        data = []

        for employee in self.employees:
            data.append(employee.to_dict())

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print(f"\nData saved successfully.")

    def load_employees(self, filename="employee.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            self.employees = []
            for item in data:
                if item["type"] == "FullTimeEmployee":
                    employee = FullTimeEmployee(
                        item["emp_id"], item["name"], item["department"], item["monthly_salary"]
                    )
                elif item["type"] == "PartTimeEmployee":
                    employee = PartTimeEmployee(
                        item["emp_id"], item["name"], item["department"], item["hourly_rate"], item["hours_worked"]
                    )
                elif item["type"] == "ContractEmployee":
                    employee = ContractEmployee(
                        item["emp_id"], item["name"], item["department"], item["project_name"], item["project_fee"]
                    )
                else:
                    continue

                self.employees.append(employee)

            print("Employees loaded successfully!")
        except FileNotFoundError:
            print("No saved data found!")
        except json.JSONDecodeError:
            print("Invalid JSON file.")

    def export_to_csv(self, filename="employees.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Employee ID",
                "Name",
                "Department",
                "Type",
                "Salary"
            ])

            for employee in self.employees:
                writer.writerow([
                    employee.emp_id,
                    employee.name,
                    employee.department,
                    employee.__class__.__name__,
                    employee.calculate_salary()
                ])

            print("CSV Exported Successfully!")
