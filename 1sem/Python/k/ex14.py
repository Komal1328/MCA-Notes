stack = []

def push():
    elem = int(input("Enter the element: "))
    stack.append(elem)
    print("Element inserted.")

def pop():
    if(len(stack)==0):
        print("Stack is empty.")
    else:
        print("Deleted elemtent is:", stack.pop())

def display():
    if(len(stack)==0):
        print("Stack is empty.")
    else:
        for i in stack:
            print(i, end = " ")
        print()

print("Stack operations using lists")
print("--------------------------------\n")
while(True):
    choice = int(input("Enter your choice: \n1. Push\n2. Pop\n3. Display\n4. Exit\n"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
