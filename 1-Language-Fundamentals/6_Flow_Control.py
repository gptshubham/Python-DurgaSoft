# Flow Control Statements

# Conditional / Selection Statements

# # Indentation
# for i in range(10):
#     print('Hello')
#     print('world')
#      print('Hi')

# # 1. if
# user = input('Enter Your Name: ')
# if user == 'Shubham':
#     print('Hello Shubham Good Morning !!!')
# print('How are you?')
# # () optional in python for if statement
# user = input('Enter Your Name: ')
# if (user == 'Shubham'):
#     print('Hello Shubham Good Morning !!!')
# print('How are you?')

# # 2. if-else
# user = input('Enter Your Name: ')
# if user == 'Shubham':
#     print('Hello Shubham, Good Morning !!!')
# else:
#     print('Hello Guest, Good Morning !!!')
# print('How are you?')

# # 3. if-elif-else ===> a substitute for Switch Statement
# brand = input('Enter Your Favourite Brand: ')
# if brand == 'RC':
#     print("It is children's brand!")
# elif brand == 'KF':
#     print("It is not that much kick!")
# elif brand == 'KO':
#     print("It is too light!")
# elif brand == 'FO':
#     print("Buy one get one free!")
# else:
#     print("Other brands are not recommended!")

# # Program -> write a program to find greatest of 2 given numbers
# n1 = int(input('Enter First Number : '))
# n2 = int(input('Enter Second Number : '))
# if n1 > n2:
#     print(n1,'is greater!')
# else:
#     print(n2,'is greater!')

# # Program -> write a program to find greatest of 3 given numbers
# n1 = int(input('Enter First Number : '))
# n2 = int(input('Enter Second Number : '))
# n3 = int(input('Enter Third Number : '))
# if n1 > n2 and n1 > n3:
#     print(n1,'is the greatest number!')
# elif n2 > n3:
#     print(n2,'is the greatest number!')
# else:
#     print(n3,'is the greatest number!')

# # Program -> write a program to find smallest of 2 given numbers
# n1 = int(input('Enter First Number : '))
# n2 = int(input('Enter Second Number : '))
# if n1 < n2:
#     print(n1,'is the smallest!')
# else:
#     print(n2,'is the smallest!')

# # Program -> write a program to find smallest of 3 given numbers
# n1 = int(input('Enter First Number : '))
# n2 = int(input('Enter Second Number : '))
# n3 = int(input('Enter Third Number : '))
# if n1 < n2 and n1 < n3:
#     print(n1,'is the smallest number!')
# elif n2 < n3:
#     print(n2,'is the smallest number!')
# else:
#     print(n3,'is the smallest number!')

# # write a program to check whether the given number is even or odd
# n = int(input('Enter A Number : '))
# if n > 0:
#     if n % 2 == 0:
#         print(n,'is even')
#     else:
#         print(n,'is odd')
# else:
#     print('Invalid Input!')

# # write a program to check whether a given number is between 1 and 100 (inclusive)?
# n = int(input('Enter A Number : '))
# if n >= 1 and n <= 100:
#     print(n,'is between 1 and 100')
# else:
#     print(n,'is not between 1 and 100')

# # Mini Project: Number to Word Converter
# # write a program to take a single digit number from the keyboard and
# # print its value in english word
# n = int(input('Enter A Single Digit Number : '))
# if n == 0:
#     print('ZERO')
# elif n == 1:
#     print('ONE')
# elif n == 2:
#     print('TWO')
# elif n == 3:
#     print('THREE')
# elif n == 4:
#     print('FOUR')
# elif n == 5:
#     print('FIVE')
# elif n == 6:
#     print('SIX')
# elif n == 7:
#     print('SEVEN')
# elif n == 8:
#     print('EIGHT')
# elif n == 9:
#     print('NINE')
# else:
#     print('Please Enter a Valid Input!')
# Alternatively --> using Dictionary
# d = {0:'ZERO',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'}
# n = int(input('Enter A Single Digit Number : '))
# if n in d:
#     print(d[n])
# else:
#     print('Please Enter a Valid Input!')


# Iterative Statements

# 1. for loop

# # print characters present in the given string
# s = input('Enter any string : ')
# for char in s:
#     print('the current character is',char)

# # print characters present in the given string index-wise
# s = input('Enter any string : ')
# i = 0
# for char in s:
#     print('character at {} index ='.format(i),char)
#     i+=1
# # Alternatively --> using string formatting
# s = input('Enter any string : ')
# i = 0
# for char in s:
#     print('character at %d index =' % i,char)              # we can use %i as well instead of %d
#     i+=1

# # print Dhoni 10 times using for loop
# for i in range(10):
#     print(i,'Dhoni')
# # Alternatively
# for i in range(1,11):
#     print(i,'Kohli')

# # print number from 0 to 10
# for i in range(11):
#     print(i)

# # print odd number from 0 to 20
# for i in range(20):
#     if i%2 != 0:
#         print(i)
# # Alternatively
# for i in range(1,20,2):
#     print(i)

# # print numbers from 10 to 1 (descending order)
# for i in range(10,0,-1):
#     print(i)

# # print sum of numbers present in a given list
# L = []
# for i in range(0,4):
#     L.append(int(input('Enter a number : ')))
# # print(L)
# sum = 0
# for i in L:
#     sum += i
# print('Sum =',sum)
# # Alternatively using eval()
# L = eval(input('Enter a List : '))
# print(L)
# sum = 0
# for i in L:
#     sum += i
# print('Sum =',sum)

