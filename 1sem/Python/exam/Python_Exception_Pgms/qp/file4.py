#exe4
file=input("enter a file name")
with o
pen(file,"r") as f:
    content=f.read()
    cl=len(content.split("\n"))
    cw=len(content.split())
    cc=len(content)

print(cl)
print(cw)
print(cc)
