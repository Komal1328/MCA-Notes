#pr1

name=(input("Enter your name: "))
sem=int(input("Enter semester: "))
m1,m2,m3,m4,m5,m6=input("Enter 6 subjects marks out of 100: ").split()
m1=int(m1)
m2=int(m2)
m3=int(m3)
m4=int(m4)
m5=int(m5)
m6=int(m6)

tot=(m1+m2+m3+m4+m5)
per=(tot/600)*100
print("Total: ",tot)
print("Percentage: ",per)
if(per>80):
    print("A grade")
elif(per>60 and per<=80):
    print("B grade")
elif(per>50 and per<=60):
    print("C grade")
elif(per>45 and per<=50):
    print("D grade")
elif(per>25 and per<=45):
    print("E grade")
elif(per<25):
    print("F grade")

#pr 3

num=int(input("Enter the a number: "))
count=0
sumn=0
dig=0
while(num!=0):
    dig=(num%10)
    sumn += dig
    count += 1
    num = int(num/10)

print("Sum of digits: ",sumn)
print("Number of digits: ",count)

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

#pr 5

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(0,4):
    for j in range(4-i,0,-1):
        print("*",end=" ")
    print()


#pr6

str1=input("enter a string:").lower()
print(str1)

def palindrome(str1):
    for i in range(len(str1)):
        if(str1[i] != str1[len(str1)-1-i]):
            return False
    return True

if(palindrome(str1)):
    print("Palindrome")
else:
    print("Not Palindrome")

#pr7

lst=[]
lstp=[]
def prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
    
print("Enter numbers: ")
while(True):
    n=int(input(" "))
    if(n==0 or n==-1):
        break
    elif(prime(n)):
        lstp.append(n)
    else:
        lst.append(n)
        
print("Prime numbers :",lstp)
print("non prime numbers: ",lst)

#pr8

import math
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def econst():
    e=0
    for i in range(0,10):
        e=1/fact(i)
    return e

print("Computed e: ",econst())
print("actual e: ",math.e)


#pr13

str1=input("Enter a string: ").lower()
str2=input("Enter a sub string: ").lower()
count=str1.count(str2)
print(count)


#pr17

def max2(a,b):
    if(a>b):
        return a
    
def max3(a,b,c):
    if(max2(a,b) and max2(a,c)):
        return a
    elif(max2(b,a) and max2(b,c)):
        return b
    else:
        return c

print(max3(500,200,30))
    

#pr18

val=lambda x:(x!=0)
odd=lambda x:x%2!=0
s=lambda x,y: x+y
sodd=lambda x,y : ((x+y)%2!=0)
prod=lambda x,y,z: (x*y)<=z

print(val(3))
print(odd(5))
print(s(20,100))
print(sodd(7,2))
print("prod",prod(2,2,3))


#pr19

lst1=[20,10,30,60,80]
lst2=[10,30,57,20,100]
ints=[]
for i in lst1:
    if(i in lst2):
        ints.append(i)
print(ints)


#pr20

def fact(num):
    if(num==0):
        return 1
    else:
        return num*(fact(num-1))


n=int(input("Enter value of n: "))
r=int(input("Enter value of r: "))
c=(fact(n))/(fact(r)*fact(n-r))
print(c)


