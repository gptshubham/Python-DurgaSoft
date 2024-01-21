# Python Data Types
# # print()
# x = 10
# print(x)
#
# # type()
# type_of_x = type(x)
# print(type_of_x)
#
# # id()
# id_of_x = id(x)
# print(id_of_x)


# y = -10
# print(type(y))
# z = 1010010001000010000001000000001111112548554785544475511225444474
# print(type(z))

# # int --> base --> Decimal, Binary, Octal, Hexa Decimal
# # 1. Decimal --> most commonly used form
# a = 1111
# print(a)
# print(type(a))
#
# # 2. Binary --> prefix --> 0b or 0B
# b = 0B1111
# print(b)
# print(type(b))
#
# # 3. Octal (0-7) --> prefix --> 0o or 0O
# c = 0o123
# print(c)
# print(type(c))
# print(0b1111 + 0o123)
#
# # 4. Hexa Decimal
# d = 0xface
# print(d)
# d = 0Xface
# print(d)
# d = 0xCAB
# print(d)
# # d = 0xBeer
# # print(d)
#
# # Base Conversion
# # to binary
# print(bin(10))
# print(bin(0b10))
# print(bin(0x123))
# # to octal
# print(oct(10))
# print(oct(0b10))
# print(oct(0x10))
# print(hex(10))

# # float data type
# f = 1.234
# # print(type(f))
# # Exponential Form --> float data type
# f = 1.2e3
# print(f)
# f = 1.2E3
# print(f)
#
# f = 12.0
# print(type(f))

# complex data type --> (skipped)

# # boolean daya type
# t = True
# print(type(t))
# f = False
# print(type(f))
#
# age = 20
# if age>18:
#     print("You are eligible for driving !")
#
# print(True)
# print(True + True)
# print(False - True)
# print(True * False)

# # string data type
# s = "shubham"
# print(s)
# s = 'Kumar'
# print(s)
# # multi line strings
# '''
# s = """Shubham
# Kumar
# Gupta"""
# print(s)
# '''
#
# """
# s = '''Shubham
# Kumar
# Gupta'''
# print(s)
# """
#
# s = "Python classes by 'Durga Sir' are awesome"
# print(s)
# s = 'Python classes by "Durga Sir" are awesome'
# print(s)
# s = """ "Python" classes by 'Durga sir' are awesome"""
# print(s)
# # Escape Characters
# s = '\"Python classes\" by \'Durga Sir\' are awesome'
# print(s)
#
# # Indexing --> Accessing Individual Characters of strings
# firstName = "shubham"
# print(firstName[0])
# print(firstName[4])
# # print(firstName[11])
# print(firstName[-1])
# print(firstName[-5])
#
# # Slice --> Accessing substring out of a string
# firstName = "shubham"
# print(firstName[2:4])
# print(firstName[4:])
# print(firstName[:4])
# print(firstName[:])
# print(firstName[4:11])
#
# print(firstName[7:0:-1])
# print(firstName[7::-1])
#
# print(firstName[-4:-1])
# print(firstName[-2:-4])
# print(firstName[-4:-1:-1])
#
# # String Concatination
# # First Character in uppercase and remaining in lowercase
# firstName = "shubham"
# # print(firstName.upper())
# output = firstName[0].upper() + firstName[1:]
# print(output)
#
# # Last Character in uppercase and remaining in lowercase
# firstName = "shubham"
# output = firstName[:-1] + firstName[-1].upper()
# print(output)
# # alternatively
# end = len(firstName) -1
# output = firstName[0:end] + firstName[end].upper()
# print(output)
#
# # First and Last Characters in uppercase and remaining in lowercase
# firstName = "shubham"
# end = len(firstName) -1
# output = firstName[0].upper() + firstName[1:end] + firstName[-1].upper()
# print(output)
#
# # Mathematical operators for Strings
# print(10+20)
# print('10' + '20')
# # print('10' + 20)
# print(10*20)
# print('10' * 20)
# # print('10' * '20')
# print('shubham ' * 5)
# user = 'shubham' + ' ' + 'kumar' + ' ' + 'gupta'
# print(user)

