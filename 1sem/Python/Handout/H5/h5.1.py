n=int(input("Enter the value of n: "))
mydict={}
for i in range(1,n+1):
    mydict.update({i:i*i})
print("Result: ",mydict)
