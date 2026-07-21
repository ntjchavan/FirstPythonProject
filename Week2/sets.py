
languages = { "Python", "Java", "C#", "Ruby", "Go"}

print(languages)

# Why Use a Set?
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers) # output: {1, 2, 3, 4, 5}

# Creating Sets
# Using curly braces: 
fruits = {"Apple", "Banana", "Orange"}
print(fruits)

# Or using the constructor:
numbers = set([1, 2, 3, 3, 4, 5, 5])
print(numbers) # output: {1, 2, 3, 4, 5}

# Membership Testing
languages = { "Python", "Java", "C#", "Ruby", "Go"}
print("Python" in languages) # True

# Set Union : Union combines all unique elements.
frontend = {"HTML", "CSS", "JavaScript" }
backend = { "Python", "Java", "JavaScript" }
all_skills = frontend | backend
print(all_skills) # {'Java', 'Python', 'JavaScript', 'HTML', 'CSS'}

# Set Intersection : Common elements only.
common_skills = frontend & backend
print(common_skills) # {'JavaScript'}

# Set Difference
print(set(frontend - backend)) # {'HTML', 'CSS'}
print(set(backend - frontend)) # {'Java', 'Python'}

print("-------------- Practice Exercises ---------------")
# Exercise 1
programming_languages = {"Python", "Java", "C#", "JavaScript"}
programming_languages.add("Go")
programming_languages.remove("Java")
print(programming_languages)

# Exercise 2 - Convert it to a set and print only unique numbers.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

# Exercise 3 - 
team_a = {"Python", "Java", "SQL"}
team_b = {"Python", "Docker", "AWS"}

# All skills (union)
# Common skills (intersection)
# Skills only in Team A (difference)
print(set(team_a | team_b))
print(set(team_a & team_b))
print(set(team_a - team_b))

# Exercise 4 - 
# Create a set containing numbers from 1 to 20.
# Using a set comprehension, create another set containing only even numbers.
numbers = {n for n in range(1, 21)}
print(numbers)
print(type(numbers))

even_numbers = {n for n in range(1, 21) if n % 2 == 0}
print(even_numbers)

print("------------- Mini Project: Student Attendance -------------------")
day1 = {
    "Alice",
    "Bob",
    "Charlie"
}

day2 = {
    "Bob",
    "Charlie",
    "David"
}

# Calculate:
# Students who attended both days.
# Students who attended only Day 1.
# Students who attended only Day 2.
# Total unique students.
common_attendiees = set(day1 & day2)
print("Common Attendiees", common_attendiees)

only_day1 = set(day1 - day2)
print("Only day 1", only_day1)

only_day2 = set(day2 - day1)
print("Only day 2", only_day2)

total_unique_students = set(day1 | day2)
print("Total Unique Students", total_unique_students)
# for ca in common_attendiees:
