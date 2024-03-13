#without list comprehension
lst1 = [1,2,3,4,5]
lst2 = [2,3,6,5,7]
lst3 = []
for i in lst1:
    if i in lst2:
        lst3.append(i)

print(lst3)

#with list comprehension

lst4 = [i for i in lst1 if i in lst2]
print(lst4)