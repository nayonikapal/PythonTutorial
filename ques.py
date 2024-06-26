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

def main():
    print("THIS IS AN ACCOUNTING PROGRAM")
    print("Choose the option given below\n      1.ADD ACCOUNT\n      2.REMOVE ACCOUNT\n      3.WITHDRAWAL\n      4.DEPOSIT\n      5.EXIT")
    y=int(input("->"))

    if y==1:
        l.addacc()
    elif y==2:
        l.removeacc()
    elif y==3:
        l.withdraw()
    elif y==4:
        l.deposit()
    elif y==5:
        exit()
    else:
        print("invalid input, try again")
        main()

class Account:
    ACCOUNTS={'Bank name':"HDFC",'Name':"Nayonika",'Branch':"Dehradun",'Balance':200.00}
    IDNAME={'ID':1,'Account':ACCOUNTS}
    BANKNAME=ACCOUNTS['Bank name']
    NAME_ON_ACC=ACCOUNTS['Name']
    BRANCH=ACCOUNTS['Branch']
    BALANCE=ACCOUNTS['Balance']
    LIST_OF_ACC=[ACCOUNTS]
    
    def __init__(self,ACCOUNTS,BANKNAME,NAME_ON_ACC,BRANCH,BALANCE,LIST_OF_ACC):
        self.accounts=ACCOUNTS
        self.bankname=BANKNAME
        self.name_on_acc=NAME_ON_ACC
        self.branch=BRANCH
        self.balance=BALANCE
        self.list_of_acc=LIST_OF_ACC

    def listofacc(self):
        print("The registered lists are: ",self.list_of_acc)   

    def bank_name(self):
        print("The Bank name is: ",self.bankname)

    def nameacc(self):
        print("The name of the account is: ",self.name_on_acc)

    def acc_branch(self):
        print("The branch of the account is: ",self.branch)

    def acc_bal(self):
        print("The balance is: ",self.balance)

class Bank(Account):
    ACCOUNTS={'Bank name':"HDFC",'Name':"Nayonika",'Branch':"Dehradun",'Balance':200.00}
    IDNAME={'ID':1,'Account':ACCOUNTS}
    BANKNAME=ACCOUNTS['Bank name']
    NAME_ON_ACC=ACCOUNTS['Name']
    BRANCH=ACCOUNTS['Branch']
    BALANCE=ACCOUNTS['Balance']
    LIST_OF_ACC=[ACCOUNTS]

    def __init__(self,IDNAME,BANKNAME,NAME_ON_ACC,BRANCH,BALANCE,LIST_OF_ACC,ACCOUNTS):
        self.idname=IDNAME
        self.bankname=BANKNAME
        self.name_on_acc=NAME_ON_ACC
        self.branch=BRANCH
        self.balance=BALANCE
        self.list_of_acc=LIST_OF_ACC
        self.accounts=ACCOUNTS

    def addacc(self):
        print("ADD ACCOUNT")
        print("Enter the details of the account you wish to add")

        id=input("Enter a unique ID for your account: ")
        if id in self.idname:
            print("Already exists, try again")
        else:
            self.idname.add()

        acc_name=input("Enter account name: ")
        self.list_of_acc.add(acc_name)

        nameonacc=input("Name on the account: ")
        self.name_on_acc.add(nameonacc)

        branch=input("Enter the branch of your bank: ")
        self.branch.add(branch)

        balance=input("Enter the minimum deposit of Rs.200: ")
        self.balance.add(balance)

    def removeacc(self):
        print("REMOVE ACCOUNT")
        d_acc=input("Enter the Account name you wish to delete: ")
        if d_acc not in self.list_of_acc:
            print("This account does not exist")
        else:
            del d_acc

    def withdraw(self):
        print("WITHDRAWAL")
        acc=input("Enter the account name from which you would like to withdraw money: ")
        if acc not in self.list_of_acc:
            print("This is account does not exist")

        acc=self.accounts
        print("Current balance",acc(self.balance))
        amount=float(input("Enter the amount you wish to withdraw"))
        print("Now, current balance is: ",self.balance-amount)

    def deposit(self):
        print("DEPOSIT")
        acc=input("Enter the account name from which you would like to withdraw money: ")
        if acc not in self.list_of_acc:
            print("This is account does not exist")

        acc=self.accounts
        print("Current balance",acc(self.balance))
        dep=float(input("Enter the amount you wish to deposit"))
        print("Now, current balance is: ",self.balance+dep)

l=Bank({'Bank name':"HDFC",'Name':"Nayonika",'Branch':"Dehradun",'Balance':200.00})

if __name__=="__main__":
    main()      

'''QUESTION 3'''
# import datetime

# class TrafficLight:
#     stop_clr="RED"
#     go_clr="GREEN"
#     wait_clr="YELLOW"
#     stop_time=60
#     go_time=30
#     wait_time=5

#     def __init__(self,stop_clr,go_clr,wait_clr,stop_time,go_time,wait_time):
#         self.stopclr=stop_clr
#         self.goclr=go_clr
#         self.waitclr=wait_clr
#         self.stoptime=stop_time
#         self.gotime=go_time
#         self.waittime=wait_time

#     def stop(self,stop_clr,stop_time):
#         print("STOP",self.stopclr,self.stoptime)

#     def go(self,go_clr,go_time):
#         print("GO",self.goclr,self.gotime)

#     def wait(self,wait_clr,wait_time):
#         print("WAIT",self.waitclr,self.waittime)

# def main():
