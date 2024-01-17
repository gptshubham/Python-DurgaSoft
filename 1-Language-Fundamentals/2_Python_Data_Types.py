# Session 8 : Python Data Types I
# print()

x = 10
# print(x)

# type()
'''
type_of_x = type(x)
print(type_of_x)
'''

# id()
'''
id_of_x = id(x)
print(id_of_x)
'''

'''
y = -10
print(type(y))
z = 1010010001000010000001000000001111112548554785544475511225444474
print(type(z))
'''

# int --> base --> Decimal, Binary, Octal, Hexa Decimal
# 1. Decimal --> most commonly used form
'''
a = 1111
print(a)
print(type(a))
'''
# 2. Binary --> prefix --> 0b or 0B
'''
b = 0B1111
print(b)
print(type(b))
'''
# 3. Octal (0-7) --> prefix --> 0o or 0O
'''
c = 0o123
print(c)
print(type(c))
print(0b1111 + 0o123)
'''
# 4. Hexa Decimal
'''
d = 0xface
print(d)
d = 0Xface
print(d)
d = 0xCAB
print(d)
# d = 0xBeer
# print(d)
'''
# Base Conversion
# to binary
'''
print(bin(10))
print(bin(0b10))
print(bin(0x123))
'''
# to octal
'''
print(oct(10))
print(oct(0b10))
print(oct(0x10))
'''

# Session 9 : Python Data Types II

# print(hex(10))

# float data type
'''
f = 1.234
# print(type(f))
# Exponential Form --> float data type
f = 1.2e3
print(f)
f = 1.2E3
print(f)

f = 12.0
print(type(f))
'''

# complex data type --> (skipped)

# boolean daya type
'''
t = True
print(type(t))
f = False
print(type(f))
'''

'''
age = 20
if age>18:
    print("You are eligible for driving !")
'''
'''
print(True)
print(True + True)
print(False - True)
print(True * False)
'''

# string data type
'''
s = "shubham"
print(s)
s = 'Kumar'
print(s)
'''
# multi line strings
'''
s = """Shubham
Kumar
Gupta"""
print(s)
'''

"""
s = '''Shubham
Kumar
Gupta'''
print(s)
"""

'''
s = "Python classes by 'Durga Sir' are awesome"
print(s)
s = 'Python classes by "Durga Sir" are awesome'
print(s)
s = """ "Python" classes by 'Durga sir' are awesome"""
print(s)
# Escape Characters
s = '\"Python classes\" by \'Durga Sir\' are awesome'
print(s)
'''

# Indexing --> Accessing Individual Characters of strings
'''
firstName = "shubham"
print(firstName[0])
print(firstName[4])
# print(firstName[11])
print(firstName[-1])
print(firstName[-5])
'''

# Slice --> Accessing substring out of a string
'''
firstName = "shubham"
print(firstName[2:4])
print(firstName[4:])
print(firstName[:4])
print(firstName[:])
print(firstName[4:11])

print(firstName[7:0:-1])
print(firstName[7::-1])

print(firstName[-4:-1])
print(firstName[-2:-4])
print(firstName[-4:-1:-1])
'''
# String Concatination
# First Character in uppercase and remaining in lowercase
'''
firstName = "shubham"
# print(firstName.upper())
output = firstName[0].upper() + firstName[1:]
print(output)
'''
# Last Character in uppercase and remaining in lowercase
'''
firstName = "shubham"
output = firstName[:-1] + firstName[-1].upper()
print(output)
# alternatively
end = len(firstName) -1
output = firstName[0:end] + firstName[end].upper()
print(output)
'''
# First and Last Characters in uppercase and remaining in lowercase
'''
firstName = "shubham"
end = len(firstName) -1
output = firstName[0].upper() + firstName[1:end] + firstName[-1].upper()
print(output)
'''

# Mathematical operators for Strings
'''
print(10+20)
print('10' + '20')
# print('10' + 20)
print(10*20)
print('10' * 20)
# print('10' * '20')
print('shubham ' * 5)
user = 'shubham' + ' ' + 'kumar' + ' ' + 'gupta'
print(user)
'''

# Type Casting

# int()
# str --> int
'''
s = '20'
n = int(s)
print(s,type(s))
print(n,type(n))
# print(int('10.5'))
# print(int('0b101010'))
'''
# float --> int
'''
f = 1.123
n = int(f)
print(n, type(n))
'''
# complex --> int ***
'''
c = 10 + 20j
n = int(c)
print(n)
'''
# bool --> int
'''
print(int(True))
print(int(False))
'''


# float()
'''
# bool --> float
print(float(True))
'''
# complex --> float
# print(float(10+20j))

# str --> float
'''
print(float('10'))
print(float('10.10'))
# print(float('0b1010'))
# print(float('ten'))
'''
# int --> float
'''
print(float(10))
print(float(0b10101))
print(float(0x1010))
'''


# complex()
'''
c = 10+20j
print(c.imag)
print(c.real)
'''
'''
print(complex(2))
print(complex(True))
print(complex('10'))
print(complex('10.5'))
'''
'''
c = complex(1,2)
print(c)
print(complex(10.5,20.1))
# print(complex('10','20'))
'''


# bool()
'''
print((bool()))
print(bool(''))
print(bool(0))
'''
# int --> float
'''
print(bool(0))
print(bool(1))
print(bool(0.00000000001))
print(bool(-1))
'''
# complex --> bool
'''
print(bool(0+0j))
print(bool(1+0j))
print(bool(0+1j))
'''
# float --> bool
'''
print(bool(0.0))
print(bool(10.5*0))
print(bool(0.0000001))
'''
# str --> bool
'''
print(bool('True'))
print(bool('False'))
print(bool('yes'))
print(bool('no'))
print(bool(''))       #*****
print(bool(' '))
'''


# str()
'''
print(str(123))
print(str(123.321))
print(str(10+20j))
print(str(0b1111))
print(str(True))
'''

# Fundamental Data Types vs Immutability
'''
a = 10
b = a
print(id(a))
print(id(b))
print(a is b)

a = 11
print(id(a))
print(id(b))
print(a is b)

b += 1
print(id(a))
print(id(b))
print(a is b)

a = 'shubham'
b = 'shubham'
print(a is b)

a = 22.22
b = 22.22
print(a is b)
'''

# Mutability
'''
L = [10,20,30,40]
print(L,id(L))
L[0] = 50
print(L,id(L))
'''
'''
L = [10,20,30,40]
L2 = L
L[0] = 90
print(L,L2)
print(L2 is L)
L2[1] = 70
print(L,L2)
print(L2 is L)
'''
'''
L = [10,20,30,40]
L2 = [10,20,30,40]
print(L is L2)
L[0] = 90
print(L,L2)
'''


# Collection --> list, tuple, set, frozenset, dict, bytes, bytearray, range

# List
'''
L = [10,10.5,'shubham',True,10]
print(L)
print(type(L))
print(L[0])
print(L[-1])
print(L[1:3])
L.append('Kumar')
L.append('Gupta')
print(L)
print(len(L))
'''

# set
s = {10,10.5,'shubham',True,10}
print(s)
print(type(s))