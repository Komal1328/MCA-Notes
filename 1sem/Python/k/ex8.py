import math
def fact(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

def valE():
    e = 0
    for i in range(10):
        e += 1/fact(i)
    return e
    
print("Computed e:",valE())
print("Actual e:",math.e)