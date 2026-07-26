BONUS_RATE = 0.10

def calculate_bonus(salary):
    return salary * BONUS_RATE

def calculate_total_salary(salary):
    bonus = calculate_bonus(salary)
    return salary + bonus

if __name__== "__main__":
    salary = 1000
    total_salary = calculate_total_salary(salary)
    print(f"Total Salary: {total_salary:.2f}")