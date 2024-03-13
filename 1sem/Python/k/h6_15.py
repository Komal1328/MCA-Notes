def lstsum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += lstsum(i)
        else:
            total += i
    return total

print(lstsum([1,2,[3,4],5]))