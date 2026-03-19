# Grocery Bill Calculator

item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))
total = item1 + item2 + item3
print("Total Bill =", total)

# Petrol Cost Calculator

litres = float(input("Enter litres filled: "))
price_per_litre = float(input("Enter price per litre: "))
total_cost = litres * price_per_litre
print("Total Petrol Cost =", total_cost)

# Student Marks & Percentage

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))
total = maths + science + english
percentage = total / 3
print("Total =", total)
print("Percentage =", percentage)

#Integer (int)

age = 21
marks = 95
year = 2026

price = 99.99
temperature = 36.5
percentage = 87.6

name = "Likhitha"
city = "Visakhapatnam"
email = "likhithakudipudi1172004@gmail.com"

is_student = True
is_logged_in = False

num = 3 + 5j

a = 10
b = float(a)
print(b)  # 10.0

a = 9.8
b = int(a)
print(b)  # 9

a = 25
b = str(a)
print(b)
print(type(b))

a = "100"
b = int(a)
print(b + 50)

a = "hello"
b = int(a)  # ERROR

print(int(True))   # 1
print(int(False))  # 0

name = input("Enter your name: ")
print("Hello", name)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)

name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))

print(name, age, height)

name = "Likhitha"
age = 20

print("Name:", name)
print("Age:", age)
