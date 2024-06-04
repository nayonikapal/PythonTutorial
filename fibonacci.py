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