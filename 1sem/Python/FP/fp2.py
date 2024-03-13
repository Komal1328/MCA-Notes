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
