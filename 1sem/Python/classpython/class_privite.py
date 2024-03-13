#privite attribute

class JustCount:
    __secretCount=100
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)
counter=JustCount()
counter.count()
counter.count()
print(counter.__JustCount__.secrectCount)
print(counter.__secretCount)
