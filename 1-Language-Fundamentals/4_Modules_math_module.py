# Module  --> python sourse file --> includes most commonly used variables, functions and classes. High level --> A bunch of functions grouped together
# Package --> a bunch of Modules grouped together in a folder
# Library --> a bunch of Packages grouped together in a folder
# Advantage : code reusability
import shubhmath as sm         # importing shubhmath as sm --> (command aliasing)
print(sm.PI)
print(sm.name)
print(sm.add(10,20))
print(sm.multiply(10,20))
print(sm.mod(100,3))
# print(shubhmath.name)         # once aliased the original name cannot be used .

# Accessing members of module directly without using the module name again and again
from shubhmath import PI
print(PI)
from shubhmath import subtract
print(subtract(10,5))

from shubhmath import *
print(PI)
print(add(10,20))
print(square(9))
print(divide(20,10))
print(name)

from shubhmath import add as a    # command aliasing with functions of a module
print(a(100,200))
from shubhmath import multiply as m
print(m(10,20))

# # Math Module -- predefined
# import math
# print(math.sqrt(16))
# print(math.pi)
# from math import *
# print(sqrt(25))
# print(pi)
# print(add(20,30))
# print(floor(10.5))
# print(ceil(10.5))
# import math as m
# print(m.pi)
# print(m.sqrt(36))
# print(m.floor(10.5))
# print(m.ceil(10.5))
# # print(dir(math))          # dir() lists all the functions,variables available in a module
#
# # calculating area
# from math import *
# r = int(input('Enter the radius'))
# area = pi * r**2
# print('The area =',area)
from random import randint
print(randint(0,9))