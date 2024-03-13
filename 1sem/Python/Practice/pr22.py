#pr22

file=input("Enter a file name: ")
str1=input("Enter a string want to find:")
match_line=[]
with open(file,"r") as f:
    content=f.read()
    lines=content.split("\n")
    for i in lines:
        if(str1 in i):
            match_line.append(i)

for i in match_line:
    print(i)
