# Program 10: Handle division by zero with try-except

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error! Cannot divide by zero")
except ValueError:
    print("Error! Enter valid numbers")
