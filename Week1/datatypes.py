age = 30
print("value of age: ", age)
print("data type of variable age: ", type(age))

number = 123456789123456789123456789123456789
print(number)

a = 20
b = 5
print(f"Minus of {a} & {b}:", a - b)
print(f"Plus of {a} & {b}", a + b)

print("--------- using format --------")
print("Addition of {} & {}: {}".format(a, b, a + b))

print("---------- Float data type --------------")

p = 33.9
print(p)
print(type(p))

print("-------- boolean data type ------------")
isactive = True
ischecked = False
print(isactive); print(ischecked)

print("---------- string data type -------------")
fname = "netaji "
lname = 'chavan' # both are valid single quote & double quote
print(fname, lname);
print("type of lname", type(lname));
print("string concatenate:", lname + " " + fname)
print("string repetition hello * 3:", "hello " * 3)

message = """
    this
    is 
    multiline
    message
""";
print(message)
print("type of multiline message", type(message))

print("----------- None (NoneType),  null (c#) ----------")
manager = None
print(manager)
print(type(manager))
print("Checking for None")
if manager is None:
    print("no manager assigned")

print("-------- Dynamic Typing -------------")
value = 10
print(type(value))

value = "Python"
print(type(value))

value = True
print(type(value))

print("------------ type checking --------------")
salary = 5300
print(salary)
print(type(salary))
print("is integer: ", isinstance(salary, int))
print("is string: ", isinstance(salary, str))

print("------------- assignments ---------------")
name = "netaji"
age = 38
salary = 84000
is_developer = True
manager = None
print(name, " Type: " ,type(name))
print(age, " Type: " ,type(age))
print(salary, " Type: " ,type(salary))
print(is_developer, " Type: " ,type(is_developer))
print(manager, " Type: " ,type(manager))

a = "100"
b = int(a)
print(f"100 * 3: ", b * 3);

c = 500
d = str(c)
print("string concatename: ", d + " INR")

f = None
if f is None:
    print("variable is none")
else:
    print("variable value is: ", f)

