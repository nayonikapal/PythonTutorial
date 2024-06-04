
# 0 1 1 2 3 5 8 13 21

num = int(input("Enter the number you wnt to print fibonacci series : "))
first = 0
second = 1
print(str(first) + " " + str(second), sep=" ", end=" ")
for i in range(num):
    res = first + second
    print(str(res), sep=" ", end=" ")
    first = second
    second = res
    
