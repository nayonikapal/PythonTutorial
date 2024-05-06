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
# n=input("Enter the number you would like to check: ")
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

'''QUESTION 4'''
lst3=[1,4,5,7]
# y=lsttup.copy()
# tup=tuple(y)
final=[]

# print(type(lsttup))

for i in lst3:
    for j in lst3:
        j=i
        x=i*i*i
    # print(x)
    final.insert(j,x)
    # print(i,j)  # lsttup.insert(x,i)

# y.extend(x)   
# print(lsttup) 
print(final)
# lsttup.extend(final)
# print(lsttup)

# lsttup.append(x)