#h6.10

def prime(n,i=2):
    if(n==i):
        return True
    elif(n%i == 0):
        return False
    else:
        return prime(n,i+1)
print("Prime numbers in given range (2,12)")
for i in range(2,12):
    res=prime(i)
    if(res==True):
        print(i,end=" ")
