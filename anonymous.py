# print(help("lambda"))

# def nest(x):
#     """This is just a docs."""
#     return lambda : 10 * x
# m = nest(6)
# print(m())
# print(nest(None))


# m = lambda y : x*y
# print(m(6,7))

# def ujjwal(x):
# if x <= 0:
#     return
#     print(x)
#     return ujjwal(x-1)
# ujjwal(15)


# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))


# lst = [(1),(2),(3),(4)]
# for i in lst:
#     print(i,type(i))

# lst2 = [(1,3),(2,2),(3,2),(4,0)]
# for i in lst2:
#     print(i,type(i))


lst = [4, 5, 1, 8, 2]
# res = [(4,64),(5,125),(1,1),(8,512),(2,8)]
res = []
for i in lst :
    res.append(tuple((i,i**3)))
    
print(res)
    

