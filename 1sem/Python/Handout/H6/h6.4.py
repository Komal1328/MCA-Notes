#h6.4

import functools
def add(a,b):
    return a+b
lst=[10,40,50,80]
print("List: ",lst)
res=functools.reduce(add,lst)
print("Sum of elements in list: ",res)
