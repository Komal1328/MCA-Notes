#pr 3

num=int(input("Enter the a number: "))
count=0
sumn=0
dig=0
while(num!=0):
    dig=(num%10)
    sumn += dig
    count += 1
    num = int(num/10)

print("Sum of digits: ",sumn)
print("Number of digits: ",count)
