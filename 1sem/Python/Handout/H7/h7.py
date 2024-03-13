#h7.1

import functools
odd=lambda x: (x%2!=0) 
even=lambda x:(x%2==0)
sqr=lambda x:(x**2)
cube=lambda x:(x**3)
large=lambda x: (x+2)
div=lambda x:(x%3==0)
div3=lambda x:(x%3==0 and x%7!=0)
add=lambda x,y:(x+y)
large1=lambda x: (x+1)

A=[1,2,4,5,6,7,9,21]
print("Original list ",A)
print("List of odd numbers",list(filter(odd,A)))
print("List of even numbers",list(filter(even,A)))
print("List of square of numbers",list(map(sqr,A)))
print("List of cube of numbers",list(map(cube,A)))
print("List of numbers larger by 2 ",list(map(large,A)))
print("List of numbers divisible by 3 ",list(filter(div,A)))
print("List of numbers divisible by 3 but not by 7 ",list(filter(div3,A)))
print("Sum of list ",functools.reduce(add,A))
print("List of numbers larger by 1 ",list(map(large1,A)))


#h7.3

import functools

mul=lambda x:(x*2)
n=int(input("Enter a number: "))
print("A:",mul(n))

words = ["mary", "had", "a", "little", "lamb"]
large=functools.reduce(lambda a,b:a if a>b else b,words)
print("largest of words is:",large)

sumn=0
for i in range(1,101):
    sumn=sumn+i
print("Sum of 100 numbers:",sumn)

#h7.4

def even(n):
    if(n%2==0):
        return True
    else:
        return False
seq=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(even,seq))
print("Even numbers from range (1,10): ",res)
