class num:
    def __init__(self,n):
        self.n=n
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"Destroyed")
a=num(40)
b=a
c=b
print(id(a),id(b),id(c))
b=100
c=-1
print(id(a),id(b),id(c))
del a
del b
