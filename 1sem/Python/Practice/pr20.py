#pr20

def fact(num):
    if(num==0):
        return 1
    else:
        return num*(fact(num-1))


n=int(input("Enter value of n: "))
r=int(input("Enter value of r: "))
c=(fact(n))/(fact(r)*fact(n-r))
print(c)

