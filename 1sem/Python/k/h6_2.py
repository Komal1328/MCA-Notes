present = [1,2,3,4,5,6,8]
def attendance():
     roll = int(input("Enter roll no.: "))
     if roll in present:
          print("Student is present")
     else:
          print("Student is absent")

attendance()     
     
