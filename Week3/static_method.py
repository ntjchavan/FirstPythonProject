class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(Calculator.add(10, 20))
print(Calculator.multiply(5, 12))

print("--------------- Complete Example ----------------")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name} - INR {self.price}")

    @staticmethod
    def discount(price, percent):
        return price - (price * percent / 100)

product = Product("Laptop", 50000)
product.show()

new_price = product.discount(50000, 10)
print(new_price)

print("-------------- Practice Exercise ---------------")
class Converter:
    @staticmethod
    def km_to_meter(km):
        return km * 1000

    @staticmethod
    def meter_to_km(meter):
        return meter / 1000

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(Converter.km_to_meter(5))
print(Converter.meter_to_km(2500))
print(Converter.celsius_to_fahrenheit(30))

