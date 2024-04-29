list1=["nayonika",0,"python",True]
# for i in list1:
#     print(i)

list1.append(False)         #append func
# print(list1)

list2=list1.copy()          #copy func
# print(list2)

# print(list2.pop(1))       #pop func
# print(list2)

# list1.remove(True)        #remove func
# print(list1)
# list2.append("nayonika")

# x=list2.count("nayonika")   #count func
# print(x)

list=["hello"]              #but list is a func?
# print(list)

list.insert(1,"apple")      #insert func
# print(list)

# print(list2.index(True))    #index func

# list1.reverse()               #reverse func
# print(list1)

list.sort()                     #sort func
# print(list)

list.extend(list1)              #extend func
print(list)
tuple1=(1,2,3,4)
list.extend(tuple1)
print(list)

list2.clear()                   #clear func
print(list2)
