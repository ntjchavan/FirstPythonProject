
try:

    file = open("files/data.txt", "r")

    content = file.read()

    print(content)

except ValueError as err:
    print(f"Error: {err}")

finally:
    if "file" in locals(): # to check file exists or not
        file.close()


print("\n------------ The with Statement -------------")
with open("files/data.txt", "r") as file:

    content = file.read()

print(content)

print("\n------------ TReading a Specific Number of Characters -------------")
with open("files/data.txt", "r") as file:

    content = file.read(12)

print(content) # O/p: Hello python

print("--------- Reading One Line — readline() ------------")
with open("files/data.txt", "r") as file:
    line = file.readline()

print(line) # O/p: Hello python, returns first line from file data

with open("files/data.txt", "r") as file:
    line = file.readline()
    line = file.readline()

print(line) 
# will return two line from txt file
# Hello python
# welcome to the python programming

print("\n---------- Reading All Lines — readlines() -----------")
with open("files/data.txt", "r") as file:
    lines = file.readlines()

print(lines) # o/p: ['Hello python\n', 'welcome to the python programming\n']

print("--------- write() Doesn't Automatically Add a Newline ---------")
with open("files/write_data.txt", "w", encoding="utf-8") as file:
    file.write("Java")
    file.write("Python\n")
    file.write("C#")

with open("files/write_data.txt", "a", encoding="utf-8") as file:
    file.write("\n\nJava")
    file.write("Python\n")
    file.write("C#")

with open("files/write_data.txt", "r") as file:

    content = file.read()

print(content)
# o/p:
# JavaPython
# C#

# commented because of failing when multiple time run
# print("------------ Create new file -------------")
# with open("files/new_file.txt", "x") as file:
#     file.write("New file data\n hello from python")


try:
    with open(
        "data.txt",
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

        print(content)

except FileNotFoundError:
    print("File does not exist.")

except PermissionError:
    print("You don't have permission to read this file.")
    