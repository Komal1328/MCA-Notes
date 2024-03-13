class Student: 
    def __init__(self,n,a): 
        self.name = n 
        self.age = a 
    def get_name(self): 
        return self.name 
# instantiating object 
s1 = Student("Bob Smith",24) 
print("Name is: ", s1.get_name()) 
# using hasattr() to check name 
print("Attribute Name: ", hasattr(s1, 'name')) 
# using hasattr() to check section 
print("Attribute section: ", hasattr(s1,'Section')) 
# using hasattr() to check get_name 
print("Method get_name: ",hasattr(s1, 'get_name')) 
# using hasattr() to check get_age 
print("Method get_age: ", hasattr(s1, 'get_age')) 
