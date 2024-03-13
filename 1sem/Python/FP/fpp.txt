#fp1

A=[i for i in range(1,50)]


print("Odd numbers in list: ")
print(list(filter(lambda x:x%2!=0,A)))
print()
print("Even numbers in list: ")
print(list(filter(lambda x:x%2==0,A)))
print()
print("Numbers divisible by 3 and 7 in list: ")
print(list(filter(lambda x:x%3==0 and x%7==0,A)))

#fp2

nonzero=lambda x:x!=0
odd=lambda x:x%2!=0
add=lambda x,y:x+y
sumo=lambda x,y:(x+y)%2 != 0
mul=lambda x,y,z:(x*y)<=z

print("Nonzero:",nonzero(3))
print("is odd: ",odd(3))
print("sum: ",add(3,4))
print("Is sum odd: ",sumo(3,4))
print("Mul: ",mul(1,2,3))

#fp3

def deg(a):
    return (a*9/5)+32

def fah(a):
    return (a-32)*5/9

tempc=[20,4,5,80,100]
tempf=[68,39,41,176,212]

print("In fahrenheit to degree celsius: ")
print(tempf)
print(list(map(fah,tempf)))
print()
print("In degree celsius to fahrenheit: ")
print(tempc)
print(list(map(deg,tempc)))


#fp4

import functools
def ave(lst):
    avg=functools.reduce(lambda a,b:a+b,lst)/len(lst)
    return avg

lst=[1,2,3,4,5]
print("Average of numbers:",ave(lst))


#fp5

def prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

lst=[2,3,4,5,6,78,9]
print("prime numbers: ",list(filter(prime,lst)))

#fp6

import functools

lst=[1,2,3,4,5]
print("sm of numbers:")
print(functools.reduce(lambda x,y:x+y,lst))

#fp7

lst=[i for i in range(1,11)]
print(lst)

print("Square of numbers: ")
print(list(map(lambda x:x**2,lst)))
print("cube of numbers")
print(list(map(lambda x:x**3,lst)))
print("List of numbers larger by 1:")
print(list(map(lambda x:x+1,lst)))

