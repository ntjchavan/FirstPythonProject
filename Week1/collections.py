
# Lists
languages = ["Python", "Java", "C++", "JavaScript"]
numbers = [1, 2, 3, 4, 5]

# Empty list
items = []
items.append("item1")
items.append("item2")
print(items)

# List indexing
print(languages[0])
print(languages[-1]) # Accessing the last element JavaScript

# Changing List Items
print(languages)
languages[1] = "C#"
print(languages)

# Adding Items with insert
languages.insert(2, "Ruby")
print(languages)

# Adding Multiple Items with extend()
more_languages = ["Go", "Swift"]
languages.extend(more_languages)
print(languages)

# Removing Items with remove()
languages.remove("Swift")
print(languages)

# Removing by Index with pop()
index = languages.pop(4)
print(f"Removed language: {index}")
print(languages)

# Delete Using del
del languages[3]
print(languages)
del languages[1:2] # Deletes from index 1 to 2
print(languages)

# Clear the Entire List
languages.clear()
print(languages)

languages = ["Python", "Java", "C++", "JavaScript"]

# List Length
print(len(languages))

# Check Whether an Item Exists
if "Java" in languages:
    print("Java is in the list")
else:
    print("Java is not in the list")
    
# Loop Through a List
for l in languages:
    print(l, end=" | ")

# List Slicing
print("\n")
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4]) # [start:stop] - The stop index is excluded.
print(numbers[:3])  # [start:stop] - From the beginning to index 3 (exclusive)
print(numbers[2:])  # [start:stop] - From index 2 to the end
print(numbers[:]) # [start:stop] - From the beginning to the end

# Sorting Lists
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
# sort() : Sorts the list in ascending order by default
# sorted() : Creates a new sorted list
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Counting Items
numbers = [1, 2, 3, 4, 5, 1, 2, 1]
print(numbers.count(1)) # Count the occurrences of 1 in the list - 3

print("-------------- Practice Exercises ---------------")
# Exercise 1: Basic List
languages = ["Python", "Java", "C++", "JavaScript", "TypeScript"]
print(languages)
print(languages[0]) # Output: Python
print(languages[-1]) # Output: TypeScript
languages[2] = "C#"
print(languages) # Output: ['Python', 'Java', 'C#', 'JavaScript', 'TypeScript']
languages.append("Go")
print(languages) # Output: ['Python', 'Java', 'C#', 'JavaScript', 'TypeScript', 'Go']
languages.remove("JavaScript")
print(languages) # Output: ['Python', 'Java', 'C#', 'TypeScript', 'Go']

# Exercise 2: Numbers
numbers = [10, 5, 20, 15, 30]
print(numbers)
print(max(numbers)) # Output: 30
print(min(numbers)) # Output: 5
print(sum(numbers)) # Output: 80
numbers.sort()
print(numbers) # Output: [5, 10, 15, 20, 30]

# Exercise 3: Even Numbers
numbers_list = []
for i in range(1, 51):
    numbers_list.append(i)

print(numbers_list)

even_numbers = []
for i in numbers_list:
    if i % 2 == 0:
        even_numbers.append(i)
    
print(even_numbers)

# List Comprehension with if-else
result = [
    number
    for number in numbers_list
    if number % 2 == 0 
]
print("Comprehension List", result)

# Exercise 4: Employee Filtering
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 80000},
    {"name": "Charlie", "salary": 120000}
]
print(employees)
employees_gt7000 = []
for e in employees:
    if e["salary"] > 70000:
        employees_gt7000.append(e)

print(employees_gt7000)

high_earners = [emp for emp in employees if emp["salary"] > 70000]
print("List Comprehension", high_earners)

# Exercise 5: Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
print(numbers)
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print(unique_numbers)

# Mini Project: Todo List application
tasks = []
while True:
    print("\n--- TO-DO APPLICATION ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    if choice == "1":
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f"'{task}' has been added!")
    elif choice == "2":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks available to remove.")
        else:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                # Using pop() to remove by index (subtracting 1 for 0-based indexing)
                removed_task = tasks.pop(task_num - 1)
                print(f"'{removed_task}' has been removed!")
            else:
                print("Invalid task number")
    elif choice == "4":
        print("Exiting application. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")


