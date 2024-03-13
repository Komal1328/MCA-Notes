class Student: 
    def __init__(self,n,a): 
        self.name = n 
        self.age = a 
    def get_name(self): 
        return self.name
    
# instantiating object 
s1 = Student("Bob Smith",24) 
print("Name is: ", s1.get_name()) 
# using setattr() to change name 
setattr(s1, 'name','Babu') 
  
# using getattr() to check get_name 
print("Method get_name: ",getattr(s1, 'get_name')()) 
