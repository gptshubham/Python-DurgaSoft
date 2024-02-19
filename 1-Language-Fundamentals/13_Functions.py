# Functions

# # Basic Example
# def display(value):
#     print(value)
#
# display('Hello world')
# display(22)
# display(True)
# display(20+20)

# # Why to use Function ?
# a = 20
# b = 10
# print('The Sum :', a+b)
# print('The Difference :', a-b)
# print('The Product :', a*b)
# print('The Dividend :', a/b)
# a = 200
# b = 100
# print('The Sum :', a+b)
# print('The Difference :', a-b)
# print('The Product :', a*b)
# print('The Dividend :', a/b)
# a = 2000
# b = 1000
# print('The Sum :', a+b)
# print('The Difference :', a-b)
# print('The Product :', a*b)
# print('The Dividend :', a/b)

# # Ans: DRY Principle --> Don't Repeat Yourself (Code Re-usability)
# # calc Function
# def calc(arg1, arg2):
#     print('The Sum :', arg1 + arg2)
#     print('The Difference :', arg1 - arg2)
#     print('The Product :', arg1 * arg2)
#     print('The Dividend :', arg1 / arg2)
#
# calc(20,10)
# calc(200,100)
# calc(2000,1000)

# # greeting function
# def greeting(name):
#     print('Hello %s! Good Morning!' %name)
#
# greeting('Shubham')
# greeting(input('Enter Your Name : '))

# # write a function to take number as argument and
# # print its squared value
# def squareIt(number):
#     print('The Square of {} is {}'.format(number,number**2))
#
# squareIt(9)
# squareIt(float(input('Enter the Number : ')))

# # write a program to accept 2 numbers as input and return sum
# def addIt(num1,num2):
#     '''
#     addIt function takes two numbers as input, and
#     it provides their sum as output
#     '''
#     return num1 + num2
#     # print('Sum of {} and {} is {}'.format(num1,num2,num1+num2))
#
# result = addIt(20,30)
# print(result)
# print(addIt(40,50))


# # write a program to validate user's mobile number
# def validate_mobile_number(Mob_No):
#     if Mob_No.isdigit():
#         if len(Mob_No) == 10:
#             return True
#     else:
#         return False
#
# mobile_number = input('Enter Your Mobile Number : ')
# output = validate_mobile_number(mobile_number)
# print(output)

# # write a function to check wether given number is even of odd
# def even_odd(num):
#     if num.isdigit():
#         if int(num) % 2 == 0:
#             return 'Even'
#         else:
#             return 'Odd'
#     else:
#         return 'Not a Number!'
#
# number = input('Enter a Number : ')
# print(even_odd(number))

# # write a function to find factorial of a given number
# def factorialOf(n):
#     if n.isdigit():
#         n = int(n)
#         if n>=0:
#             fact = 1
#             while int(n)>1:
#                 fact *= n
#                 n -= 1
#             return fact
#     else:
#         return 'Invalid Input!'
#
# number = input('Enter a Number : ')
# factorial = factorialOf(number)
# print(factorial)

# # Returning multiple values
# def calc(a,b):
#     sum = a+b
#     sub = a-b
#     prod = a*b
#     div = a/b
#     return sum,sub,prod,div      # Tuple Packing
#
# t = calc(20,10)
# total,diff,product,dividend = t         # Tuple Unpacking
# print(t)
# print(type(t))
# print('Sum :',total)
# print('Difference :',diff)
# print('Product :',product)
# print('Dividend :',dividend)
#
# for values in t:
#     print(values)

# Types of Arguments

# # 1. Positional Arguments
#
# def sub(a,b):
#     return a-b
#
# # result = sub(20)
# # print(result)
# # TypeError: sub() missing 1 required positional argument: 'b'
# result = sub(20,10)
# print(result)              # 10
# result = sub(10,20)
# print(result)              # -10
# # result = sub(20,10,5)
# # print(result)
# # TypeError: sub() takes 2 positional arguments but 3 were given

# # 2. Keyword Arguments
# def sub(a,b):
#     return a - b
#
# result = sub(a=20,b=10)
# print(result)             # 10
# result = sub(b=10,a=20)
# print(result)             # 10
# # result = sub(x=20,a=10)
# # print(result)
# # TypeError: sub() got an unexpected keyword argument 'x'

