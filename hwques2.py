'''
1.Find the frequency of each element in a tuple.
2.Find the difference between two tuples.
3.All pair combinations of 2 tuples
    Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8) 
    Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)] 

    Input : test_tuple1 = (9, 2), test_tuple2 = (7, 8) 
    Output : [(9, 7), (9, 8), (2, 7), (2, 8), (7, 9), (7, 2), (8, 9), (8, 2)]
4.Print an Inverted Star Pattern.
   **********
    *********
     ********
      *******
       ******
        *****
         ****
          ***
           **
            *
5.Remove empty List from List.
    The original list is : [5, 6, [], 3, [], [], 9]
    List after empty list removal : [5, 6, 3, 9]
'''

'''QUESTION 1'''
t1=(1,1,3,8,2,2,4,6,2,9)
d1={}
for i in t1:
    if i in d1:
        d1[i]+=1
    # d1={i:t1.count(i)}
    # d1.append()
    # x=t1.count(i)
    else:
        d1[i]=1
    # print(i,":",x)
# print(d1)

'''QUESTION 2'''
t2=(4,5,2,6,3)
t3=(2,6,7,3,9)
t2=set(t2)
t3=set(t3)
tf=t2-t3
# print(tuple(tf))

'''QUESTION 3'''
tt1=(7,2)
tt2=(7,8)
tt3=(9,2)
fl1=[]
fl2=[]
for i in tt1:
    for j in tt2:
        ft1=(i,j)
        ft2=(j,i)
        fl1.append(ft1)
        fl1.append(ft2)
for x in tt3:
    for y in tt2:
        ft3=(x,y)
        ft4=(j,i)
        fl2.append(ft3)
        fl2.append(ft4)
# print(fl1)
# print(fl2)

'''QUESTION 4'''
# # for j in range(11):
# for j in range(10,0,-1):
#     for i in range(10-j):    # if j>0:
#         print(" ",end="")    # print("*",end="\n")
#     for i in range(j-1):    # else:
#         print("*",end="")    # print(" ",end=" ")
#     print()
'''QUESTION 5'''
ol=[5, 6, [], 3, [], [], 9]
fl=[]
for i in ol:
    # if i==[]:
    #     ol.remove(i)
        # print(ol)
    if i!=[]:
        fl.append(i)
print(fl)  
