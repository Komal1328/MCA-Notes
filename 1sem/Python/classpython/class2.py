class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount += 1

emp1=Employee("Raja",20000)
emp2=Employee("Kumar",5000)
print("Employee.__doc__:",Employee.__doc__)
print("Employee.__name__:",Employee.__name__)
print("Employee.__module__:",Employee.__module__)
print("Employee.__bases__:",Employee.__bases__)
print("Employee.__dict__:",Employee.__dict__)

    
