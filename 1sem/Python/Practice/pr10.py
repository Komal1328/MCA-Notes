#pr10

div=lambda x:x%3==0

lst=[i for i in range(1,11)]
print("number divisible by 3 in range (1,11):",list(filter(div,lst)))

def prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

lst1=[i for i in range(0,50) if(prime(i))]
print("List of prime numbers between range(0,15):")
print(lst1)
