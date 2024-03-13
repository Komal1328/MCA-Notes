#h6.7

def sum(arg,*vart):
    sumn=arg
    for var in vart:
        sumn += var
    return sumn
def mul(arg,*vart):
    muln=arg
    for var in vart:
        muln *= var
    return muln
print("Sum of elements in tuple (10,20,40,50)=",sum(10,20,40,50))
print("Multiplication of elements in tuple (1,2,4,5)=",mul(1,2,4,5))
