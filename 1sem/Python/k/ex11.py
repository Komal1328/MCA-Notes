class BankAccount:
    def __init__(self, bal):
        self.bal = bal
        self.nm = ""
        self.em = ""
        self.ph = ""
        self.tp = ""

    def read(self, n, e, p, t):
        self.nm = n
        self.em = e
        self.ph = p
        self.tp = t

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        if (self.bal-amount<1000):
            print("Insufficient balance")
        else:
            self.bal -= amount

    def display(self):
        print("Name:", self.nm)
        print("Email:", self.em)
        print("Phone:", self.ph)
        print("Account Type:", self.tp)
    
    def getBalance(self):
        print("Balance:", self.bal)

    def add_interest(self):
        if self.tp == "SB":
            self.bal *= 1.04
        elif self.tp == "FD":
            self.bal *= 1.08
acc = BankAccount(10000)
acc.read("xyz","xyz@domain.com","9800913478","SB")
acc.display()
acc.getBalance()

acc.deposit(1000)
acc.getBalance()
acc.withdraw(999)
acc.getBalance()
acc.add_interest()
acc.getBalance()
