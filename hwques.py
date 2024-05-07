# Python program to interchange first and last elements in a list.
# Python program to count Even and Odd numbers in a List.
# Write a Python Program to check whether a given number is a palindrome.
# Python program to create a list of tuples from given list having number and its cube in each tuple.
# Python Program for Bubble Sort.
# Write a Python Program to check whether a given number is a prime No.

'''QUESTION 1'''
# lst1=[1,3,5,7,9]
# a=lst1[0]
# b=lst1[4]
# lst1[4]=a
# lst1[0]=b
# print(lst1)

'''QUESTION 2'''
# lst2=[1,2,5,3,7,8]
# ecount,ocount=0,0
# for i in lst2:
#     if i%2==0:
#         ecount+=1   #lst2.count(i)
#         # x=lst2.count(i%2==0)

#     else:
#         # print("Odd number: ",i)
#         ocount+=1
#         pass
# print("Even: ",ecount)
# print("Odd: ",ocount)

'''QUESTION 3'''
'''''''n=int(input("Enter the number you would like to check for palindrome: "))  '''''''
# s=n.split()
# lst3=[]
# for i in s:
#     # lst3.append(s)
#     pass
# print(s)
# r=s.reverse()
# if r==s:
#     print("palin")
# else:
#     print("non palin")
'''o=n
rev=0
if n<0:
    print("incorrect input")
while n>0:
        t=n%10
        rev=rev*10+t
        n=n//10
if o==rev:
    print(o,"is a palindrome")
else:
    print(o,"is not a palindrome")  '''

'''QUESTION 4'''
# # lsttup=[1,4,5,7]

# # y=lsttup.copy()
# # tup=tuple(y)
# # final=[]
# lst3=[1,4,5,7]
# # print(type(lsttup))
# # lst=[]
# for i in lst3:
#     for j in lst3:
#         j=i
#         x=i*i*i
#         y=[j,x]             # print(x)
# # k=[j,x]
#     # y.insert(j,x)
#     h=list(zip(i,x))
#     h.append(y)
#     # k=tuple((j,x))
#     # k.append(k)
#     # print(list(k))
#     # print(list(k))
#     print(h)
#     print(tuple((i,x)))
# lst3.extend(k)          # k.insert(j,x)     # print(i,j)  # lsttup.insert(x,i)

# y.extend(x)   
# print(lsttup) 
# print(final)
# lsttup.extend(final)
# print(k)


# lsttup.append(x)
''''''''''''
# lst3=[1,4,5,7]
# final=[]
# for i in lst3:
#     x=i*i*i
#     final.insert(i,x)

# print(tuple((lst3,final))) 
''''''''''''
# lst=[1,4,5,7]
# fin=[]
# for i in lst:
#     fin.append((i,i**3))
# print(fin)

'''QUESTION 5'''
bub=[1,4,7,9,34,23,67,45,9]

'''QUESTION 6'''
gn=int(input("Enter the number you would like to check: "))
prm=True
if gn<=0:
    print("invalid input, try again")
elif gn>0:
    if gn==2:
        prm=True
    elif gn==3:
        prm=True
    elif gn==5:
        prm=True
    elif gn==7:
        prm=True
    elif gn%2==0:
        prm=False
    elif gn%3==0:
        prm=False
    elif gn%5==0:
        prm=False
    elif gn%7==0:
        prm=False
    else:
        prm=True

if prm==True:
    print(gn,"is a prime number")
else:
    print(gn,"is not a prime number")
