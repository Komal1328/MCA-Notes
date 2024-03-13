q=[]
def enqueue():
    if(len(q)==3):
        print("Queue is full")
    else:
        ele=int(input("enter element to be inserted:"))
        q.append(ele)

def dequeue():
    if(len(q)==0):
        print("Queue is empty")
    else:
        print("Deleted element is: ",q.pop(0))

def display():
    if(len(q)==0):
        print("Queue is empty")
    else:
        print("Queue elements are: ")
        for i in q:
            print(i)


print("Queue operations")
print("1.Insert 2.Delete 3.DISPLAY 4.EXIT")
while(True):
    ch=int(input("Enter your choice: "))
    if(ch==1):
        enqueue()
    elif(ch==2):
        dequeue()
    elif(ch==3):
        display()
    elif(ch==4):
        break
    else:
        print("enter valid choice")
