age = 23
if age >= 18:
    print("you are an adult.")

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

marks = 98
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

print("----------- Multiple Conditions --------------")
age = 31
experience = 11

if age >=30 and experience >=10:
    print("You are eligible for senior position.")
else:
    print("You are not eligible for senior position.")

print("----------- Nested if --------------")
username = "admin"
password = "secret"

if username == "admin":
    if password == "secret":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")

print("----------- Ternary Operator --------------")
age = 16
result = "Adult" if age >= 18 else "Minor"
print(result)

print("----------- Match Statement --------------")
day = 8

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

print("----------- Check Even or Odd --------------")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
    
print("----------- Check Positive, Negative or Zero --------------")
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

print("----------- Largest of Two Numbers --------------")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is larger than {num2}.")
else:
    print(f"{num2} is larger than {num1}.")

print("----------- Employee Promotion ---------------")
experience = int(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1-5): "))

if experience >= 10 and rating >= 4:
    print("Eligible for promotion.")
else:
    print("Not eligible for promotion.")