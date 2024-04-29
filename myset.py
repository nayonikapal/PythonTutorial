set1={"nayo","nika","pal","student"}
# print(len(set1))                    #length of set

set1.add("hello")                   #adding elements
# print(set1)

set2=set1.copy()                    #copy list
# print(set2)

# set1.clear()                      #clear func
# print(set1)

d=set1.difference(set2)             #difference func
# print(d)

set3={1,3,5,7}
set2.update(set3)                   #update func
# print(set2)

d1=set2-set3                        #difference func
# print(d1)

# set3.discard(7)                     #discard func
# print(set3)

# i1=set1&set2                      #intersection func
# print(i1)

# set3&=set1&set2                   #intersection update func
# print(set3)

# print(set1.isdisjoint(set3))        #disjoint func
# print(set2.isdisjoint(set3))
print(set1)
print(set2)
print(set3)

# print(set1.issubset(set2))          #subset func
# print(set3<=set1)

# print(set2.issuperset(set1))            #superser func
# print(set3>set2)

# set1.pop()                            #pop func
# print(set1)

# set1.remove("pal")                      #remove func
# print(set1)

# print(set1^set2)                        #symmetric func
# print(set1^set3)

print(set2|set3)                            #union func
print(set1.union(set3))
