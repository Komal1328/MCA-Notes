# READ
# Open a file
fo = open("Sample.txt", "r+")
str2 = fo.read(10)
str1= fo.read()

print ("Read String is : ", str1)
print ("Read String is : ", str2)
# Close opened file
fo.seek(0)
fo.write("Welcome")
fo.close()
