#fp4

def prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

lst=[2,3,4,5,6,78,9]
print("prime numbers: ",list(filter(prime,lst)))
