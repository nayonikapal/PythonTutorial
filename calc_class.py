class calc:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def addition(self):
        add=self.num1+self.num2
        print("The sum is ",add)

    def subtraction(self):
        sub=self.num1-self.num2
        print("The difference is ",sub)

    def multiplication(self):
        mul=self.num1*self.num2
        print("The the multiplication is ",mul)

# calc()      #test 
print("This is a calculator program")
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
calc()