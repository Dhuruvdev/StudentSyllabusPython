# Program 12: Display Fibonacci sequence using loop

terms = int(input("Enter number of terms: "))
a, b = 0, 1

print("Fibonacci:")
for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print()
