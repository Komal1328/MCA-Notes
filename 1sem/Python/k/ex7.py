def isPrime(num):
    if(num<=1):
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if(num%i==0):
                return False
    return True

prime_lst = []
lst = []
while(True):
    num = int(input("Enter values (0/-1 to exit): "))
    if(num == 0 or num == -1):
        break
    elif(isPrime(num)):
        prime_lst.append(num)
    else:
        lst.append(num)

print(prime_lst)
print(lst)

