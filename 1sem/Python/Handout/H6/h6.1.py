#h.1

def out():
    def in_add(a,b):
        return a+b
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    return (in_add(n1,n2)+5)
print("Result: ",out())
