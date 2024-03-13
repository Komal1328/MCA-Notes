#8.1

class BankAccount:
    def __init__(self):
        self.bal=0
        self.nm=""
        self.em=""
        self.ph=""
        self.ta=""

    def read(self,n,e,p,t):
        self.nm=n
        self.em=e
        self.ph=p
        self.ta=t
    def deposit(self,am):
        self.bal += am

    def withdraw(self,amt):
        if(self.bal-amt<1000):
            print("Insufficient balance")
        else:
            self.bal -= amt

    def display(self):
        print("Name: ",self.nm)
        print("Email: ",self.em)
        print("Phone: ",self.ph)
        print("Account type: ",self.ta)

    def getBalance(self):
        return self.bal

    def inter(self):
        if self.ta=="SB":
            self.bal *= 1.04
        elif self.ta == "FD":
            self.bal *= 1.08
            
acc=BankAccount()
acc.read("Ram","ram123@email.com","9851478548","SB")
acc.deposit(5000)
acc.display()
print("Afetr deposit:",acc.getBalance())
acc.inter()
print("Afetr adding interst:",acc.getBalance())
acc.withdraw(1000)
print("After withdraw:",acc.getBalance())
acc.withdraw(3500)
print("After withdraw:",acc.getBalance())
