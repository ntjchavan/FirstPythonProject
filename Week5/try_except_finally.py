try:
    number = int(input("Enter number: "))

    print("\nEntered number: ", number)

except ValueError as err:
    print(f"\nError: {err}")
finally:
    print("Finally block")


try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    result = num1 / num2

    print(f"Division of number {num1} & {num2}: {result:.0f}")

except ValueError as err:
    print(f"Error: {err}")
except ZeroDivisionError as err:
    print(f"Error: {err}")

finally:
    print("Completed block")


def test():
    try:
        print(f"\nIn Test method")
        number = int(100)

        return "success"
    
    except ValueError as err:
        print(f"Error: {err}")

    finally:
        print("Finally block")

print(test())

