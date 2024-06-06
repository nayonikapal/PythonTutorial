'''CLASS'''

# class Student:
#     pass

'''OBJECTS'''

# class Student:
#     pass
# obj_1=Student()     #object of class student

class School:
    print("This is a record of Students enrolled")
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    
    def registry(self):
        print("Names of students\n  ",self.name)

    def enroll(self):
        print("Enrollment number of Students:\n ",self.rollno)

a=School(26,"Nayonika")
b=School(20,"Ram")
c=School(15,"Shyam")
a.registry()
b.registry()
c.registry()
a.enroll()
b.enroll()
c.enroll()