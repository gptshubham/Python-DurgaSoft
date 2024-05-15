# Arithmetic Operators
'''
print(10//3)
print(10%3)
print(10**3)
print(10.5//3)
print(10//3.5)
print(10.5//3.5)
print('Shubham'+' Kumar '+'Gupta')
print('Shubham'*5)
# print('Shubham'*2.5)
# TypeError: can't multiply sequence by non-int of type 'float'
'''

# Relational Operators
'''
# ord()
print(ord('A'))
print(ord('a'))
# chr()
print(chr(65))
print(chr(97))

print('a' > 'A')
print('z' > 'a')
'''

# Equality Operators
'''
# Equality(==) vs. Assignment(=)
L1 = 10,20,30,40
print(L1)
L2 = 10,20,30,40
print(L2)
print(L1 == L2)
L3 = [50,60,70,80]
print(L1 == L3)
# Equality(==) vs Identity(is)
L1 = [10,20,30,40]
L2 = [10,20,30,40]
print(L1 == L2)
print(L1 is L2)
'''

# Compound Assignment Operator
'''
a = 10
print(a)
a += 2
print(a)
a -= 4
print(a)
a *= 5
print(a)
a /= 2
print(a)
a //= 3
print(a)
a %= 5
print(a)
'''

# Increment and Decrement
'''
a = 10
print(a)
# a++
# SyntaxError: invalid syntax
a += 1
print(a)
# a--
# SyntaxError: invalid syntax
a -= 1
print(a)
'''

# Ternary / Conditional Operator
# unary operator
'''
print(not 's')
print(not '')
'''

# binary operator
'''
print(10+2)
print(10-2)
print(10*2)
print(10/2)
print(10//3)
print(10%3)
'''

# ternary operator
'''
a,b = 10,20
x = 30 if a<b else 40
print('x = ',x)
# Example1 : Minimum Value
a,b = 10,20
print(f'minimum of a and b is {a if a<b else b}')
'''

# Nested Ternary Operator
'''
# Example 2 : Minimum of Three given Values
a,b,c = 30,10,20
print(f'Minimum of a, b and c is {a if a<b<c else b if b<c else c}')
'''

# Math Module

# different ways to import a module
'''
import math
print(math.sqrt(25))
print(round(math.pi,2))

import math as m
print(m.sqrt(49))
print(round(m.pi,2))

from math import sqrt,pi
print(sqrt(81))
print(round(pi,2))
'''

# important functions of math module
'''
import math
print(math.ceil(10.7))
print(math.floor(10.7))
print(math.pow(10,2))
print(math.factorial(6))

# dir()
print(dir(math))

from random import randint
print(randint(0,10))
print(randint(0,10))
print(randint(0,10))
print(randint(0,10))
print(randint(0,10))
print(randint(0,10))
'''

# Input and output Statements
'''
# reading dynamic input from keyboard
fname = input("Enter your first name : ")
mname = input("Enter your middle name : ")
lname = input('Enter your last name : ')
age = int(input('Enter your age : '))
print(fname,mname,lname,age)

# taking input form user and printing sum
fnum = int(input('Enter first number : '))
snum = int(input('Enter second number : '))
print(f'The Sum of {fnum} and {snum} is {fnum + snum}')

# eval()
x = eval('10,20,30')
print(x,type(x))

# unpacking and assigning
a,b,c = [10,20,30]
print(a,b,c)
'''

