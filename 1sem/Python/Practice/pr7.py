#pr7

lst=[]
lstp=[]
def prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
    
print("Enter numbers: ")
while(True):
    n=int(input(" "))
    if(n==0 or n==-1):
        break
    elif(prime(n)):
        lstp.append(n)
    else:
        lst.append(n)
        
print("Prime numbers :",lstp)
print("non prime numbers: ",lst)
