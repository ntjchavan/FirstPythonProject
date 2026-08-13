# parents=True means:
# Create parent directories if they don't already exist.

# exist_ok=True means:
# Create it if necessary, but don't raise an error if it already exists.

# File Stem
# The stem is the filename without the extension.

from pathlib import Path

path = Path("files/employees.json")

print(path) # files\employees.json

# files\employees.json
print(Path.cwd()) # file that with drive like D:\

if path.exists:
    print(f"Path exists: {path}")
else:
    print("Path not found")


# Important Path Properties

path = Path(
    "data/employees/employees.csv"
)

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

# Result
# name   -> employees.csv
# stem   -> employees
# suffix -> .csv
# parent -> data/employees

# Get File Extension
print("\n---------- Get File Extension -----------")

path = Path("files\employees.csv")

print(path.stem) # employees
print(path.suffix) # .csv
