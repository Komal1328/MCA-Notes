try:
    tfile=open("test.txt",'r')
    l1=tfile.readline()
    print(l1)
    
except IOError:
    print("can't find file or read data")
else:
    print("written into file")
