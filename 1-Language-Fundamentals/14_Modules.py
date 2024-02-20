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
# from Module1 import *
# from Module2 import *
#
# add(30,20)
#
#
# from Module2 import *
# from Module1 import *
#
# add(30,20)
#
#
# from Module2 import *
# from Module1 import *
# def add(a,b):
#     print('Current Module add function')
#     print('The Sum:',a+b)
# add(30,20)
#
#
# from Module2 import *
# def add(a,b):
#     print('Current Module add function')
#     print('The Sum:',a+b)
# from Module1 import *
#
# add(30,20)
#
# # Note: most recent module/function will be considered
# # in case of a Naming Conflict

# How to solve Naming Conflict

# # Method 1 : don't import member import module only
# import Module1
# import Module2
# Module1.add(30,20)
# Module2.add(3,2)
#
# # Method 2 : import members with different aliased names
# from Module1 import add as a1
# from Module2 import add as a2
# a1(30,20)
# a2(3,2)

# # Reloading of Module
#
# import time
# import Module1
# Module1.add(30,20)
# print('program entering into sleeping state')
# time.sleep(45)
# print('waking up and calling updated function')
# import Module1
# Module1.subtract(30,20)
# # AttributeError: module 'Module1' has no attribute 'subtract'

# # How to solve this problem
#
# import importlib
# import time
# import Module1
# Module1.add(30,20)
# print('program entering into sleeping state')
# time.sleep(45)
# print('waking up and calling updated function')
# importlib.reload(Module1)
# import Module1
# Module1.subtract(30,20)



