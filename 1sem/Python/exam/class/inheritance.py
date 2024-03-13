class student:
    'A class representing a student.'
    def __init__(self,n,a):
        self.full_name = n
        self.age = a
    def get_age(self):
        return self.age

class ai_student (student):
    'A class extending student.'
    def __init__(self,n,a,s):
        student.__init__(self,n,a)
        self.section_num = s
    def get_age(self):
        print ("Age: "+ str(self.age))
ais1= ai_student("aaa",20,"a")
ais1.get_age()
