#h6.5

n=int(input("Enter a number "))
i=1
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
print(n," is perfect number") if(sum==n) else print("NOt perfect number")
