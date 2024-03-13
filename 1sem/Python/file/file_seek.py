fo=open("Sample.txt1","r+")
str1=fo.read()
print("Read String1 is : ",str1)

position=fo.tell()
print("Current file position: ",position)
position=fo.seek(0,0)
str1=fo.read(10)
print("Again reading : ",str1)
fo.close
