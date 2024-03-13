file=input("enter a file name")
str1=input("enter a sub string")
lst=[]
with open(file,"r") as f:
    content=f.read()
    line=content.split('\n')
    
    for i in line:
        if(str1 in i):
            lst.append(i)
for i in lst:
    print(i)
