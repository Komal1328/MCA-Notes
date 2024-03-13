class BankAccount(object):
    def __init__(self,amount=0):
        self.balance=amount
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def getBalance(self):
        return self.balance
    def transfer(self,amount,toAccount):
        self.withdraw(amount)
        toAccount.deposit(amount)
        
myAccount=BankAccount()
secondAccount=BankAccount()
myAccount.deposit(200)
print("After deposit")
print("myaccount ",myAccount.getBalance())
secondAccount.deposit(125)
print("2nd account ",secondAccount.getBalance())
print("After withdraw")
myAccount.withdraw(70)
print("myaccount ",myAccount.getBalance())
secondAccount.withdraw(25)
print("2nd account ",secondAccount.getBalance())
print("After transfer")
myAccount.transfer(20,secondAccount)
print("myaccount ",myAccount.getBalance())
print("2nd account ",secondAccount.getBalance())
print()

def winLottery(winner):
    winner.deposit(10000)

bobsAccount=BankAccount(1000)
bobsAccount.deposit(300)
aliceAccount=bobsAccount
aliceAccount.withdraw(250)
print("BobsAcccount",bobsAccount.getBalance())
winLottery(bobsAccount)
print("BobsAcccount",bobsAccount.getBalance())

