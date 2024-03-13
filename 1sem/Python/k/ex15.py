queue = []

def enqueue():
    elem = int(input("Enter the element: "))
    queue.append(elem)
    print("Element inserted.")

def dequeue():
    if(len(queue)==0):
        print("Queue is empty.")
    else:
        print("Deleted elemtent is:", queue.pop(0))

def display():
    if(len(queue)==0):
        print("Queue is empty.")
    else:
        for i in queue:
            print(i, end = " ")
        print()

print("queue operations using lists")
print("--------------------------------\n")
while(True):
    choice = int(input("Enter your choice: \n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\n"))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
