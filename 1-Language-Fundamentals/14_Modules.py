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

# print(__doc__)
# import math
# print(math.__doc__)
# import random
# # print(random.__doc__)

__file__

# print('Absolute Path:',__file__)
# import os
# print('Relative Path:',os.path.relpath(__file__))
# print('Directory Name:',os.path.dirname(__file__))

__name__

# # indirect execution of Module3
# import module3               # module3 ==> Indirect Execution
# print('Current Module')

# # import module3
# print('we require only some functions but not all')
# module3.f1()


# working with random module

# import random
# L = dir(random)
# print(L)
#
# help(random)

# from random import *

# # random()
# for i in range(10):
#     print(random())

# # uniform()
# for i in range(10):
#     print(uniform(1,100))

# # randint()
# for i in range(10):
#     print(randint(1,10000))

# # randrange()
# for i in range(10):
#     print(randrange(1,11,2),end=' ')
# print()
# for i in range(10):
#     print(randrange(0,11,2),end=' ')
# print()
# for i in range(10):
#     print(randrange(0,100,10),end=' ')

# # choice()
# L = ['Dhoni','Kohli','Sachin','Rohit','SKY','Gill','Hardik']
# for i in range(10):
#     print(choice(L))

# # Program 1: generate a random alphabet symbol
# from random import choice
# # print(ord('A'))  # 65
# # print(ord('Z'))  # 90
# # print(ord('a'))    # 97
# # print(ord('z'))    # 122
#
# # creating a list of alphabet symbols
# alphabets = []
# for i in range(ord('A'),ord('Z')+1):
#     alphabets.append(chr(i))
# for i in range(ord('a'),ord('z')+1):
#     alphabets.append(chr(i))
#
# # confirming list
# # print(alphabets)
#
# # generating random alphabets from the list using choice()
# for i in range(10):
#     print(choice(alphabets), end=' ')


# # Program 2: OTP Generation
# # generate a 6 digit random number which can used as OTP
#
# from random import randint
# # creating an Empty list 'otp'
# otp = []
# # generating OTP using for loop and randint()
# for i in range(6):
#     otp.append(randint(0,9))
# # confirming otp list
# print(otp)
# # converting int values of otp list into string using map()
# otp = list(map(str,otp))
# print(otp)
# # joining otp
# otp = ''.join(otp)
# # printing output
# print(otp)
#
# # Alternatively : Shortcut Method 😎 All Hail Time and Space Complexity
# print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
#
# # Alternatively : Ultra Shortcut -> Not Preferred as it can't generate otps starting from 0 like 000000,000001 etc.
# print(randint(100000,999999))


# # Program 3: Password Generation
# # generate random password of 8 length where 1st, 3rd, 5ht and 7th
# # are alphabet symbols and 2nd, 4th, 6th and 8th are digits
#
# from random import *
# # creating alphabet list using for loop, ord() and chr()
# alphabets = []
# for i in range(ord('A'),ord('Z')+1):
#     alphabets.append(chr(i))
# for i in range(ord('a'),ord('z')+1):
#     alphabets.append(chr(i))
# # creating digits range odject
# digits = range(0,9)
# # creating password variable
# password = ''
# # creating password using for loop, str concatenation,and choice()
# for i in range(1,9):
#     if i%2 == 0:
#         password += str(choice(digits))
#     else:
#         password += choice(alphabets)
# # printing output
# print(password)
#
# # Alternatively : Shortcut Method
# print(choice(alphabets),randint(0,9),choice(alphabets),randint(0,9),choice(alphabets),randint(0,9),choice(alphabets),randint(0,9),sep='')

# Program 4: write a program to generate fake employee data for database testing

from random import *

# alphabets list
alphabets = []
for i in range(ord('A'),ord('Z')+1):
    alphabets.append(chr(i))
for i in range(ord('a'),ord('z')+1):
    alphabets.append(chr(i))

# digits str
digits = '0123456789'

# city option
cities = ['Hyderabad','Chennai','Bangalore','Pune','Delhi','Mumbai']

# designation options
designations = ['Software Engineer','Senior Software Engineer','Team Lead','Project Lead','Project Manager']
# Employee Name
def get_emp_name():
    # random length of employee name between 3 and 10
    emp_name_len = randint(3,10)
    # employee name generation
    emp_name = ''
    for i in range(emp_name_len):
        emp_name += choice(alphabets)
    # return statement
    return emp_name.title()

# Employee Number
def get_emp_no():
    # generating employee number
    emp_no = 'e-'
    for i in range(4):
        emp_no += choice(digits)
    # return statement
    return emp_no

# Employee salary
def get_emp_salary():
    # generating salary
    salary = round(uniform(10000,50000),2)
    # return statement
    return salary

# Employee Mobile Number
def get_emp_mob_no():
    # first digit
    mob_no = str(choice(range(6,10)))
    # remaining 9 digits
    for i in range(9):
        mob_no += str(choice(range(10)))
    # return statement
    return mob_no

# Employee City
def get_emp_city():
    # choosing employee city
    city = choice(cities)
    # return statement
    return city

# Employee Designation
def get_emp_designation():
    # choosing employee designation
    designation = choice(designations)
    # return statement
    return designation

def get_fake_emm_data():
    print('Employee Name: ',get_emp_name())
    print('Employee Number: ',get_emp_no())
    print('Employee salary: ',get_emp_salary())
    print('Employee City: ',get_emp_city())
    print('Employee Mobile Number: ',get_emp_mob_no())
    print('Employee Designation: ',get_emp_designation())

# generating employee data for 1 employee
# get_fake_emm_data()

# generating employee data for n employees
n = int(input('Enter the No. of Employees : '))
for i in range(n):
    get_fake_emm_data()
    print()