# # Type Casting
#
# # int()
# # str --> int
# s = '20'
# n = int(s)
# print(s,type(s))
# print(n,type(n))
# # print(int('10.5'))
# # print(int('0b101010'))
# # float --> int
# f = 1.123
# n = int(f)
# print(n, type(n))
# # complex --> int ***
# c = 10 + 20j
# n = int(c)
# print(n)
# # bool --> int
# print(int(True))
# print(int(False))
#
# # float()
# # bool --> float
# print(float(True))
# # complex --> float
# # print(float(10+20j))
#
# # str --> float
# print(float('10'))
# print(float('10.10'))
# # print(float('0b1010'))
# # print(float('ten'))

# # int --> float
# print(float(10))
# print(float(0b10101))
# print(float(0x1010))
#
# # complex()
# c = 10+20j
# print(c.imag)
# print(c.real)
#
# print(complex(2))
# print(complex(True))
# print(complex('10'))
# print(complex('10.5'))
#
# c = complex(1,2)
# print(c)
# print(complex(10.5,20.1))
# # print(complex('10','20'))
#
# # bool()
# print((bool()))
# print(bool(''))
# print(bool(0))
#
# # int --> bool
# print(bool(0))
# print(bool(1))
# print(bool(0.00000000001))
# print(bool(-1))
#
# # complex --> bool
# print(bool(0+0j))
# print(bool(1+0j))
# print(bool(0+1j))
#
# # float --> bool
# print(bool(0.0))
# print(bool(10.5*0))
# print(bool(0.0000001))
#
# # str --> bool
# print(bool('True'))
# print(bool('False'))
# print(bool('yes'))
# print(bool('no'))
# print(bool(''))             #***** Surprise!
# print(bool(' '))
#
# # str()
# print(str(123))
# print(str(123.321))
# print(str(10+20j))
# print(str(0b1111))
# print(str(True))

# # Fundamental Data Types vs Immutability
# a = 10
# b = a
# print(id(a))
# print(id(b))
# print(a is b)
#
# a = 11
# print(id(a))
# print(id(b))
# print(a is b)
#
# b += 1
# print(id(a))
# print(id(b))
# print(a is b)
#
# a = 'shubham'
# b = 'shubham'
# print(a is b)
#
# a = 22.22
# b = 22.22
# print(a is b)
#
# # Mutability
# L = [10,20,30,40]
# print(L,id(L))
# L[0] = 50
# print(L,id(L))
#
# L = [10,20,30,40]
# L2 = L
# L[0] = 90
# print(L,L2)
# print(L2 is L)
# L2[1] = 70
# print(L,L2)
# print(L2 is L)
#
# L = [10,20,30,40]
# L2 = [10,20,30,40]
# print(L is L2)
# L[0] = 90
# print(L,L2)

# #Collection --> list, tuple, set, frozenset, dict, bytes, bytearray, range
#
# # List
# L = [10,10.5,'shubham',True,10]
# print(L)
# print(type(L))
# print(L[0])
# print(L[-1])
# print(L[1:3])
# L.append('Kumar')
# L.append('Gupta')
# print(L)
# print(len(L))
#
# # Tuple
# t = (10,10.5,'shubham',True,10)
# print(t,type(t))
# print(t[2])
# print(t[-1])
# print(t[1:4])
# # t[0] = 7777
# # t.append(50)
# # t.remove(10.5)
# # Empty Tuple
# t = ()
# print(t,type(t))
# # Single Valued Tuple
# t = (10)
# print(t,type(t))              # *** Surprised!
# t = (10,)
# print(t,type(t))
# t = (10,20,30,40,)
# print(t,type(t))
# t = 10,20,30,40
# print(t,type(t))             # ***** Surprised!
#
# # Sets
# s = {10,10.5,10,'shubham',10,True,10,10}
# print(s)
# print(type(s))           # Duplicates are not allowed
# # print(s[0])
# # print(s[0:4])
# # adding elements to set
# # add()
# s.add(50)
# print(s)
# s.add(60)
# print(s)
# s.remove(50)
# print(s)
#
# # Empty Set                     # *** Surprise!
# s = {}
# print(s,type(s))
# s = set({})
# print(s)
# print(len(s))
# print(type(s))
#
# # frozenset
# s = {10,20,30,40}
# fs = frozenset(s)
# print(s,type(s))
# print(fs,type(fs))
# # fs.add(50)
# # fs.remove(10)

