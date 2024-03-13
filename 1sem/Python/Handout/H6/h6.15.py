#h6.15

def lstsum(lst):
    total=0
    for i in lst:
        if(type(i)==list):
            total += lstsum(i)
        else:
            total += i
    return total

lst=[1, 2, [3,4], [5,6]]
print("Sum of list elements",lstsum(lst))
