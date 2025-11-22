# Program 14: Program to check if a string is palindrome using stack logic

string = input("Enter a string: ")
stack = []

for char in string:
    stack.append(char)

reverse = ""
while len(stack) > 0:
    reverse = reverse + stack.pop()

if string == reverse:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
