class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __def__(self):
        class_name=self.__class__.__name__
        print(class_name,"Destroyed")
pt1=Point()
pt2=pt1
pt3=pt1
print(id(pt1),id(pt2),id(pt3))
del pt1
print("Deletion of point 1")
del pt2
print("Deletion of point 2")
del pt3
print("Deletion of point 3")
