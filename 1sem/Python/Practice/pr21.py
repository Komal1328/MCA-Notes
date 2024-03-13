#pr21

file=input("Enter a file name: ")
with open(file,"r") as f:
    content=f.read()
    cline=len(content.split("\n"))
    cword=len(content.split())
    cchar=len(content)

print(cline)
print(cword)
print(cchar)
