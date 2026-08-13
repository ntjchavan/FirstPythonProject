
import csv

try:
    with open("files/students.csv", "r", encoding="utf-8") as file:

        reader = csv.reader(file)

        next(reader) # to skip header

        for row in reader:
            print(row)

except Exception as err:
    print(f"Error: {err}")


# DictReader : read data in dictionary

try:
    with open("files/students.csv", "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)

except Exception as err:
    print(f"Error: {err}")


# Writing a CSV file
# with  newline="", data like below
# id,name,age,department
# 1,Netaji,23,IT
# 2,Punam,18,HR

# without  newline="", data like below
# id,name,age,department

# 1,Netaji,23,IT

# 2,Punam,18,HR


try:

    with open("files/employees.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "id", "name", "age", "department"
        ])

        writer.writerow(
            [1, "Netaji", 23, "IT"]
        )
        writer.writerow(
            [2, "Punam", 18, "HR"]
        )

        print("Employee CSV created!")
        

except Exception as err:
    print(f"Error: {err}")
