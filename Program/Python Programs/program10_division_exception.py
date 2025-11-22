# Program 10: Program to handle division by zero using try-except

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print("Result:", c)
except ZeroDivisionError:
    print("Error! Cannot divide by zero")
except ValueError:
    print("Error! Please enter valid numbers")
