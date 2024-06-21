'''QUESTIONS'''

'''1. Write a Python program to create a class called "Shape" with abstract methods for calculating area and perimeter, 
      and subclasses for "Rectangle", "Circle", and "Triangle".

   2. Write a Python program to create a class called "Bank" with a collection of accounts and methods to add and remove accounts, 
      and to deposit and withdraw money. Also define a class called "Account" to maintain account details of a particular customer.

   3. Write a Python program to create class called "TrafficLight" with attributes for color and duration, 
      and methods to change the color and check for red or green.'''

'''QUESTION 1'''
l=float(input("Enter the length: "))
b=float(input("Enter the breadth: "))
h=float(input("Enter the height: "))

class Shape:
    def __init__(self,l,b,h,r):
        self.l=l
        self.b=b
        self.h=h
        self.r=r
    
    def area(self):
        pass

    def peri(self):
        pass


class Rectangle(Shape):

    def area(self):
        print("Area of rectangle is")
        return self.l*self.b
    
    def peri(self):
        print("Perimeter of rectangle is")
        return 2*(self.l+self.b)
    
class Circle(Shape):
    
    r=float(input("Enter the radius: "))

    def __init__(self,r):
        self.r=r
    
    def area(self):
        print("Area of a circle is")
        return 3.14*self.r*self.r
    
    def peri(self):
        print("Perimeter of a circle is")
        return 2*3.14*self.r
    
class Triangle(Shape):

    a=float(input("Enter value of side 'a': "))
    b=float(input("Enter value of side 'b': "))
    c=float(input("Enter value of side 'c': "))


    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        print("Area of a triangle is")
        return 0.5*self.b*self.h
    
    def peri(self):
        print("Perimeter of a triangle is")
        return self.a+self.b+self.c
    
print('''Calculate area and perimeter of rectangle, circle and triangle
            Which shape?
                1. Rectangle
                2. Circle
                3. Triangle
                4. Exit''')

i=int(input())

if i==1:
    Rectangle(Shape(l,b,h,))

elif i==2:
    Circle(Shape)

elif i==3:
    Triangle(Shape(l,b,h))

elif i==4:
    exit()

else:
    print("Invalid input")


'''QUESTION 2'''

# class Bank:
