#pr2

print("1.BattryBased toy 2.Key based toy 3.Electrical charging toy")
n=int(input("Enter code 1,2,3: "))
amt=int(input("Enter the amount: "))
if(n==1 and amt>1000):
    amt=amt-((amt*10)/100)
    print("Net amount: ",amt)
elif(n==2 and amt>100):
    amt=amt-((amt*5)/100)
    print("Net amount: ",amt)
elif(n==3 and amt>500):
    amt=amt-((amt*10)/100)
    print("Net amount: ",amt)
else:
    print("Net amount: ",amt)
