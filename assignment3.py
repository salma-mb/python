# # num = int(input("enter a number:"))
# # if num % 2 == 0:
# #  print("num")
# # else:
# #  print("odd")
#
#
# def greetings(name):
#  print("hello", name)
#  greetings("salama")
#

# def add(a, b):
#     return a+b
# result = add(3, 5)
# print(result)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#          return n * factorial(n - 1)
# print(factorial(5))

import math
def calculate_area(radius):
    area = math.pi * radius ** 2
    return area
radius = float(input("enter the radius of the circle:"))
print(calculate_area(radius))
