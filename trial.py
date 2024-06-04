# n=5
# for i in range(1, n + 1):
#     # Print left stars
#     for j in range(i):
#         print("*", end="")
#     # Print spaces
#     for j in range(2 * (n - i)):
#         print(" ", end="")


# for i in range(0, 5):
#     for j in range(0, i+1):
#         print("* ",end="")
#     print()
# n=185
# t=n%10
# while t!=0:
#     print(t)
#     break

# # Given list
# numbers = [1, 2, 3, 4, 5]

# # Create a list of tuples
# result = []
# for num in numbers:
#     result.append((num, num ** 3))

# # Print the result
# print(result)


# Given list
# numbers = [64, 34, 25, 12, 22, 11, 90]

# # Perform bubble sort
# n = len(numbers)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# # Print the sorted list
# print("Sorted list:", numbers)

# gn=int(input("enter num"))
# print(gn%2)
# print(gn//3)
# print(gn//5)
# print(gn//7)

# s=[]
# for i in s:
#     print(type(s))
# if s==True:
#     print("no")

# rows = 10
# for i in range(rows, 0, -1):
#     for j in range(rows-i):
#         print(" ", end="")
#     for j in range(i-1):
#         print("*", end="")
#     print()

import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

my_string = '*'
if my_string in string.ascii_lowercase:
   print("'{0}' is a lowercase letter.".format(my_string))
