#pr1

name=(input("Enter your name: "))
sem=int(input("Enter semester: "))
m1,m2,m3,m4,m5,m6=input("Enter 6 subjects marks out of 100: ").split()
m1=int(m1)
m2=int(m2)
m3=int(m3)
m4=int(m4)
m5=int(m5)
m6=int(m6)

tot=(m1+m2+m3+m4+m5)
per=(tot/600)*100
print("Total: ",tot)
print("Percentage: ",per)
if(per>80):
    print("A grade")
elif(per>60 and per<=80):
    print("B grade")
elif(per>50 and per<=60):
    print("C grade")
elif(per>45 and per<=50):
    print("D grade")
elif(per>25 and per<=45):
    print("E grade")
elif(per<25):
    print("F grade")
