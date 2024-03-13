#file10
file=input("enter a file name")
lst=[]
with open(file,"r") as f:
    c=f.readlines()
    print("1st 5 lines")
    for i in (c[:5]):
        print(i)
        
    print("last 5 lines")
    for line in (c[-5:]):
        print(line)





