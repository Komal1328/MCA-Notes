#fp1

A=[i for i in range(1,50)]


print("Odd numbers in list: ")
print(list(filter(lambda x:x%2!=0,A)))
print()
print("Even numbers in list: ")
print(list(filter(lambda x:x%2==0,A)))
print()
print("Numbers divisible by 3 and 7 in list: ")
print(list(filter(lambda x:x%3==0 and x%7==0,A)))

