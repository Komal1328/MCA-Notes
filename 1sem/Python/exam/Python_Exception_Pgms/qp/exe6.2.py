#exe6.2
try:
    file=input("Enter a file name")
    with open(file,"r") as f:
        print(len(f.read()))
    #f=open("text","r")

except IOError:
    print(file," file does not exists")
