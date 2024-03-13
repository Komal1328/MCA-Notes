#pr19

lst1=[20,10,30,60,80]
lst2=[10,30,57,20,100]
ints=[]
for i in lst1:
    if(i in lst2):
        ints.append(i)
print(ints)