# while loop

# # print numbers from 1 to 10 using while loop
# i = 1
# while i<=10:
#     print(i)
#     i += 1

# # print the sum of first n natural numbers
# n = int(input('Enter the value of n : '))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# # print('The sum of first {} natural numbers is {}'.format(n,sum))
# print('The sum of first %i natural numbers is %i .' %(n,sum))

# # infinite loops

# # write a program to prompt user to enter your favourite player
# # untill entering Dhoni
# player = ''
# while player != 'Dhoni':
#     player = input('Enter your favourite player name : ')
# print('Thank you for confirmation!')
# print('Your favourite player is %s' %player)

# # userName Password Program
# username = 'sanki aadmi'
# password = 'kalachittha'
# user = ''
# pwd = ''
# while user != username or pwd != password:
#     user = input('Enter the username : ')
#     pwd = input ('Enter the password : ')
# print('Welcome!')
# # Alternatively :
# username = 'sanki aadmi'
# password = 'kalachittha'
# user = ''
# pwd = ''
# while True:
#     user = input('Enter the username : ')
#     pwd = input ('Enter the password : ')
#     if user == username and pwd == password:
#         print('welcome %s !' %user)
#         break
#     else:
#         print('Invalid Username or Password! \n Please Try Again!')

# # nested loops

# for i in range(4):
#     for j in range(4):
#         print(i,j)


# Transfer Statements

# 1. break
# # Basic Example
# for i in range(10):
#     if i==5:
#         print('Enough of that Stupid Loop!')
#         break
#     print(i)

# Qsn: Which Loop will break in case of following Programs:
# for i in range(10):
#     for j in range(10):
#         if j == 5:
#             print('Loop Completed!')
#             break
#         print(i,j)

# for i in range(10):
#     for j in range(10):
#         if i == 5:
#             print('Loop Skipped!')
#             break
#         print(i,j)

# for i in range(10):
#     if i == 5:
#         print('Loop Completed!')
#         break
#     for j in range(10):
#         print(i,j)

# for i in range(10):
#     for j in range(10):
#         print(i,j)
#     if j == 5:
#         print('Loop Completed!')
#         break

# Cart Insurance Example with break statement
# cart = [10,20,600,60,70]
# for item in cart:
#     if item >= 500:
#         print('To place this order, insurance must be required!')
#         break
#     print(item)

# Mobile No. & Directory Example --> Search Operation (is it available or not)

# 2. continue --> skip current iteration and continue for the remaining

# # basic example
# for i in range(10):
#     if i == 5:
#         print('Loop Skipped!')
#         continue
#     print('order',end='')
#     print(' = ',end='')
#     print(i)

# # print only odd numbers between 1 and 20
# for i in range(1,20):
#     if i%2 == 0:
#         continue
#     print(i)

# # print table of n: (Although this code is expensive, still it's possible to do so.)
# n = int(input('Enter the number : '))
# for i in range(1,(n*10)+1):
#     if i%n != 0:
#         continue
#     print(i)

# # Cart Insurance Example with continue statement
# cart = [10,20,600,60,70]
# for item in cart:
#     if item >= 500:
#         print('We cannot process this itme without insurance : ',item)
#         continue
#     print(item)

# number = [10,20,0,5,0,30]
# for i in number:
#     if i == 0:
#         print('dividing with 0 leads to ZeroDivisionError!')
#         continue
#     # print('100/%d = %d' %(i,100/i))
#     print('100/{} = {}'.format(i,100/i))

# # else block
# # for-else
# # 1. for-else without break being executed.
# print('1. for-else without break being executed.')
# cart = [10,20,30,40,50]
# for item in cart:
#     if item >= 500:
#         print("We can't place this order")
#         break
#     print('Processing Item',item)
# else:
#     print('Congrates...! All your items processed successfully!')
# # 2. for-else with break being executed.
# print('2. for-else with break being executed.')
# cart = [10,20,30,700,40,50]
# for item in cart:
#     if item >= 500:
#         print("We can't place this order")
#         break
#     print('Processing Item',item)
# else:
#     print('Congrates...! All your items processed successfully!')
# # 3. for-loop withou break statement--> not much meaningful
# print('3. for-loop withou break statement')
# cart = [10,20,30,700,40,50]
# for item in cart:
#     if item >= 500:
#         print("We can't place this order")
#         continue
#     print('Processing Item',item)
# else:
#     print('Congrates...! All your items processed successfully!')

# pass Statement

# # basic example
# if 10>20:
#     print('Hello')
# else:
#     pass

# addItem(), removeItem() & updateItem() Example
def addItem():
    pass
def deleteItem():
    pass
def updateItem():
    pass

# class Loan example
class Loan:
    def getInterestRate(self):
        pass
class GoldLoan(Loan):
    def getInterestRate(self):
        return 10
class HomeLoan(Loan):
    def getInterestRate(self):
        return 7
class CarLoan(Loan):
    def getInterestRate(self):
        return 13

# # del statement

# # basic Example
# x = 10
# print(x)
# del x
# print(x)

# s1 = 'shubham'
# s2 = s1
# s3 = s1
# print(s1,s2,s3)
# del s1
# print('s2 =',s2)
# print('s3 =',s3)
# # print('s1 =',s1)
# del s2,s3
# # print(s2)
# # print(s3)
# s1 = None
# print(s1)

# # deleting an item of string object
# s = 'shubham'
# print(s[0])
# del s[0]
