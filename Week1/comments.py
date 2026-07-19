# This is a single line comments

"""
    Calculate the total 
    price for a product.
"""
print("Salary is")
print(3 * 23.4)
age = 34
if age >= 18:
    print("adult")
    print("Can vote")

print("Okay")

age=25
isEmployeed=True

if age > 18:
    print("Can vote2")
    if isEmployeed:
        print("Active Employee")

print("----------- Line Length ----------------")
employee_description = (
    "This is a very long description about an employee "
    "and their responsibilities"
)
print(employee_description)

print("----------- Breaking Long Expressions ----------------")
price=10
tax = 1.2
shipping=2
discount = 2
total = (
    price
    + tax
    + shipping
    - discount
)
print(f"Total: ", total)