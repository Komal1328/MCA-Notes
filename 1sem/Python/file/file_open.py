fo=open("Sample.txt1","w")
print("Name of the file: ",fo.name)
print("Closed or not",fo.closed)
print("Openung mode:",fo.mode)

fo.close()
print("Closed or not",fo.closed)
