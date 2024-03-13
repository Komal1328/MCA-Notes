nonzero = lambda x: x!=0
odd = lambda x: x%2!=0
sumf = lambda x,y: x+y
sumf_odd = lambda x,y: (x+y)%2!=0
prod = lambda x,y,z: (x*y)<=z

print(nonzero(2))
print(odd(3))
print(sumf(2,3))
print(sumf_odd(2,3))
print(prod(3,5,27))