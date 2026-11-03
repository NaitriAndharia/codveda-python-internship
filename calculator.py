
# Simple Calculator
# Codveda Technologies Internship

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


print("===== SIMPLE CALCULATOR =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Result:", addition(num1, num2))

elif choice == "2":
    print("Result:", subtraction(num1, num2))

elif choice == "3":
    print("Result:", multiplication(num1, num2))

elif choice == "4":
    print("Result:", division(num1, num2))

else:
    print("Invalid Choice!")
