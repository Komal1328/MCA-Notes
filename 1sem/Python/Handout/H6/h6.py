#h6.1

def out():
    def in_add(a,b):
        return a+b
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    return (in_add(n1,n2)+5)
print("Result: ",out())

#h6.2

lst=[12,34,65,89,34,15,17,16]
rno=int(input("Enter your roll no: "))
print("Present") if(rno in lst) else print("Absent")


#h6.3   
def max2(a,b):
    return a>b
def max3(n1,n2,n3):
    if(max2(n1,n2) and max2(n1,n3)):
            return n1
    elif(max2(n2,n3) and max2(n2,n1)):
            return n2
    else:
        return n3
n1=int(inpur("Enter the 1st number: "))
n2=int(inpur("Enter the 1st number: "))
n3=int(inpur("Enter the 1st number: "))
print("max number: ",max3(n1,n2,n3))


#h6.4

import functools
def add(a,b):
    return a+b
lst=[10,40,50,80]
print("List: ",lst)
res=functools.reduce(add,lst)
print("Sum of elements in list: ",res)

#h6.5

n=int(input("Enter a number "))
i=1
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
print(n," is perfect number") if(sum==n) else print("NOt perfect number")

#h.6

def palindrom(str1):
    flag=0
    for i in range(len(str1)):
        if(str1[i] != str1[len(str1)-1-i]):
            flag = 1
        return flag
str1=input("Enter a String: ")
res=palindrom(str1)
if(res==1):
    print("String is not palindrome")
else:
    print("String is palindrome")   


#h6.7

def sum(arg,*vart):
    sumn=arg
    for var in vart:
        sumn += var
    return sumn
def mul(arg,*vart):
    muln=arg
    for var in vart:
        muln *= var
    return muln
print("Sum of elements in tuple (10,20,40,50)=",sum(10,20,40,50))
print("Multiplication of elements in tuple (1,2,4,5)=",mul(1,2,4,5))

#h6.8

def genrate_n_char(n,ch):
    return n*ch
print("Genrate string=",genrate_n_char(5,'A'))
    

#h6.9
def sumn(n):
    if(n==1):
        return 1
    else:
        return n+sumn(n-1)
n=int(input("Enter the value of n: "))
print("Sum of ",n," numbers: ",sumn(n))

#h6.10

def prime(n,i=2):
    if(n==i):
        return True
    elif(n%i == 0):
        return False
    else:
        return prime(n,i+1)
print("Prime numbers in given range (2,12)")
for i in range(2,12):
    res=prime(i)
    if(res==True):
        print(i,end=" ")



#h6.11
def fact(n):
    res=1
    for i in range(1,n+1):
        res *= i
    return res
def comb(n,r):
    return (fact(n))/(fact(r) * (fact(n-r)))
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
print("nCr=",comb(n,r))    

#h6.12

def fact(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    else:
        return n*fact(n-1)

def fune(n1):
    e=1
    for i in range(1,n1+1):
        e= e+(1 / fact(n1))
    return e

i=int(input("enter the value of n: "))
res=fune(i)
print("Methematical constant e : ",res)

#h6.13


def palindrome(str1):
    for i in range(len(str1)):
        if(str1[i] !=str1[len(str1)-1-i]):
            return False
        else:
            return True
st=input("Enter a sentence: ")
slst=list(st.split(" "))
print(slst)
count=0
for i in slst:
    res=palindrome(i)
    if(res==True):
        count=count+1
    else:
        count=count+0
print("Numbber of palindrome strings are :",count)

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


#h6.15

def lstsum(lst):
    total=0
    for i in lst:
        if(type(i)==list):
            total += lstsum(i)
        else:
            total += i
    return total

lst=[1, 2, [3,4], [5,6]]
print("Sum of list elements",lstsum(lst))
