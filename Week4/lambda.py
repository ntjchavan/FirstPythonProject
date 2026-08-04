# Syntax
# lambda parameters: expression

# Normal function
def square(x):
    return x * x

print(square(8))

# Instead of above, you can wrote like below.
lambda_sqr = lambda x: x * x

print(lambda_sqr(9))

add = lambda a, b: a + b
print("Addition:", add(10, 12))

# Even or Odd
is_even = lambda num: "Even" if num % 2 == 0 else "Odd"
print("Number 8:", is_even(8))

# Largest Number
large = lambda a, b: a if a > b else b
print(large(10, 15))

# Mini Exercise
salaries = [25000, 27000, 24500, 28000, 21000]

updated_salary = lambda salary: salary + 10
print(updated_salary)
