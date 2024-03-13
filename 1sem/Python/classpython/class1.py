class BankAccount(object):
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def getBalance(self):
        return self.balance
myAccount=BankAccount()
secondAccount=BankAccount()
myAccount.deposit(200)
print(myAccount.getBalance())
secondAccount.deposit(125)
print(secondAccount.getBalance())
myAccount.withdraw(70)
print(myAccount.getBalance())
secondAccount.withdraw(25)
print(secondAccount.getBalance())
