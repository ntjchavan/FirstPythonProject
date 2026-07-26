name = "Netaji"
print(name)

# String Slicing
print(name[1:4]) # eta

# Removing Whitespace
name = "      netaji chavan   "
print(name.strip())

# Checking String Content
print("name".isalpha())
print("name".isdigit())

# The format() Method
name = "Netaji"
age = 35
message = "My name is {} and I am {} years old".format(name, age)
print(message)

print("---------- Practice Exercises --------------")
text = "    Python is Awesome      "
print(text.strip())
print(text.strip().upper())

# Word Count
text = "python java python csharp python"
word_counts = {}
for t in text.split():
    word_counts[t] = word_counts.get(t, 0) + 1

print(word_counts)

# Extract Numbers
text = "There are 25 apples and 10 oranges."
numbers = [int(word) for word in text.split() if word.isdigit()]
print(numbers)

print("-------------- Mini Project: Log Analyzer ---------------")
logs = """
INFO User logged in
ERROR Database connection failed
INFO User viewed dashboard
WARNING Disk space low
ERROR Timeout occurred
"""
log_counts = {}
errors = []

# process line by line
for line in logs.strip().splitlines():
    if not line:
        continue

    # split into two parts, level and message
    level, message = line.split(" ", 1)

    # increment count using dict.get() to safely handle new keys
    log_counts[level] = log_counts.get(level, 0) + 1

    # track error message seperately
    if level == "ERROR":
        errors.append(message)

# print logs
for level, count in log_counts.items():
    print(level, count)

# print errors
print("\nErrors")
for err in errors:
    print(err)
