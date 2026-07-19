print("----------- For loop --------------")
for i in [1,2,3,4,5]:
    print(i)

print("----------- For loop using range --------------")
for i in range(6):
    print(i)

for i in range(11, 21):
    print(i)

print("----------- For loop using range with step --------------")
for i in range(1, 21, 2):
    print(i)

print("----------- Loop Through a String --------------")
for char in "Hello":
    print(char)

print("----------- Loop Through a list --------------")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("----------- Loop Through a dictionary --------------")
employee = {
    "name": "Netaji",
    "age": 31,
    "experience":11
}
for key in employee:
    print(key, ":", employee[key])

print("----------- while Loop --------------")
cnt = 1
while cnt <= 5:
    print(cnt)
    cnt += 1

print("----------- Loop with break --------------")
for i in range(1, 11):
    if i == 6:
        break
    print(i)

print("----------- Loop with continue --------------")
for i in range(7):
    if i == 2 or i == 5:
        continue
    print(i)

print("----------- Loop with else --------------")
for i in range(4):
    print(i)
else:
    print("Loop completed successfully")

print("----------- Loop with patterns --------------")
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

print("----------- enumerate function --------------")
languages = ["Python", "Java", "C++", "JavaScript"]
for i, l in enumerate(languages):
    print(i, l)
print("\n")
for i, l in enumerate(languages, start=1):
    print(i, l)

print("----------- zip function --------------")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)

print("----------- while True --------------")
# while True:
#     user_input = input("Enter 'exit' to quit: ")
#     if user_input.lower() == 'exit':
#         break
#     print("You entered:", user_input)

print("----------- Practice Exercises --------------")
print("----------- Exercise 1: Print numbers from 1 to 10 --------------")
for i in range(1, 11):
    print(i)

print("----------- Exercise 2: Sum of number from 1 to 100 --------------")
total = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100 is:", total)

print("----------- Exercise 3: Print even numbers from 1 to 50 --------------")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

print("\n----------- Exercise 4: Reverse Countdown ---------------")
for i in range(10, 0, -1):
    print(i, end=" ")

print("\nBlast off!")

print("----------- Exercise 5: Find a Number ---------------")
numbers = [10, 20, 30, 40, 50]
search_num = 30
for num in numbers:
    if num == search_num:
        print(f"Found {search_num} in the list.")
        break

print("----------- Exercise 6: Login Attempts ---------------")
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == "p":
        print("Login successfull!")
        break

    attempts += 1
    if attempts == 3:
        print("Account locked")

print("----------- Exercise 7: Employee Search ---------------")
employees = ["Alice", "Bob", "Charlie", "David"]
search_name = input("Enter employee name to serch: ")
for emp in employees:
    if emp.lower() == search_name.lower():
        print(f"{search_name} found.")
        break
else:
    print(f"{search_name} not found.")
