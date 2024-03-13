#part A
lst = [i for i in range(1,11)]
print(lst)

div3 = lambda x: x%3==0

lst = list(filter(div3, lst))
print(lst)

#part B
def isPrime(num):
    if(num<=1):
        return False
    for i in range(2,int(num**0.5) + 1):
        if(num%i==0):
            return False
    return True
lst2 = [i for i in range(0,50) if(isPrime(i))]
print(lst2)