
def greet(name):
    """
    This function takes a name as input and prints a greeting message.
    
    Parameters:
    name (str): The name of the person to greet.    
    """
    print(f"Hello, {name}! Welcome to the Python programming world.")

greet("Netaji")
greet("Alice")

def say_hello():
    """
    This function prints a simple hello message.
    """
    print("Hello! How are you today?")

say_hello()

def add_numbers(a, b):
    print(f"The sum of {a} and {b} is: {a + b}")

add_numbers(5, 10)
add_numbers(3.5, 2.3)

def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(4, 5)
print(f"The product of 4 and 5 is: {result}")

def check_age(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."
    
vote_eligibility = check_age(20)
print(vote_eligibility)

print("------------- Functions Returning Multiple Values -------------")
def calculate(a, b):
    return a + b, a - b, a * b

add, minus, mult = calculate(15, 12)
print(add, minus, mult)

def type_safe(a: int, b: int) -> int:
    """
    This function takes two integers as input and returns their sum.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The sum of the two integers.
    """
    return a + b

result = type_safe(10, 20)
print(f"The sum of 10 and 20 is: {result}")

print("------------- Modern Type Hints 3.10+ -------------")
def find_user(name: str) -> str | None:
    """
    This function takes a name as input and returns a greeting message if the name is found.
    
    Parameters:
    name (str): The name of the user to find.
    
    Returns:
    str | None: A greeting message if the user is found, otherwise None.
    """
    users = ["Netaji", "Alice", "Bob"]
    if name in users:
        return f"Hello, {name}! You are found in the user list."
    else:
        return None
    
user = find_user("Alice1")
if user:
    print(user)
else:
    print("User not found.")

print("------------- *args -------------")
def sum_numbers(*numbers):
    """
    This function takes a variable number of arguments and returns their sum.
    
    Parameters:
    *numbers: A variable number of numeric arguments.
    
    Returns:
    int or float: The sum of the provided numbers.
    """
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4, 5))

print("------------- **kwargs -------------")
def print_details(**kwargs):
    """
    This function takes a variable number of keyword arguments and prints them.
    
    Parameters:
    **kwargs: A variable number of keyword arguments.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Netaji", age=25, city="Pune")

print("------------- Combining Parameters, *args, and **kwargs -------------")
def combined_function(a, b, *args, **kwargs):
    """
    This function demonstrates the use of positional parameters, *args, and **kwargs.
    
    Parameters:
    a: The first positional argument.
    b: The second positional argument.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
    """
    print(f"a: {a}, b: {b}")
    print("Additional positional arguments:", args)
    print("Additional keyword arguments:", kwargs["name"], ",", kwargs)

combined_function(1, 2, 3, 4, 5, name="Netaji", age=25)

print("------------- Unpacking Arguments -------------")
numbers = [1, 2, 3, 4, 5]
result = sum_numbers(*numbers)
print(f"The sum of the numbers {numbers} is: {result}")

print("------------- Lambda Functions -------------")
square = lambda number: number * number
print(square(5))

print("----------- Nested Functions -----------")
def outer_function(text):
    """
    This function demonstrates the use of nested functions.
    
    Parameters:
    text (str): The text to be printed by the inner function.
    """
    def inner_function():
        print(f"Inner function says: {text}")
    
    inner_function()

outer_function("Hello from the outer function!")

print("----------- Passing a Function to Another Function -----------")
def greet(name):
    print(f"Hello, {name}!")

def execute_function(function, name):
    function(name)

execute_function(greet, "Alice")
