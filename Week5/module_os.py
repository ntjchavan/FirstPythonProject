# why need os
# -> Python programs sometimes need to communicate with the operating system.


import os

# Get Current Working Directory

current_directory = os.getcwd()

print(current_directory) # D:\Projects\Git\FirstPythonProject\Week5

# List Files and Directories
items = os.listdir()

print(items)
# ['application.log', 'custom_exception.py', 'files', 'file_csv.py', 'file_handling.py', 
#  'file_json.py', 'file_xml.py', 'logger_test.py','module_os.py', 'module_pathlib.py', 'raise.py', 
#  'try_except_finally.py', '__pycache__']

# Check Whether It Is a File
if os.path.isfile("files/data.txt"):
    print("\nThis is a file")
else:
    print("\nThis is not a file")


# Join Paths with os.path.join()
path = os.path.join(
    "files",
    "employee.xml"
)

print(path) # files\employee.xml

# Get File Extension
print("\n---------- Get File Extension -----------")

path = "files\employee.xml"
name, extension = os.path.splitext(path)

print(name) # files\employee
print(extension) # .xml

# Reading an Environment Variable
environment = os.environ.get("APP_ENV")
print(environment)

# List All Environment Variables
print("\n---------------- List all environment variables --------------")
for key, value in os.environ.items():
    print(key, "=", value)
    
