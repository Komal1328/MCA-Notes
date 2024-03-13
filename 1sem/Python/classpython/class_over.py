class student:
    "A class representing a student."

    def __init__(self,n,a):
        self.full_name=n
        self.age=a

    def get_age(self):
        return self.age

    def get_details(self):
        print("Name: ",self.full_name)
        print("Age: ",self.age)

class ai_student(student):
    "A class extending student"

    def __init__(self,n,a,s):
        student.__init__(self,n,a)
        self.section_num=s

    def get_age(self):
        print("Age:"+str(self.age))

    def get_selection(self):
        print("Selection: ",self.section_num)
        

ais1=ai_student("aaa",20,"a")
ais1.get_age()
ais1.get_selection()
stu=student("xyz",10)
print("Age in base class:",stu.get_age())
#print("Age in sub class:",ais1.get_age())

