#fp6

import functools

lst=[1,2,3,4,5]
print("sm of numbers:")
print(functools.reduce(lambda x,y:x+y,lst))
