class Bankaccount():

    def __init__(self,bal):
        self.bal=bal
        self.na=""
        self.em=""
        self.ph=""
        self.ty=""

    def read(self,n,e,p,t):
        self.nm=n
        self.em=e
        self.ph=p
        self.ty=t

    def withdraw(self,amt):
        self.amt=amt
        if(self.bal-amt < 1000):
            print("Insufficent balance")
        else:
            self.bal -= self.amt

    def deposit(self,amount):
        self.bal += amount

    def inst(self):
        if(self.ty=="SB"):
            self.bal *= 1.04
        elif(self.ty=="FD"):
            self.bal *= 1.08

    def display(self):
        print("name: ",self.nm)
        print("email: ",self.email)
        print("Phone no :",self.ph)
        print("Acount type: ",self.ty)

    def getbalance(self):
        return self.bal

acc=Bankaccount(5000)
acc.read("ram","ram@gmail.com",984532196,"SB")
print("Innitial balance: ",acc.getbalance())
acc.deposit(5000)
print("After deposit balance: ",acc.getbalance())
acc.inst()
print("After adding interest balance: ",acc.getbalance())
acc.withdraw(5000)
print("After withdrawing 5000 balance is: ",acc.getbalance())
acc.withdraw(4500)
