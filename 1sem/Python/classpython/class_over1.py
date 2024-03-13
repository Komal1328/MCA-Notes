#overriding

class Parent:
    def myMethod(self):
        print("Calling parent method")

class Child(Parent):
        def myMethod(self):
            print("Caling child method")

c=Child()
c.myMethod()
p=Parent()
p.myMethod()
