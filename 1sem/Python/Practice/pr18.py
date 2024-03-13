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
