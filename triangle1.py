# for i in range(0,6):
#        print("*", end=" ")
#        i-1
# for j in range(i):
#     if j==6:
#         print("\n*", end=" ")
#     if j==5:
#         print("\n*", end=" ")


# for i in range(0,6):
#        print("*", end= " ")
#        print("\n")
#        if i==1:
#         print("*", end=" ")
#        elif i==2:
#         print("*", end=" ")
#        elif i==3:
#         print("*", end=" ")

# for i in range(0,6):                      #incorrect way
#     if i==0:
#         print("* * * * *",end="\n")   
#     if i==1:
#         print("* * * *",end="\n")
#     if i==2:
#         print("* * *",end="\n")
#     if i==3:
#         print("* *",end="\n")
#     if i==4:
#         print("*",end="\n")

# for i in range(0,6):
#     for j in range(0,6):
#         if i<=j:
#             print("*", end=" ")
#         else:
#             print()


for i in range(0,6):
    for j in range(0,6):
        if i>=j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(6,0,-1):
    for j in range(6-1):
        print(" ", end=" ")
    for j in range(i-1):
        print("*", end=" ")
    print()