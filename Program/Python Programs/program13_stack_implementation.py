# Program 13: Implement a stack using list with push() and pop() operations

stack = []

def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(element, "pushed to stack")

def pop():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        element = stack.pop()
        print(element, "popped from stack")

def display():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Stack elements:", stack)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice!")
