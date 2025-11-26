# Program 9: Calculate factorial using loop

num = int(input("Enter a number: "))
result = 1

for i in range(1, num + 1):
    result = result * i

print("Factorial:", result)
