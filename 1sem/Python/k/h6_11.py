def fact(n):
     res = 1
     for i in range(1,n+1):
          res *= i
     return res
def combination(n,r):
     return(fact(n)/(fact(r)*(fact(n-r))))

n = int(input("Enter the value of n "))
r = int(input("Enter the value of r "))
print(combination(n,r))
