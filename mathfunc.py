'''---------TRIAL----------'''

# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))

# def maths():
#     sum=num1+num2
#     print("Addition: ",sum)
#     sub=num1-num2
#     print("Subtraction: ",sub)
#     div=num1/num2
#     print("Division: ",div)
#     mul=num1*num2
#     print("Multiply: ",mul)
#     fac=num

# input("Enter the operation you would like to use(sum,sub,div,mul): ")
# maths()
'''-------ALTERNATIVE-------'''

# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))

# def sum():
#     add=num1+num2
#     print("Addition: ",add)

# def sub():
#     min=num1-num2
#     print("Subtraction: ",min)

# def div():
#     dvd=num1/num2
#     print("Division: ",dvd)

# def mul():
#     mlty=num1*num2
#     print("Multiplication: ",mlty)

# def fac():
#     i=num1
#     fact1=1
#     while i>=1:
#         fact1*=i
#         i-=1
#     print("Factorial of first number: ",fact1)
#     j=num2
#     fact2=1
#     while j>=1:
#         fact2*=1
#         j-=1
#     print("Factorial of second number: ",fact2)

# a=input("Enter what you would like to calculate: \n[sum,sub,div,mul,fac]: ")

# if a=="sum":
#     sum()
# elif a=="sub":
#     sub()
# elif a=="div":
#     div()
# elif a=="mul":
#     mul()
# elif a=="fac":
#     fac()
# else:
#     print("Invalid input, please try again!")

'''-------FINAL------'''

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

t=input("Enter the operation you would like to execute:\n[sum,sub,div,mul,fac]: ")

def mathfunc():
    if t=="sum":
        add=num1+num2
        print("Addition: ",add)
    elif t=="sub":
        min=num1-num2
        print("Subtraction: ",min)
    elif t=="div":
        dvd=num1/num2
        print("Division: ",dvd)
    elif t=="mul":
        mlty=num1*num2
        print("Multiplication: ",mlty)
    elif t=="fac":
        y=input("Which number do you want to calculate factorial of?: \n[num1,num2]: ")
        if y=="num1":
            i=num1
            fact1=1
            while i>=1:
                fact1*=i
                i-=1
            print("Factorial of the first number is: ",fact1)
        elif y=="num2":
            j=num2
            fact2=1
            while j>=1:
                fact2*=j
                j-=1
            print("Factorial of the second number is: ",fact2)
        else:
            print("Invalid input, please try again!")
    else:
        print("Invalid input, please try again!")

mathfunc()