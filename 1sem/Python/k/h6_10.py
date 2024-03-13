def isPrime(n):
     for i in range(2,int(n**0.5)+1):
          if(n%i==0):
               return False
     return True
def primeRange(n1,n2):
     if(n1==n2):
          return
     if(isPrime(n1)):
          print(n1)
     primeRange(n1+1,n2)

n1 = int(input("Enter the value of n1: "))
n2 = int(input("Enter the value of n2: "))
primeRange(n1,n2)
