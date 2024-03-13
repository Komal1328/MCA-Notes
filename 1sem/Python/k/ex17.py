def maxOf2(n1, n2):
    if n1>n2:
        return n1
    else:
        return n2
def maxOf3(n1,n2,n3):
    return maxOf2(n1, maxOf2(n2, n3))

print(maxOf3(10,20,30))
print(maxOf3(20,10,30))
print(maxOf3(30,20,10))