# Session 8 : Python Data Types I
# print()

x = 10
print(x)


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
