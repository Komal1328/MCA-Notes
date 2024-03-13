class BankAccount():
    def __init__(self,balance):
        self.balance=balance
    def getBalance(self):
        return self.balance
    def transfer (self, amount, toAccount):
    # transfer the amount from one account to another
        self.withdraw(amount)
        toAccount.deposit(amount)
    def withdraw (self, amount):
    # withdraw the given amount from the account
        self.balance = self.balance - amount
    def deposit (self, amount):
# deposit the given amount into the account
        self.balance = self.balance + amount

myAccount = BankAccount(500)
newAccount = BankAccount(200)
myAccount.transfer(200, newAccount)
print(myAccount.getBalance())
print(newAccount.getBalance())
