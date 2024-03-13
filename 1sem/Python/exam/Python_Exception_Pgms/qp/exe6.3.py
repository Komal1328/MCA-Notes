#exe6.3
a=[1,2,3]
try:
    print(a[2])
    print(a[3])
except IndexError:
    print("Out of index")
