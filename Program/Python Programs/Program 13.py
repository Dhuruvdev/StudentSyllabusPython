# Program 13: Stack implementation with push and pop

stack = []

def push():
    item = input("Enter element: ")
    stack.append(item)
    print(item, "pushed")

def pop():
    if stack:
        print(stack.pop(), "popped")
    else:
        print("Stack empty")

def display():
    print("Stack:", stack)

while True:
    print("\n1. Push  2. Pop  3. Display  4. Exit")
    choice = int(input("Choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
