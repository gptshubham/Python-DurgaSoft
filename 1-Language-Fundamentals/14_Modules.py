# modules : e.g; shubhmath module

# different ways to import a module

# # import <module_name>
# import shubhmath
# shubhmath.add(30,20)
# shubhmath.subtract(30,20)
# shubhmath.multiply(30,20)
# print(shubhmath.name)
# print(shubhmath.PI)

# # Module Aliasing:
# import shubhmath as sm
# sm.add(30,20)
# sm.subtract(30,20)
# sm.multiply(30,20)
# print(sm.name)
# print(sm.PI)
# # print(shubhmath.name)  # NameError: name 'shubhmath' is not defined
# # print(shubhmath.PI)

# # from -import: ---> most commonly used method to import modules
# from shubhmath import *
# add(30,20)
# subtract(30,20)
# multiply(30,20)
# print(name)
# print(PI)

# # Member Aliasing
# from shubhmath import subtract as sub, multiply as mul, square as sq
# sub(30,20)
# mul(30,20)
# sq(9)

# # Module Naming Conflicts
#
# from module1 import *
# from module2 import *
#
# add(30,20)
#
#
# from module2 import *
# from module1 import *
#
# add(30,20)
#
#
# from module2 import *
# from module1 import *
# def add(a,b):
#     print('Current Module add function')
#     print('The Sum:',a+b)
# add(30,20)
#
#
# from module2 import *
# def add(a,b):
#     print('Current Module add function')
#     print('The Sum:',a+b)
# from module1 import *
#
# add(30,20)
#
# # Note: most recent module/function will be considered
# # in case of a Naming Conflict

# How to solve Naming Conflict

# # Method 1 : don't import member import module only
# import module1
# import module2
# module1.add(30,20)
# module2.add(3,2)
#
# # Method 2 : import members with different aliased names
# from module1 import add as a1
# from module2 import add as a2
# a1(30,20)
# a2(3,2)

# # Reloading of Module
#
# import time
# import module1
# module1.add(30,20)
# print('program entering into sleeping state')
# time.sleep(45)
# print('waking up and calling updated function')
# import module1
# module1.subtract(30,20)
# # AttributeError: module 'module1' has no attribute 'subtract'

# # How to solve this problem
#
# import importlib
# import time
# import module1
# module1.add(30,20)
# print('program entering into sleeping state')
# time.sleep(45)
# print('waking up and calling updated function')
# importlib.reload(module1)
# import module1
# module1.subtract(30,20)


# how to find members of a module

# dir()

a = 10
b = 20
def add(a,b):
    return a+b
def product(a,b):
    return a*b

# print(dir())

# import math
# print(dir(math))

# # help
# import math
# help(math)

# help()

# special variables in Python Modules  --> __doc__, __file__, __name__

# print(__annotations__)
# print(__builtins__)
# print(__cached__)
# print(__doc__)
# print(__file__)
# print(__loader__)
# print(__name__)
# print(__package__)
# print(__spec__)

__doc__

print(__doc__)
import math
print(math.__doc__)
import random
# print(random.__doc__)

__file__

print('Absolute Path:',__file__)
import os
print('Relative Path:',os.path.relpath(__file__))
print('Directory Name:',os.path.dirname(__file__))

__name__

# indirect execution of Module3
import module3               # module3 ==> Indirect Execution
print('Current Module')

# import module3
print('we require only some functions but not all')
module3.f1()