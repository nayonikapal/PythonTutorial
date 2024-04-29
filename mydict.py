# dict1={'a':"apple",'b':"ball",'c':"cat"}
# # dict1.update({'d':"data"})
# dict1['d']="data"
# dict1['c']="copy"
# del dict1['a']
# dict1.clear()

# print(dict1)
# for i,j in dict1.items():
#     print(i,j)
    # print(i," : ",dict1[i])
# print(dict1.items()) 


'''DICT METHODS'''

dict1={'1':"one",'2':"two",'3':"three",'4':"four"}

dict2=dict1.copy()
# print(dict2)

print(dict2.fromkeys(dict1))   ####

# print(dict1.get('3'))           #get func

# print(dict1.items())            #items func

# print(dict2.keys())               #keys func

# dict2.pop('4')                    #pop func
# print(dict2)

# dict2.popitem()                   #popitem func
# print(dict2)

# dict2.setdefault('4',"four")        #set default func
# dict2.setdefault('1',"one")
# print(dict2)

dict2.update({'name':"nayonika"})       #update func
print(dict2)

print(dict2.values())                   #values func

list1=["a","b","c","d"]
list2=["app","ball","cat","dog"]
print(dict().fromkeys(list1,False))

x="ccffghkdkkhlcfg"
