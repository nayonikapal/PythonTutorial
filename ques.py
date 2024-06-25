'''QUESTIONS'''

'''1. Write a Python program to create a class called "Shape" with abstract methods for calculating area and perimeter, 
      and subclasses for "Rectangle", "Circle", and "Triangle".

   2. Write a Python program to create a class called "Bank" with a collection of accounts and methods to add and remove accounts, 
      and to deposit and withdraw money. Also define a class called "Account" to maintain account details of a particular customer.

   3. Write a Python program to create class called "TrafficLight" with attributes for color and duration, 
      and methods to change the color and check for red or green.'''

'''QUESTION 1'''

# class Shape:
    
#     def area(self):
#         pass

#     def peri(self):
#         pass


# class Rectangle(Shape):

#     def __init__(self,l,br):
#         self.l=l
#         self.br=br

#     def area(self):
#         print("Area of rectangle is")
#         return self.l*self.br
    
#     def peri(self):
#         print("Perimeter of rectangle is")
#         return 2*(self.l+self.br)
    
# class Circle(Shape):

#     def __init__(self,r):
#         self.r=r
    
#     def area(self):
#         print("Area of a circle is")
#         return 3.14*self.r*self.r
    
#     def peri(self):
#         print("Perimeter of a circle is")
#         return 2*3.14*self.r
    
# class Triangle(Shape):

#     def __init__(self,a,b,c,bt,h):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.bt=bt
#         self.h=h

#     def area(self):
#         print("Area of a triangle is")
#         return 0.5*self.bt*self.h
    
#     def peri(self):
#         print("Perimeter of a triangle is")
#         return self.a+self.b+self.c


# def main():

#     print('''Calculate area and perimeter of rectangle, circle and triangle
#                 Which shape?
#                     1. Rectangle
#                     2. Circle
#                     3. Triangle
#                     4. Exit''')

#     i=int(input("->"))

#     if i==1:
#         l=float(input("Enter the length: "))
#         br=float(input("Enter the breadth: "))

#         shape=Rectangle(l,br)

#     elif i==2:
#         r=float(input("Enter the radius: "))

#         shape=Circle(r)

#     elif i==3:
#         a=float(input("Enter value of side 'a': "))
#         b=float(input("Enter value of side 'b': "))
#         c=float(input("Enter value of side 'c': "))
#         bt=float(input("Enter the base of the triangle: "))
#         h=float(input("Enter the height of the triangle: "))

#         shape=Triangle(a,b,c,bt,h)

#     elif i==4:
#         exit()

#     else:
#         print("Invalid input")

#     print('''What would you like to calculate?
#                 1. Area
#                 2. Perimeter''')
    
#     j=int(input("->"))

#     if j==1:
#         print(f"The area is: {shape.area()}")

#     if j==2:
#         print(f"The perimeter is: {shape.peri()}")

# if __name__ == "__main__":
#     main()


'''QUESTION 2'''



class Bank:
    ACCOUNTS=['Bank name','ID','Name','Branch']
    BANKNAME=['HDFC']
    IDNAME=[1]
    NAME_ON_ACC=['Nayoinka']
    BRANCH=['Dehradun']
    BALANCE=[200.00]

    def __init__(self,IDNAME,BANKNAME,NAME_ON_ACC,BRANCH,BALANCE):
        self.idname=IDNAME
        self.bankname=BANKNAME
        self.nameonacc=NAME_ON_ACC
        self.branch=BRANCH
        self.balance=BALANCE

    def addacc(self):
        print("Enter the details of the account you wish to add")
        self.idname=input("Enter a unique ID for your account: ")
        if self.idname in IDNAME:
            print("Already exists")
            self.idname
        else:
            IDNAME.add()
        self.nameonacc=input("Name on the account: ")
        self.branch=input("Enter the branch of your bank: ")
        self.balance=input("Enter the minimum deposit of Rs.200: ")
        BALANCE.insert[self.balance,]

    def removeacc(self):
        pass

    def withdraw(self):
        pass

    def deposit(self):
        pass

class Account:
    
    def bankname(self):
        print("The Bank name is: ")
        
Bank(2,'SBI','Ram','Delhi',500)
'''QUESTION 3'''
