
import xml.etree.ElementTree as ET

# Creating XML in Python
root = ET.Element("employee")

id_element = ET.SubElement(
    root,
    "id"
)

id_element.text = "101"

name_element = ET.SubElement(
    root,
    "name"
)

name_element.text = "Netaji"

department_element = ET.SubElement(
    root,
    "department"
)

department_element.text = "IT"

tree = ET.ElementTree(root)

tree.write("files/employee.xml", encoding="utf-8", xml_declaration=True)

print("XML file created")

# Reading XML from a File
print("\n------------ Reading XML file -----------")
tree = ET.parse("files/employee.xml")

root = tree.getroot()

print(root.tag) # employee
print(root.find("id").text)
print(root.find("name").text)

# Complete XML example
print("\n------------ Complete XML example -----------")

root = ET.Element("employees")

employees = [
    {
        "id": "101",
        "name": "Rahul",
        "department": "IT",
        "salary": "75000"
    },
    {
        "id": "102",
        "name": "Amit",
        "department": "HR",
        "salary": "65000"
    },
    {
        "id": "103",
        "name": "Priya",
        "department": "Finance",
        "salary": "80000"
    }
]

for employee_data in employees:

    employee = ET.SubElement(
        root,
        "employee",
        {"id": employee_data["id"]}
    )

    name = ET.SubElement(
        employee,
        "name"
    )
    name.text = employee_data["name"]

    department = ET.SubElement(
        employee,
        "department"
    )
    department.text = employee_data["department"]

    salary = ET.SubElement(
        employee,
        "salary"
    )
    salary.text = employee_data["salary"]

tree = ET.ElementTree(root)

ET.indent(tree, space="    ")

tree.write(
    "files/employees_data.xml",
    encoding="utf-8",
    xml_declaration=True
)
print("Complete XML created")


print("\n---------- Reading XML created")
try:
    tree = ET.parse("files/employees_data.xml")

    root = tree.getroot()

    for employee in root.findall("employee"):

        employee_id = employee.get("id")
        name = employee.find("name").text
        department = employee.find("department").text
        salary = employee.find("salary").text

        print(
            f"{employee_id} - "
            f"{name} - "
            f"{department} - "
            f"{salary}"
        )
except Exception as err:
    print(f"Error: {err}")