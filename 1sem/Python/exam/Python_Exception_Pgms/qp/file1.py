#file1
file=input("enter a file name")
lst=[]
with open(file,"r") as f:
    content=f.read()
    line=content.split('\n')
    
    for i in line:
        if("#" in i):
            lst.append(i)
for i in lst:
    print(i)
