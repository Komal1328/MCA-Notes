#fp7

lst=[i for i in range(1,11)]
print(lst)

print("Square of numbers: ")
print(list(map(lambda x:x**2,lst)))
print("cube of numbers")
print(list(map(lambda x:x**3,lst)))
print("List of numbers larger by 1:")
print(list(map(lambda x:x+1,lst)))
