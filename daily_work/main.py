# from fibo import myFunc as f
# f('test_test')

# import sys

# print(sys.__name__)

# import random

# number = float(random.randint(1,10))

# user_input = float(input())

# if number == user_input:
#     print('You are win')

# if number > user_input:
#     print('You number is smaller')
# if number < user_input:
#     print('You number is bigger')

# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
import math
a=4
b=6
h=2
r = 5

print('rectangle = ', (a*b)*2)
print('triangle = ', (0.5*h*a))
circle = math.pi*(math.pow(r,2))
print('triangle = ', circle)