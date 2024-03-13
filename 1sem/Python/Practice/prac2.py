stack=[]
def push():
    if(len(stack)==3):
        print("Stack is full")
    else:
        ele=int(input("Enter an element to be inserted:"))
        stack.append(ele)

def pop():
    if(len(stack)==0):
        print("Stack is empty")
    else:
        print("Deleted element is : ",stack.pop())

def display():
    if(len(stack)==0):
        print("stack is empty")
    else:
        print("Stack elements are: ")
        for i in stack:
            print(i)

print("Stack operations")
print("1.PUSH 2.POP 3.DISPLAY 4.EXIT")
while(True):
    ch=int(input("Enter your choice: "))
    if(ch==1):
        push()
    elif(ch==2):
        pop()
    elif(ch==3):
        display()
    elif(ch==4):
        break
    else:
        print("enter valid opetion")
