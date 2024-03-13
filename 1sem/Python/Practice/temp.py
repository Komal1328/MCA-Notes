import math
def fact(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

def valE(n):
    e = 0
    i=0
    for i in range(i,n):
        e += 1/fact(i)
    return e
n=int(input("enter a number"))
print("Computed e:",valE(n))
print("Actual e:",math.e)
