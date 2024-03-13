#fp4

import functools
def ave(lst):
    avg=functools.reduce(lambda a,b:a+b,lst)/len(lst)
    return avg

lst=[1,2,3,4,5]
print("Average of numbers:",ave(lst))

