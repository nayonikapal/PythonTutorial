<<<<<<< HEAD
x=int(input("Enter the length of numbers in the sequence: "))

if x<0:
    print("Invalid input")
yf=0
ys=1
print(yf,ys,end=" ")
for i in range(2,x):
    r=yf+ys
    print(r,end=" ")
    yf=ys
    ys=r
=======
# 0 1 1 2 3 5 8 13 21

num = int(input("Enter the number you wnt to print fibonacci series : "))
first = 0
second = 1
print(str(first) + " " + str(second), sep=" ", end=" ")
for i in range(num):
    res = first + second
    print(str(res), sep=" ", end=" ")
    first = second
    second = res
    
>>>>>>> dbc758829c6d1953461c2c63eafbe155c4d481b3