# # using Positional and Keyword Arguments Simultaneously
# result = sub(10,b=20)
# print(result)             # -10
# # result = sub(a=10,20)
# # print(result)
# # SyntaxError: positional argument follows keyword argument
# # Note: we can use positional and keyword arguments simultaneously.
# # However, Keyword Arguments must follow Positional Arguments
# def subIt(a,b,c):
#     return a - b -c
# # result = subIt(20,10,b=5)
# # print(result)
# # TypeError: sub() got multiple values for argument 'b'
# # result = subIt(20,b=10,5)
# # print(result)
# # SyntaxError: positional argument follows keyword argument
# result = subIt(20,b=10,c=5)
# print(result)                  # 5

# # 3. Default Arguments
# def sub(a=0,b=0):
#     return a - b
#
# result = sub(20,10)
# print(result)              # 10
# result = sub(10,20)
# print(result)              # -10
# result = sub()
# print(result)              # 0
# result = sub(20)
# print(result)              # 20
# # result = sub(20,10,5)
# # print(result)
# # TypeError: sub() takes from 0 to 2 positional arguments
# # but 3 were given
#
# def wish(name='Guest',msg='Good Morning!'):
#     print('Hello',name,msg)
# wish()
# wish('Shubh','Good Evening!')
#
# def wish(name,msg='Good Morning!'):
#     print('Hello',name,msg)
# wish('Shubh','Good Night!')
#
# # def wish(name='Guest',msg):
# #     print('Hello',name,msg)
# # wish('Shubh','Good Evening!')
# # SyntaxError: parameter without a default follows parameter with a default
#
# # Note : Default Arguments must be last Arguments
# # We can't take Default Arguments after Non-Default Arguments

# Variable Length Arguments

# def f(*args):
#     print('The Type of args :',type(args))
#     print('The Number of Arguments Passed :',len(args))
#     print(args)
#
# f()
# f(10)
# f(10,20)
# f(10,20,30)
# f(10,20,30,40,50,60,70,80,90)

# # Basic Example : sumIt()
# def sumIt(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# result = sumIt(10,20)
# print(result)
# print(sumIt(10,20,30,40,50))
# print(sumIt(10,20,30,40,50,60,70,80,90,100))
# print(sumIt())

# # Positional Argument and Variable Length Argument Combination
# def sumOf(n, *args):
#     print(n)
#     print(args)
#
# sumOf(10)
# sumOf(10,20,30,40,50)
# # Note: all positional arguments should come first and then VLAs
# # Otherwise Positional Arguments will work only if
# # value is passed along with Keyword ==> Keyword Argument

# # Keyword Argument and Variable Length Argument Combination
# def sumit(*args, n):
#     print(args)
#     print(n)
#
# # sumof(10)
# # TypeError: sumof() missing 1 required keyword-only argument: 'n'
# # sumof(10,20)
# # TypeError: sumof() missing 1 required keyword-only argument: 'n'
# sumit(10, 20, 30, 40, n=50)
#
# # Note: after variable length argument if we are taking any normal
# # argument we should provide value using Keyword Only.

# # Default Arguments and Variable Length Arguments Combination
# def sumof(n=0,*args):
#     print(n)
#     print(args)
# sumof(7777)
# sumof(7777,20)
# sumof(7777,20,30,40,50)
#
# def sumit(*args,n=0):
#     print(n)
#     print(args)
# sumit(10)
# sumit(10,20)
# sumit(10,20,30,40,50)
# sumit(10,20,30,n=7777)

# # **kwargs
# def display(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     print('#' * 20)
#     print('keys\t\tvalues')
#     print('----\t\t------')
#     for (k,v) in kwargs.items():
#         print('{}\t\t{}'.format(k,v))
#     print('#'*20)
#
# display(Dhoni=7,Sachin=10,Kohli=18,Rohit=45)
# display(name='shubham',age=22,gender='male',address='India')