# # Dictionary
# d = {100:'shubham',200:'kumar',300:'gupta'}
# print(d,type(d))
# print(d[100])
# user = {'name':'shubham','age':22,'gender':'male'}
# print(user['name'])
#
# d = {}
# d['name'] = 'shubham'
# print(d)
# d['age'] = 22
# print(d)
# d['gender'] = 'male'
# print(d)
# d ['name'] = 'abhi'
# d['age'] = 26
# print(d)
#
# d = {}
# d[100] = 'shubham'
# d['abhi'] = 200
# d['flag'] = True
# print(d)
#
# # duplicate : key vs value
# a = 100
# b = 200
# c = 300
# d = {}
# d[a] = 'shubham'
# d[b] = 'shubham'
# d[c] = 'shubham'
# print(d)
# d[a] = 'abhi'
# d[b] = 'shubh'
# d[c] = 'sonal'
# print(d)
# d = {100:'shubham',100:'kumar',100:'gupta'}          # *** Surprise!
# print(d)
# d = {100:['shubham','kumar','gupta']}
# print(d)
# print(d[100][0])
# print(d[100][1])
# print(d[100][10])
# d = {100:'shubham','100':'kumar'}
# print(d)

# # range --> data type as well as function
# # form-1 --> range(n)
# r = range(10)
# print(type(r))
# for x in r:
#     print(x)
#
# # form-2 --> range(begin,end)
# r = range(1,10)
# for x in r:
#     print(x)
#
# # form-3 --> range(begin,end,increment/decrement)
# r = range(1,11,2)
# for x in r:
#     print(x)
#
# r = range(1,11,3)
# for x in r:
#     print(x)
#
# r = range(20,10,-1)
# for x in r:
#     print(x)
#
# l = []
# for x in range(0,101,5):
#     l.append(x)
# print(l)
#
# r = range(10)
# print(r[0])
# print(r[-1])
# print(r[2:6])        # returns range object
# # r[1] = 7777

# # bytes data type
# l = [10,20,30,40]
# b = bytes(l)
# print(b,type(b))
# print(b[0])
# print(b[-1])
# print(b[1:3])
# b1 = b[1:3]
# for x in b1:
#     print(x)
# # b[0] = 77

# # bytearray data type
# l = [10,20,30,40]
# b = bytearray(l)
# print(b,type(b))
# # b[0] = 7777
# b[0] = 255
# for x in b:
#     print(x)

# # None Data Types
# x = 10
# print(x)
# x = None
# print(x)
# print(type(x))
# print(id(x))
# print(id(None))
# a = None
# b = None
# c = None
# print(id(a), id(b), id(c))
# None as return value of a function that does not return anything
# def f2():
#     pass
#
# d = f2()
# print(d)
# print(id(d))
# # None as default value of a variable
# x = None
# y = 100
#
# if y == 10:
#     x = 20
#
# print(x)
#
# def f1():
#     print('Hello')
#
# r = f1()
# print(r)

# # Escape Characters
# s = 'ShubhamKumarGupta'
# print(s)
# # \t
# s = 'Shubham\tKumar\tGupta'
# print(s)
# # \n
# s = 'Shubham\nKumar\nGupta'
# print(s)
# print(s)
# # \'
# s = 'Python\'s Popularity keeps on growing'
# print(s)
# # \"
# s = "teacher said \"Honesty is best polycy\" in Moral Science's Lecture."
# print(s)
# # \\
# filePath = 'D:\\durgaclasses\\abc.txt'
# print(filePath)

# # Comments                      #*** Surprise!
# # --> Single line comment
# '''
# Multi-Line            # It is DocString but not Multi-line Comment
# Comment               # Python does not have any special syntax for
# 1st Preference        # Multi-line String
# '''                   # This is exactly How we write multi-line comments
# """                   # in Python using # in the beginning of
# Multi-line            # every line.
# comment
# """

# Constant --> Not applicable in Python
# convention
MAX_VALUE = 10  # It is a constant , don't change it's value
print(MAX_VALUE)
MAX_VALUE = 20
print(MAX_VALUE)
# as said constant concept is not applicable in Python
