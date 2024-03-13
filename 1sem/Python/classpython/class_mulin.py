#multiple inheritansce

class A(object):
    def doA(self):
        print("I am a")

class B(object):
    def doB(self):
        print("I am b")

class C(A,B):
    def doC(self):
        print("I am c")

c=C()
c.doC()
c.doB()
c.doA()
