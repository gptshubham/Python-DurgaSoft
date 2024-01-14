# Session 8 : Python Data Types I
# print()

x = 10
# print(x)

# type()
"""
type_of_x = type(x)
print(type_of_x)
"""

# id()
"""
id_of_x = id(x)
print(id_of_x)
"""

"""
y = -10
print(type(y))
z = 1010010001000010000001000000001111112548554785544475511225444474
print(type(z))
"""

# int --> base --> Decimal, Binary, Octal, Hexa Decimal
# 1. Decimal --> most commonly used form
"""
a = 1111
print(a)
print(type(a))
"""
# 2. Binary --> prefix --> 0b or 0B
"""
b = 0B1111
print(b)
print(type(b))
"""
# 3. Octal (0-7) --> prefix --> 0o or 0O
"""
c = 0o123
print(c)
print(type(c))
print(0b1111 + 0o123)
"""
# 4. Hexa Decimal
"""
d = 0xface
print(d)
d = 0Xface
print(d)
d = 0xCAB
print(d)
# d = 0xBeer
# print(d)
"""
# Base Conversion
# to binary
"""
print(bin(10))
print(bin(0b10))
print(bin(0x123))
"""
# to octal
"""
print(oct(10))
print(oct(0b10))
print(oct(0x10))
"""

# Session 9 : Python Data Types II

# print(hex(10))

# float data type
"""
f = 1.234
# print(type(f))
# Exponential Form --> float data type
f = 1.2e3
print(f)
f = 1.2E3
print(f)

f = 12.0
print(type(f))
"""

# complex data type --> (skipped)

# boolean daya type
"""
t = True
print(type(t))
f = False
print(type(f))
"""

"""
age = 20
if age>18:
    print("You are eligible for driving !")
"""
"""
print(True)
print(True + True)
print(False - True)
print(True * False)
"""

# string data type
"""
s = "shubham"
print(s)
s = 'Kumar'
print(s)
"""
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
print(int(True))
print(int(False))

