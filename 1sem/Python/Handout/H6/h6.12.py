#h6.12

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    return fact

def fune(n1):
    e=0
    i=0
    for i in range(i,n1):
        e= e+(1 / fact(i))
    return e

i=int(input("enter the value of n: "))
res=fune(i)
print("Methematical constant e : ",res)
