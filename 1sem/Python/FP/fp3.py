#fp3

def deg(a):
    return (a*9/5)+32

def fah(a):
    return (a-32)*5/9

tempc=[20,4,5,80,100]
tempf=[68,39,41,176,212]

print("In fahrenheit to degree celsius: ")
print(tempf)
print(list(map(fah,tempf)))
print()
print("In degree celsius to fahrenheit: ")
print(tempc)
print(list(map(deg,tempc)))
