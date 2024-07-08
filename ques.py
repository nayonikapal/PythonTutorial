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

# class Account:

#     def __init__(self,ACCOUNT_ID,BANKNAME,NAME_ON_ACC,BRANCH,BALANCE=200.00):
#         self.account_id=ACCOUNT_ID
#         self.bankname=BANKNAME
#         self.name_on_acc=NAME_ON_ACC
#         self.branch=BRANCH
#         self.balance=BALANCE

#     def __str__(self):
#         return f"Account ID: {self.account_id}, Bank: {self.bankname}, Name: {self.name_on_acc}, Branch: {self.branch}, Balance: {self.balance:.2f}"

# class Bank:

#     def __init__(self):
#         self.accounts={}

#     def addacc(self):
#         print("ADD ACCOUNT")
#         print("Enter the details of the account you wish to add")

#         id=input("Enter a unique ID for your account: ")
#         if id in self.accounts:
#             print("Already exists, try again")

#         bank_name=input("Enter bank name: ")
#         nameonacc=input("Enter name on the account: ")
#         branch=input("Enter the branch of your bank: ")
#         balance=float(input("Enter the initial deposit (minimum = ₹200): "))

#         if balance<200:
#             print("Minimum deposit of ₹200 mandatory")
        
#         new_acc= Account(id, bank_name, nameonacc, branch, balance)
#         self.accounts[id]= new_acc
#         print("Account added successfully")

#     def removeacc(self):
#         print("REMOVE ACCOUNT")
#         id=input("Enter the Account ID you wish to delete: ")
#         if id not in self.accounts:
#             print("This account does not exist")
#         else:
#             del self.accounts[id]
#             print("Account removed successfully")

#     def withdraw(self):
#         print("WITHDRAWAL")
#         id=input("Enter the Account ID from which you would like to withdraw money: ")

#         if id not in self.accounts:
#             print("This is account does not exist")
        
#         acc=self.accounts[id]
#         print("Current balance:",acc.balance)
#         amount=float(input("Enter the amount you wish to withdraw"))

#         if amount>acc.balance:
#             print("Insufficient funds")

#         acc.balance-=amount
#         print("Withdrawal successful\nCurrent balance: ",acc.balance)

#     def deposit(self):
#         print("DEPOSIT")
#         id=input("Enter the Account ID to which you would like to deposit money: ")
#         if id not in self.accounts:
#             print("This is account does not exist")

#         acc=self.accounts[id]
#         print("Current balance:",acc.balance)
#         dep=float(input("Enter the amount you wish to deposit"))

#         acc.balance+=dep
#         print("Deposit successful\nCurrent balance: ",acc.balance)

#     def list_of_acc(self):
#         print("The registered accounts are: ")
#         for account in self.accounts.values():
#             print(account)

# def main():
#     bank=Bank()
#     print("THIS IS AN ACCOUNTING PROGRAM")
#     print("Choose the option given below\n      1.ADD ACCOUNT\n      2.REMOVE ACCOUNT\n      3.WITHDRAWAL\n      4.DEPOSIT\n      5.EXIT")
#     y=int(input("->"))

#     if y==1:
#         bank.addacc()
#     elif y==2:
#         bank.removeacc()
#     elif y==3:
#         bank.withdraw()
#     elif y==4:
#         bank.deposit()
#     elif y==5:
#         exit()
#     else:
#         print("invalid input, try again")
#         main()

# if __name__=="__main__":
#     main()      

'''QUESTION 3'''

class TrafficLight:

    def __init__(self,clr="RED",dur=60):
        self.clr=clr
        self.dur=dur

    def changeclr(self,newclr,newdur):
        self.clr=newclr
        self.dur=newdur

    def red(self):
        return self.clr.upper()=="RED"

    def green(self):
        return self.clr.upper()=="GREEN"

def main():
    print("THIS IS A TRAFFIC LIGHT PROGRAM")
    light=TrafficLight()
    print(f"Current colour: {light.clr}, Duration: {light.dur}")

    light.changeclr("GREEN",30)
    print(f"Updated colour: {light.clr}, Updated duration: {light.dur}")

    if light.red():
        print("The light is RED, please STOP!")
    elif light.green():
        print("The light is GREEN, please GO!")
    
if __name__=='__main__':
    main()
    