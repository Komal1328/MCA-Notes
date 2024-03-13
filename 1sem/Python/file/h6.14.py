#h6.14

def compute(str1):
    cntd=0
    cntu=0
    cntl=0
    for i in str1:
        if(i==" "):
            continue
        elif (i.isdigit()):
            cntd=cntd+1
        else:
            if(i.isupper()):
                cntu= cntu+1
            else:
                cntl=cntl+1
    return cntd,cntu,cntl

st=input("Enter a string:")
nd,nu,nl=compute(st)
print("Number of digits in string: ",nd)
print("Number of Upper case letters in string: ",nu)
print("Number of lower case letters in string: ",nl)
