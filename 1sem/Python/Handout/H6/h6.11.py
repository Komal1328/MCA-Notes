#h6.11
def fact(n):
    res=1
    for i in range(1,n+1):
        res *= i
    return res
def comb(n,r):
    return (fact(n))/(fact(r) * (fact(n-r)))
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
print("nCr=",comb(n,r)) 
