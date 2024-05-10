# print('Hello world')

# Identifiers
'''
firstName = 'Shubham'
# print(firstname)
# NameError: name 'firstname' is not defined. Did you mean: 'firstName'?
print(firstName)
'''

# Reserved Words
'''
# pritn(firstName)
# NameError: name 'pritn' is not defined. Did you mean: 'print'?

import keyword
print(keyword.kwlist)
'''

# Python Data Types
'''
# basic data types --> int,str,float,bool,complex

# int data type
a = 10
print(a)
print(type(a))
print(id(a))

a = 0b1111
print(a)
a = 0o123
print(bin(15))
print(a)
print(oct(83))
a = 0xFACE
print(a)
print(hex(64206))

# float data type
f = 1.234
print(f)
print(type(f))
print(id(f))
# Exponential Form
f = 1.2e3
print(f)
f = 1.2E3
print(f)
f = 1.2e5
print(f)

# complex data type --> skipped

# bool data type
print(type(True))
print(type(False))
print(True + True)
print(False + True)
'''
# string data type
# # multi line string
# s = '''shubham
# kumar
# gupta'''
# print(s)
# s = """shubham
# kumar
# gupta"""
# print(s)
#
# print('Python Classes by "Durga Sir" are awesome')
# print("Python Classes by 'Durga Sir' are awesome")
# print("""Durga Sir's "Python Classes" are awesome""")

# Type Casting / Type Conversion
# skipped as we just covered this topic as part of our Week 1 curriculum at IIT Madras

# Fundamental Data Types vs Immutability
'''
a = 10
b = a
print(id(a))
print(id(b))
print(a is b)

s = 'shubham'
k = s
print(id(s))
print(id(k))
print(s is k)
'''

# Mutability
'''
L = [10,20,30,40]
print(L)
L[0] = 1111
print(L)

L1 = [10,20,30,40]
print(id(L))
print(id(L1))
print(L is L1)

s = 'shubham'
s1 = 'shubham'
print(id(s))
print(id(s1))
print(s is s1)
'''

#Collection --> list, tuple, set, frozenset, dict, bytes, bytearray, range

# List
'''

L = [10,20,30,40,10,True,'Dhoni',7.77,10,[11,12,13,14]]
print(type(L))
print(L[0])
print(L[-1])
print(L[2:6])
L[0] = 999
print(L)
# Empty List
L = []
print(L)
print(type(L))
'''

# Tuple
'''
t = (10,20,30,40,10,10,10,True,'MSD',10.5)
print(t,type(t))
t1 = 10,20,30,40
print(t1,type(t1))
print(t[0])
print(t[1])
print(t[-1])
print(t[2:6])
# t[0] = 999
# TypeError: 'tuple' object does not support item assignment
t = (10,20,30,40)
t1 = (10,20,30,40)
print(id(t))
print(id(t1))
print(t is t1)
#Empty Tuple
t = ()
print(t)
print(type(t))
# Single Value Tuple
t = (10)
print(t)
print(type(t))
t = (10,)
print(t)
print(type(t))
'''

# Set
'''
s = {10,20,30,40,10,10,10,True,'MSD',10.5}
print(s)
# print(s[0])
# TypeError: 'set' object is not subscriptable
# s[0] = 999
# TypeError: 'set' object does not support item assignment
s.add(999)
print(s)
# Empty Set
s = {}
print(s)
print(type(s))

t = ()
print(t,type(t))
s = set(t)
print(s)
print(type(s))
'''

# Dictionary
'''
d = {'fname':'shubham','sname':'gupta'}
print(d)
print(type(d))
print(d['fname'])
d['fname'] = 'abhishek'
print(d)
# print(d[0])
# KeyError: 0
d['gender'] = 'male'
print(d)
# Empty Dictionary
d = {}
print(d)
print(type(d))
'''

# None Data Type
'''
a = 10
print(a)
a = None
print(a)
print(id(a))
b = a
print(id(a))
print(id(b))
print(a is b)
a = None
b = None
c = None
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(b is c)
print(a is c)
print(id(None))

# None as return value of a function that does not return anything
def f():
    pass
print(f())
k = f()
print(k)
# None as default value of a variable
x = None
y = 100

if y == 10:
    x = 20

print(x)
'''

# Escape Characters
'''
s = 'shubhamkumargupta'
print(s)
# \t
s = 'shubham\tkumar\tgupta'
print(s)
# \n
s = 'shubham\nkumar\ngupta'
print(s)
# \'
d = 'Durga Sir\'s Python Class is Awesome'
print(d)
# \"
d = "\"Python\" is Awesome"
print(d)
# \\
# filePath = 'D:\durgaclasses\abc.txt'
# SyntaxWarning: invalid escape sequence '\d'
#   filePath = 'D:\durgaclasses\abc.txt'

filePath = 'D:\\durgaclasses\\abc.txt'
print(filePath)
'''