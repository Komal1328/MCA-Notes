# Open a file
fo = open("Sample.txt", "w")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
# Close a file
fo.close()
print ("Closed or not : ", fo.closed)



