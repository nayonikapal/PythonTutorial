tuple1=(1,2,3,4,5,"hello","nayonika","here")
tuple2=(6,7,8,"bye","hello")
tuple1+=tuple2                  #adding tuples

print(tuple2)
x=tuple1.count("hello")         #count func
print(x)

y=list(tuple1)
y[0]="bye"                      #changing value
tuple1=tuple(y)
print(tuple1)

z=list(tuple2)
z.append("cool")                   #append func
tuple2=tuple(z)
print(tuple2)

print(tuple2.index("bye"))          #index func
