# print(help("lambda"))

def nest(x):
    """This is just a docs."""
    return lambda : 10 * x
m = nest(6)
print(m())
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