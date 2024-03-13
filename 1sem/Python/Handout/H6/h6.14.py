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
    print("Number of digits in string: ",cntd)
    print("Number of Upper case letters in string: ",cntu)
    print("Number of lower case letters in string: ",cntl)

st=input("Enter a string:")
compute(st)
