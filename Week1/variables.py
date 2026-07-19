
x = 10
firstname = "netaji"
lastname = "chavan"
isworking = True

print(x)
print(firstname)
print(lastname)
print(isworking)

print("--------variable data types-------")
print("x ", type(x))
print(type(firstname))
print(type(lastname))
print(type(isworking))

print("------ data type change ------")
y = 10
print("value of y: ", y, ", and data type: ", type(y))

y = "testing data type change"
print("value of y: ", y, ", and data type: ", type(y))

print("--------------- Assignments -----------------")
yourname = "Netaji Chavan"
yearofexp = 2
city = "Delhi"
iscurrentlyworking = True
print("Your Name: ", yourname, ", Year of Exp:", yearofexp, ", City: ", city, ", Is Currently Working:", iscurrentlyworking)

x = 10
y = 20
print("Before swapping x & y: ", x, y)

x = x + y # x = 30 (10 + 20)
y = x - y # y = 10 (30 - 20)
x = x - y # x = 20 (30 - 10)

print("After swapping x & y: ", x, y)

x = y = z = 100
print("value of x, y, z", x, y, z)