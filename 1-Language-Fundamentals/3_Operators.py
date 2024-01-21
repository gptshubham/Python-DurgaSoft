# Operators

# # Mathematical Operators
# print(10 + 2)
# print(10 - 2)
# print(10 * 2)
# print(10 % 2)
# print(10 / 2)
# print(10 // 2)
# # floor division
# print(10 / 3)
# print(10 // 3)
# print(10.5 // 2)          # **** Surprise!
# print(10.5 // 2.5)        # **** Surprise!
# # exponential
# print(10**3)
# print(3**3)
# print(3**3*3)
# # string concatenation
# print('shubham' + ' ' + 'kumar' + ' ' + 'gupta')
# # print('shubham' + 10)
# print('shubham' + '10')
# print('shubham' + str(10))
# # String Repetition
# print('shubham' * 3)
# # print('shubham'*'kumar')
# print('shubham' * int('5'))
# print('shubham' * 0)
# print('shubham '*2**2)
# # zero division error
# # print(10 / 0)
# # print(10.0 // 0)
# # print(10 % 0)

# # Relational Operators
# a = 10
# b = 15
# print(a > b)
# print(a >= b)
# print(a < b)
# print(a <= b)
# print('A' > 'a')
# print('a' < 'b')
# # ord()
# print(ord('a'))
# print(ord('A'))
# # chr()
# print(chr(97))
# print(chr(65))
# print(True > False)
# print(False <= True)
# # print('s' < 1000)
# print(ord("s") < 1000)
# print('aaa' > 'aab')
#
# a = 10
# b = 20
# if a > b:
#     print('a is greater than b')
# else:
#     print('a is not greater than b')
# # chaining of relational operators
# print(10 < 20)
# print(10 < 20 < 30)
# print(10 < 20 < 30 < 40)
# print(10 < 20 < 30 < 40 > 50)

# # Equality Operators
# print(10 == 20)
# print(10.5 == 10)
# print(10.0 == 10)
# print('shubham' == 'Shubham')
# print('shubham' == 10)
# print('shubham' == 10)
# print(True == False)
# print(True == 1)
# print('10' == 10)
# print('a' == 97)
# print(True == 1.0)
# # chaining of equality operators
# print(10 == 20 == 20.0)
# # difference between '==' and 'is' operator
# l1 = [10,20,30,40]
# l2 = [10,20,30,40]
# print(id(l1),id(l2))
# print(l1 is l2)
# print(l1 == l2)
# l3 = l1
# print(l1 is l3)
# print(l1 == l3)

# # Logical Operators
# print(10 < 20 < 30 and 30 < 40 and 40 > 35 and 'a' < 'b' and True)
# print(10 < 20 < 30 and 30 < 40 and 40 > 35 and 'a' > 'b' and True)
# print(10 < 20 < 30 and 30 < 40 and 40 > 35 or 'a' < 'b' and True)
# print(not True)
# print(not False)
#
# print([] == False)
# print([] == True)
#
# print('shubham' and 'kumar' and 'gupta')
# print('' and 'kumar' and 'gupta')
# print('shubham' or 'kumar' or 'gupta')
# print('' or 'shubham' or 'kumar' or 'gupta')
# print(False and 'shubham')
#
# userName = input('Enter username : ')
# # print(userName)
# password = input('Enter password : ')
# # print(password)
# if userName == 'shubham' and password == 'sochbeta':
#     print('Welcome')
# else:
#     print('Incorrect User Id or Password!')
#
# password = input('Enter the password')
# print(password,type(password))
# password = int(input('Enter the password'))
# print(password,type(password))

# # Bitwise Operators ---> skipped for Now

# # Compound Assignment Operators
# # +=
# x = 10
# x += 20
# print(x)
# # -=
# x = 10
# x -= 3
# print(x)
# # *=
# x = 10
# x *= 2
# print(x)
# # /=
# x = 10
# x /= 2
# print(x)
# # **=
# x = 10
# x **= 2
# print(x)
# # //=
# x = 10
# x //= 3
# print(x)

# # Increment and Decrement Operators
# x = 10
# x++
# print(x)                           # ***** Surprise
#
# x = 10
# x--
# print(x)                           # ***** Surprise
#
# x = 10
# ++x
# print(x)                             # ***** Surprise
# --x
# print(x)                             # ***** Surprise
# ++++++x
# print(x)                             # ***** Surprise
# ---x
# print(x)                             # ***** Surprise

# # Ternary / Conditional Operator
#
# # unary operator
# print(not 's')
#
# # binary operator
# print(10+2)
#
# # ternary operator
# a,b = 10,20
# x = 30 if a<b else 40
# print('x = ',x)
#
# # min value using ternary operator
# a = int(input('Enter First Number'))
# b = int(input('Enter Second Number'))
# min = a if a < b else b
# print('Minimum Value =',min)
#
# # nested Ternary operator
#
# # min of 3 numbers
# a = int(input('Enter First Number'))
# b = int(input('Enter Second Number'))
# c = int(input('Enter Third Number'))
# # min = a if a<b<c else b if b<c else c
# min = a if a<b and a<c else b if b<c else c
# print('min value =',min)
#
# # max of 3 numbers
# a = int(input('Enter First Number'))
# b = int(input('Enter Second Number'))
# c = int(input('Enter Third Number'))
# max = a if a>b and a>c else b if b>c else c
# print(max)
#
# a = int(input('Enter First Number'))
# b = int(input('Enter Second Number'))
# print('a is greater than b') if a>b else print('b is greater than a') if b>a else print('a and b are equal')

# Special Operators in Python

# # Identity Operator
# s1 = 'shubham'
# s2 = 'shubham'
# print(s1 is s2)
# print(s1 is not s2)
# print(id(s1),id(s2))
# L1 = [10,20,30,40]
# L2 = [10,20,30,40]
# print(L1 is L2)
# print(L1 is not L2)
# L3 = L1
# print(L1 is L3)
# print(id(L1),id(L2),id(L3))

# # Membership Operators
# s = 'shubham'
# print('m' in s)
# print('bh' in s)
# print('bharat' in s)
# L = [10,20,30,40,'shubham']
# print(10 in L)
# print(100 in L)
# print('shubh' in L[4])
# t = (90,80,70,60)
# print(90 in t)
# print(10 in t)
# s = {'shubham','kumar','gupta',11,22,33,44,True,False}
# print(False in s)

# Python Operator Precedence
print(10+20*3)
print((10+20)*3)

a = 30
b = 20
c = 10
d = 5
print((a + b)*c/d)
print((a + b)*(c/d))
print(a + (b*c)/d)