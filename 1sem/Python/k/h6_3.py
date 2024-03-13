def maxof2(n1,n2):
     return n1>n2
def maxof3(n1,n2,n3):
     if(maxof2(n1,n2) and maxof2(n1,n3)):
          return n1
     elif(maxof2(n2,n3) and maxof2(n2,n1)):
          return n2
     else:
          return n3
n1 = int(input("Enter the first number\n"))
n2 = int(input("Enter the second number\n"))
n3 = int(input("Enter the third number\n"))

print(maxof3(n1,n2,n3))
