# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
    f.write("Hello World!!!")


# Python code to illustrate with()
with open("file.txt") as file: 
    data = file.read()
# do something with data
print(data)
