class JustCount:
    secretCount=100
    def count(self):
        self.secretCount += 1
        print(self.secretCount)
counter=JustCount()
counter.count()
counter.count()
print(counter.secretCount)
