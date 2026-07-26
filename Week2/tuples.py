
employee = ( "Netaji", 35, "Software Developer" )
print(employee)

language_lists = ["Python", "Java", "C#", "Ruby"]
language_tuples = ("Python", "Java", "C#", "Ruby")
print(language_lists)
print(language_tuples)

mixed_datatypes_tuple = ("Netaji", 35, True, 75309.54)
print(mixed_datatypes_tuple)

# Single-Item Tuple
number = (10,)
print(type(number))

# Empty Tuple
empty_tuple = ()
print(type(empty_tuple))

# Accessing Tuple Elements
languages = ("Python", "Java", "C#", "Go", "Ruby")
print(languages[0])
print(languages[2])
# Negative Indexing
print(languages[-2])

# Slicing : Works exactly like lists
print(languages[1:4])

# Looping Through a Tuple
for l in languages:
    print(l)

# Checking Membership
if "Java" in languages:
    print("Found")
else:
    print("Not Found")

# Tuple Methods
numbers = (1, 2, 2, 3, 4, 5, 2)
print(numbers.count(2)) # output - 3

print(numbers.index(4)) # output - 4

# Packing : Python automatically packs values into a tuple.
employee = "Netaji", 35, "Developer"
print(employee)

# Unpacking - You can unpack a tuple into separate variables.

name, age, role = employee
print(name)
print(age)
print(role)

# Returning Multiple Values
def calculate(a, b):
    return (
        a + b,
        a - b,
        a * b
    )

result = calculate(10, 5)
print(result)

# Extended Unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first, middle, last)

print("-------------- Practice Exercises ---------------")
# Excercise 1 - Create a tuple containing five programming languages. print first, last and length
programming_lang = ("Python", "Java", "JavaScript", "Ruby", "C#")
print(programming_lang[0], programming_lang[4], len(programming_lang))

# Excercise 2 - unpack & print it
employee = (
    "Netaji",
    35,
    "Developer"
)
name, age, role = employee
print(name, age, role)

# Excercise 3 - Swap two variables without using a temporary variable.
x = 100
y = 200
y, x = x, y
print(x, y)

# Excercise 4: Create a function that returns: Sum, Difference, Product
def operations(x, y):
    return (
        x + y,
        x - y,
        x * y
    )

result = operations(12, 5)
sum, diff, product = result
print(sum, diff, product)

# Excercise 5 - Create a tuple of employee records, Use a loop to print:
employees = (
    ("Netaji", 35),
    ("Alice", 33),
    ("Bob", 40)
)

for e in employees:
    print(f"{e[0]} is {e[1]} years old")

# Use tuple unpacking inside the loop:
for name, age in employees:
    print(f"{name} is {age} years old")

print("------------- Mini Project: Student Results -------------")
# Create a tuple for each student:
alice = ("Alice", 85, 90, 88)
bob = ("Bob", 78, 82, 80)
charlie = ("Charlie", 92, 95, 94)

aname, am1, am2, am3 = alice
bname, bm1, bm2, bm3 = bob
cname, cm1, cm2, cm3 = charlie

aavg = (am1 + am2 + am3) / 3
bavg = (bm1 + bm2 + bm3) / 3
cavg = (cm1 + cm2 + cm3) / 3

print(f"{aname} : {aavg:.2f}")
print(f"{bname} : {bavg:.2f}")
print(f"{cname} : {cavg:.2f}")


