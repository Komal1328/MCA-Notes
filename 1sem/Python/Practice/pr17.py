#pr17

def max2(a,b):
    if(a>b):
        return a
    
def max3(a,b,c):
    if(max2(a,b) and max2(a,c)):
        return a
    elif(max2(b,a) and max2(b,c)):
        return b
    else:
        return c

print(max3(500,200,30))
    
