# x = 1
# y = 1
# def scope():
#     global x
#     y = 1
#     y+=1
#     # x += 1
#     print(y)

# # print(x)
# scope()
# print(y)


x = "Nayonika"
def myfunc1():
  x = "John"
  
  def myfunc2():
    global x
    x = "hello"
    
    
  myfunc2()
  return x
print(myfunc1())
print(x)