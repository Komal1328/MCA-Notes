class Employee:
    'Common base class for all employees'
    empCount = 0
    name=" "

    def __init__(self,name,salary):
        Employee.name=name
        Employee.salary=salary
        Employee.empCount += 1
        

emp1=Employee("Raja",20000)
print("Employee.__name__:",Employee.name)
print("Salary:",Employee.salary)
emp2=Employee("Kumar",5000)
print("Employee.__name__:",Employee.name)
print("Employee count:",Employee.empCount)
    
