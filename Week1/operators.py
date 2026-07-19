print("----------- Division vs Floor Division ---------")
print(10 / 3) # returns a float. - o/p: 3.3333333333333335
print(10 // 3) # returns the integer quotient (floored). - o/p: 3

print("----------- comparison -----------")
a = 10
b = 20
c = 10

print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

print("--------- logical operators ----------")
age = 25
salary = 90000
print(age > 18 and salary > 50000)

is_active = True
print(not is_active)

is_checked = True
is_manager = False
print(is_checked or is_manager)

print("---------- Identity operators -------------")
a = [1, 2]
b = a
print(a is b) # True, Both variables reference the same list object.

a = [1,2]
b = [1,2]
print(a == b) # True, Checks whether the values are equal.

print(a is b) # False, Because they are two different list objects with the same contents.

print("------------ Membership Operators --------------")
name = "Python"
print("P" in name) # True
print("p" in name) # False
print("x" in name) # False

print("------- Lists ---------")
number = [10, 20, 30]
print(20 in number) # True
print(50 in number) # False
print(50 not in number) # True

username = "netaji"
password = "neta12345"
if username == "netaji" and password == "neta12345":
    print("login successfull")
else:
    print("Invalid credentials")

print("----------- practice exercises ----------")
a = 25
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # Floor division
print(a % b)
print(a ** b) # Power 2 ** 3

age = 21
if age >= 18:
    print("Qualifies to vote")
else:
    print("Not eligible to vote")

counter = 10
counter+=1
counter+=1
counter+=1
counter+=1
counter+=1
print(counter)

name = "Python"
print("t" in name) # membership operator

p = ['a', 'b']
q = ['a', 'b']
print(p == q) # True
print(p is q) # False

t = None
if t is None:
    print("No value")
else:
    print("Value is: ", t)

print("---------- assignment ---------")
employee_name = "netaji chavan"
age = 25
year_of_exp = 7
salary = 55000
if age >= 25 and year_of_exp > 3:
    print("Eligible for promotion")
else:
    print("No promotion")

if salary < 100000:
    print("Received bonus")
else:
    print("No bonus received")
