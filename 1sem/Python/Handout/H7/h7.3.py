#h7.3

import functools

mul=lambda x:(x*2)
n=int(input("Enter a number: "))
print("A:",mul(n))

words = ["mary", "had", "a", "little", "lamb"]
large=functools.reduce(lambda a,b:a if len(a)>len(b) else b,words)
print("largest of words is:",large)

sumn=0
for i in range(1,101):
    sumn=sumn+i
print("Sum of 100 numbers:",sumn)

