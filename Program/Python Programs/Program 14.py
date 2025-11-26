# Program 14: Check if string is palindrome using stack

string = input("Enter a string: ")
stack = []

for ch in string:
    stack.append(ch)

reverse = ""
while stack:
    reverse += stack.pop()

if string == reverse:
    print(string, "is palindrome")
else:
    print(string, "is not palindrome")
