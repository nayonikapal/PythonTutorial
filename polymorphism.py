
class Nayonika:
    def intro(self):
        print(" My name is Noyonika")

class Employee(Nayonika):
    def intro(self):
        print(" My name is Noyonika. I'm employee.")
        
    def working(self):
        print("I'm a Developer")   

class School(Nayonika):
    def intro(self):
        print(" My name is Noyonika. I'm Student.")
        
    def working(self):
        print("I'm a Studying")
    
    
nayo = Nayonika()
emp = Employee()
stu = School()

nayo.intro()
emp.intro()
emp.working()
stu.intro()
stu.working()