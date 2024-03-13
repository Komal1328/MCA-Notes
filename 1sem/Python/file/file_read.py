fo=open("Sample.txt1","r+")
print("Name of the file: ",fo.name)


str1=fo.read()
print("Read String1 is : ",str1)

fo.write("Welcome")
fo.seek(0)  #pointer strat pointing at starting of the file 
str2=fo.read(10)
print("Read String2 is : ",str2)
fo.close()

