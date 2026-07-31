
from employee_manager import EmployeeManager
from employee import FullTimeEmployee, PartTimeEmployee, ContractEmployee

manager = EmployeeManager()
manager.load_employees()
print("============ Employee Management System ============")
while True:
    print("\n")
    print("1. Add Employees")
    print("2. View Employees")
    print("3. Search Employees")
    print("4. Delete Employees")
    print("5. Total Payroll Employees")
    print("6. Highest Paid Employee")
    print("7. Save Employee")
    print("8. Salary Report")
    print("9. Sort by Name")
    print("10. Export to CSV")
    print("11. Exit: ")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        employee = None
        
        emp_id = int(input("Employee ID: "))
        name = input("Name: ")
        department = input("Department: ")

        employee_type = input("Employee Type (FullTime/PartTime/Contract): ")
        #print(employee_type, employee_type.lower() == "fulltime")
        if employee_type.lower() == "fulltime":
            monthly_salary = float(input("Monthly Salary: "))
            employee = FullTimeEmployee(emp_id, name, department, monthly_salary)
        elif employee_type.lower() == "parttime":
            hourly_rate = float(input("Hourly Rate: "))
            hours_worked = float(input("Hours Worked: "))
            employee = PartTimeEmployee(emp_id, name, department, hourly_rate, hours_worked)
        elif employee_type.lower() == "contract":
            project_name = input("Project Name: ")
            project_fee = float(input("Project Fee: "))
            employee = ContractEmployee(emp_id, name, department, project_name, project_fee)
        else:
            print("Invalid Employee Type")

        if manager.search_employee(emp_id):
            print(f"\nEmployee with ID {emp_id} already exists!")
        elif employee:
            manager.add_employees(employee)

    elif choice == 2:
        print("\n")
        manager.view_employees()

    elif choice == 3:
        emp_id = int(input("Employee ID: "))
        print(f"\n{manager.search_employee(emp_id)}")

    elif choice == 4:
        emp_id = int(input("Employee ID: "))
        result = manager.delete_employee(emp_id)
        if result:
            print("Employee delete successfully!")
        else:
            print(f"Employee not found for ID {emp_id}")

    elif choice == 5:
        print(f"\n{manager.total_payroll()}")

    elif choice == 6:
        print(f"\n{manager.highest_paid_employee()}")

    elif choice == 7:
        manager.save_data()

    elif choice == 8:
        manager.salary_report()

    elif choice == 9:
        manager.sort_by_name()
        manager.view_employees()

    elif choice == 10:
        manager.export_to_csv()

    elif choice == 11:
        print("Good bye!")
        break

    else:
        print("Invalid choice, please enter choice between 1-9")

