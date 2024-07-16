
# class nayonika:
    
#     def __init__(self,num1, num2) -> None:
#         self.varx1 = num1 
#         self.varx2 = num2
#         print(self.varx1,self.varx2)
    
#     def add(self):
#         return self.varx1 + self.varx2
    
#     def subs(self):
#         return self.varx1 - self.varx2
    
#     def divi(self):
#         return self.varx1 / self.varx2
    
#     def multi(self):
#         return self.varx1 * self.varx2
    

# obj1 = nayonika(5,4)
# obj2 = nayonika(15,3)

# print(obj2.add())
# print(obj2.subs())
# print(obj2.multi())
# print(obj2.divi())

class Person:
    nayo = "Nayionika"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} | {self.age}"

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()