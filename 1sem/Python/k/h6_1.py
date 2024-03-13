def add_out():
     def add_in(a, b):
          return a+b
     n1 = int(input("Enter the first number:\n "))
     n2 = int(input("Enter the second number:\n "))
     return(add_in(n1,n2) + 5)
print(add_out())
