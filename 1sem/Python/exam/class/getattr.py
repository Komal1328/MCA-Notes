# declaring class 
class Student: 
    def __init__(self,n,a): 
        self.name = n 
        self.age = a 
    def get_name(self):
        return self.name 
# instantiating object 
s1 = Student("Bob Smith",24) 
print("Name is: ", s1.get_name()) 
try: 
    # using getattr() to get name 
    print("Attribute Name: ", getattr(s1, 'name')) 
    # using getattr() to check get_name
    print("Method get_name: ",getattr(s1, 'get_name')) 
    # using getattr() to get name 
    print("Method get_name value: ",getattr(s1, 'get_name')())
    # using getattr() to get age 
    print("Attribute age: ", getattr(s1, 'age')) # using getattr() to check section  print("Attribute section: ", getattr(s1,'Section')) 
except AttributeError: 
    print("Attribute not found") 
finally: 
    print("Execution completed") 
