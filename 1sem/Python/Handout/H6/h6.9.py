#h6.9
def sumn(n):
    if(n==1):
        return 1
    else:
        return n+sumn(n-1)
n=int(input("Enter the value of n: "))
print("Sum of ",n," numbers: ",sumn(n))
