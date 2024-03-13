#h7.5

res=list(filter (lambda x:x,[4,0,6,3,0,2]))
print(res)

res1=list(reduce(lambda x, y: x and y, filter(lambda x:x%2==0,a)))
print(res1)
