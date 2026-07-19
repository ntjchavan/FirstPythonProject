name = "netaji"
age=35

print(f"Name is {name} and age is {age}")

print("-------- Print multiple values -------")
print(name, age);

print("--------sep Parameter------")
print(name, age, sep="-")
print("Python", "Java", ".Net", sep=" | ")

print("------ end Parameter ---------")
print("Hello", end=" ")
print("World")

print("------------- input ------------------")
name = input("Enter name: ")
print(name)

age = input("Enter age: ")
print(age, type(age))

print("--------- Converting Input ------------")
salary = int(input("Enter salary int: "))
print(salary)

salary = float(input("Enter salary float: "))
print(salary)

print("------- Formatting Numbers ----------")
price =12345.456723
print(f"{price:.3f}")

print("-------- Escape Characters ---------")
print("Hello \nworld")
print("Hello \tNetaji")

print("---------- Double Quotes Inside String ------------")
print("Welcome to \"Jungle\"")
print('Welcome to "Dhamal"')

print("---------- Raw Strings ------------")
path = r"C:\Users\Netaji\Documents"
print(path)

print("------------- Practical Example: 1 -------------")
name=input("Enter your name:")
age=int(input("Enter age:"))
salary=float(input("Enter salary: "))
experience=float(input("Enter experience: "))
isActive = bool(input("Is Active: "))

print("\nEmployee Information:")
print("----------------------------------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Salary: {salary}")
print(f"Experience: {experience}")
print(f"Is Active: {isActive}")

print("------------- Practical Example: 2 -------------")
name=input("Enter name: ")
age=int(input("Enter age: "))
city=input("Enter city: ")
print(f"My name is {name}. I am {age} years old and live in {city}")

print("------------- Practical Example: 3 -------------")
productName = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price=float(input("Enter product price:"))
print("Product Name:", productName)
print(f"Quantity: {quantity}")
print(f"Price: {price}")
print(f"Total: {quantity * price}")

