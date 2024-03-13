
def inter(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i in lst2:
            lst3.append(i)
    return lst3

lst1=[1,2,34,5,9]
lst2=[2,5,7,6,1,10]
print("Lst1:",lst1)
print("Lst2:",lst2)
print("Intersection list:",inter(lst1,lst2))
