#pr4

cs=0
cd=0
str1=input("enter a string: ")
for i in str1:
    if(i==" "):
        continue
    elif(i.isdigit()):
        cd += 1
    elif(i.isalpha()):
        cs += 1
print("Number of digits: ",cd)
print("Number of letters: ",cs)
