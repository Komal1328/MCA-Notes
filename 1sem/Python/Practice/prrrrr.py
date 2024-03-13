lst1=[i for i in range(1,11)]
div=lambda x:x%3 == 0
print(list(filter(div,lst1)))

def prime(n):
    if(n<=1):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
    return True

lst2=[i for i in range(0,50) if(prime(i))]
print((lst2))

