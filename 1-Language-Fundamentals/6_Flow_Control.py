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
#     print('character at %d index =' % i,char)                # we can use %i as well instead of %d
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

# print numbers from 10 to 1 (descending order)
for i in range(10,0,-1):
    print(i)