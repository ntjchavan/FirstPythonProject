# dumps -> Python object -> JSON string
# loads -> JSON string -> Python object

# dump  -> Python object -> JSON file
# load  -> JSON file -> Python object


import json

# python object
employee = {
    "id": 1,
    "name": "Netaji",
    "department": "IT"
}

json_data = json.dumps(employee)

print(json_data) # {"id": 1, "name": "Netaji", "department": "IT"}


try:
    with open("files/config.json", "r", encoding="utf-8") as file:

        config = json.load(file)

    print(config["application"]["name"]) # Bank Application
except FileNotFoundError as err:
    print(f"File Not found: {err}")

except json.JSONDecodeError as err:
    print(f"Invalid JSON file: {err}")

# writing JSON file
employees = {
    "employees": [
        {
            "id": 101,
            "name": "Rahul",
            "department": "IT",
            "salary": 75000
        },
        {
            "id": 102,
            "name": "Amit",
            "department": "HR",
            "salary": 65000
        },
        {
            "id": 103,
            "name": "Priya",
            "department": "Finance",
            "salary": 80000
        }
    ]
}

try:
    with open("files/employees.json", "w", encoding="utf-8") as file:

        json.dump(employees, file, indent=4)

    print("Store data in file")

except FileNotFoundError as err:
    print(f"File not found: {err}")
    
except json.JSONDecodeError as err:
    print(f"Invalid JSON file: {err}")

# reading JSON file
print("\n----------- Read employee file data")
try:
    with open("files/employees.json", "r", encoding="utf-8") as file:

        data = json.load(file)

    for employee in data["employees"]:
        print(
            f"{employee["id"]} - "
            f"{employee["name"]} "
        )

except FileNotFoundError as err:
    print(f"File not found: {err}")
    
except json.JSONDecodeError as err:
    print(f"Invalid JSON file: {err}")