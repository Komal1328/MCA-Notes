#h8.3

class Rectangle:
    def __init__(self,ln,br):
        self.l=ln
        self.b=br
    def getVal(self):
        return self.l,self.b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)
    def sqrchk(self):
        return self.l==self.b
rec=Rectangle(3,4)
l,b=rec.getVal()
print("Length: ",l," and "," Breadth: ",b)
print("Area of rectangle: ",rec.area())
print("Perimeter of rectangle: ",rec.perimeter())
print("Square check: ",rec.sqrchk())