# # using *args and **kwargs together
# def printIt(*args,**kwargs):
#     print(type(args))
#     print(args)
#     print(type(kwargs))
#     for (k,v) in kwargs.items():
#         print('{} : {}'.format(k,v))
#
# printIt(7,10,18,45,Dhoni=7,Sachin=10,Kohli=18,Rohit=45)

# # Types of Variables (Variable Scopes)
#
# # Global vs Local Variables
# a = 10          # global variable
# def f1():
#     a = 7       # local variable
#     print('Local variable Value :',a)
#     print('Globla Variable Value :',globals()['a'])
#
# def f2():
#     global b    # global keyword --> global variable
#     b = 18
#     print(a)
#
# def f3():
#     c = 45
#     print(b)
#
# f1()
# f2()
# f3()
# print(a)
# print(b)
# # print(c)      # NameError: name 'c' is not defined

# # whether b is a loval variable or global variable
# a = 10
# for i in range(1):
#     b = 20
# print(a,b)


# Recursive Functions

# # write a python function to find factorial of a given number using recursion
# def factorial(n):
#     print(f'Finding factorial of {n}')
#     # stop condition
#     if n == 0:
#         result = 1
#     else:
#         result = n*factorial(n-1)
#     print(f'Completion of finding factorial of {n} and result is {result}')
#     return result
# print('Factorial of 5 is :',factorial(5))
# # print('Factorial of 6 is :',factorial(6))

# # write a function to find the Fibonacci series of n where n>2
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for i in range(10):
#     print(fibonacci(i),end=' ')


# # Anonymous Functions/ Lambda Functions

# # write a function to return square of given value
#
# # normal function
# def squareIt(n):
#     return n**2
#
# num = int(input('Enter a Number to Square : '))
# print(squareIt(num))
#
# # Anonymous/Lambda Function
# s = lambda n:n*n
# num = int(input('Enter a Number to Square : '))
# print(s(num))
# print(type(s))

# # lambda function to find sum of two given numbers
# num1 = int(input('Enter the first number : '))
# num2 = int(input('Enter the second number : '))
# s = lambda n1,n2:n1+n2
# print(f'The Sum of {num1} and {num2} =',s(num1,num2))

# # find biggest of two numbers using lambda functions
# num1 = int(input('Enter the first number : '))
# num2 = int(input('Enter the second number : '))
# s = lambda n1,n2:n1 if n1>n2 else n2
# print(f'Biggest of {num1} and {num2} is',s(num1,num2))

# # find biggest of three numbers using lambda functions
# num1 = int(input('Enter the first number : '))
# num2 = int(input('Enter the second number : '))
# num3 = int(input('Enter the third number : '))
# s = lambda n1,n2,n3:n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
# print(f'The Biggest of {num1}, {num2} and {num3} is',s(num1,num2,num3))


# filter()

# # given a list of numbers filter the even numbers
#
# # without lambda function
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
#
# L = [0,10,15,20,25,30,35,40,45]
# output = list(filter(is_even,L))
# print(output)
#
# # with lambda function
# L = [0,10,15,20,25,30,35,40,45]
# evens = list(filter(lambda n: n%2==0, L))
# odds = tuple(filter(lambda n:n%2!=0,L))
# print(evens)
# print(odds)

# # input: tuple of strings | output: tuple of strings where len(str) >= 3
# t = ('A','AA','AAA','AAAA','AAAAA')
# output = tuple(filter(lambda s:len(s)>=3,t))
# print(output)


# map()

# # given a list of numbers generate a list of squares of its values
#
# # without lambda function
# def squareIt(n):
#     return n**2
#
# L = [1,2,3,4,5]
# suare_list = list(map(squareIt,L))
# print(suare_list)
#
# # with lambda function
# L = [1,2,3,4,5]
# suare_list = list(map(lambda n:n**2,L))
# print(suare_list)

# # generate output by multiplying values from both lists
# L1 = [1,2,3,4]
# L2 = (10,20,30,40,50,60)     #***** Surprise!
# output = list(map(lambda n1,n2:n1*n2,L1,L2))
# print(output)       # [10, 40, 90, 160]


# reduce()

# # generate the product of all list items
# from functools import reduce
# L = [1,2,3,4,5]
# print(sum(L))
# output = reduce(lambda n,m:n*m,L)
# print(output)