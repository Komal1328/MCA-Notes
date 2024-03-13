#pr8

import math
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def econst():
    e=0
    for i in range(0,10):
        e=1/fact(i)
    return e

print("Computed e: ",econst())
print("actual e: ",math.e)
