num = int(input("Enter the number"))
nsum = 0
for i in range (1,num):
     if(num%i==0):
          nsum += i
if(nsum==num):
     print("Perfect number")
else:
     print("Not perfect number")
