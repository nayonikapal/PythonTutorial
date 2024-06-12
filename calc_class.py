class calc:
    
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def addition(self):
        add=self.num1+self.num2
        print("The sum is",self.num1,"and",self.num2,"is",add)
        return main()

    def subtraction(self):
        sub=self.num1-self.num2
        print("The difference is",self.num1,"and",self.num2,"is",sub)
        return main()

    def multiplication(self):
        mul=self.num1*self.num2
        print("The multiplication of",self.num1,"and",self.num2,"is",mul)
        return main()
    
    def division(self):
        div=self.num1/self.num2
        print("The division of",self.num1,"and",self.num2,"is",div)
        return main()

print("This is a calculator program")
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

l=calc(num1,num2)

def main():
    print ("""What operation would you like to calculate?
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Exit""")
    i=int(input("Enter the number from the list given above: "))

    if i==1:
        print(l.addition())
            
    elif i==2:
        print(l.subtraction())

    elif i==3:
        print(l.multiplication())

    elif i==4:
        print(l.division())

    elif i==5:
        exit()
            
    else:
        print("Invalid input")
        main()

if __name__=='__main__':
    main()

# calc()      #test 

# print(l.addition())
# print(l.subtraction())
# print(l.multiplication())
