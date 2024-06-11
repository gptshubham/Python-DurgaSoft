# Conditional / Selection Statements

# Program -> write a program to find greatest of 2 given numbers
'''
num1 = int(input('Enter First Number : '))
num2 = int(input('Enter Second Number : '))
result = num1 if num1>num2 else num2
print(f'The Greatest of {num1} and {num2} is {result}')
'''

# Program -> write a program to find greatest of 3 given numbers
'''
num1 = int(input('Enter First Number : '))
num2 = int(input('Enter Second Number : '))
num3 = int(input('Enter Third Number : '))
result = num1 if num1>num2>num3 else num2 if num2>num3 else num3
print(f'The greatest of {num1} , {num2} and {num3} is {result}')
'''

# Program -> write a program to find smallest of 2 given numbers
'''
num1 = int(input('Enter First Number : '))
num2 = int(input('Enter Second Number : '))
result = num1 if num1<num2 else num2
print(f'The Smallest of {num1} and {num2} is {result}')
'''

# Program -> write a program to find smallest of 3 given numbers
'''
num1 = int(input('Enter First Number : '))
num2 = int(input('Enter Second Number : '))
num3 = int(input('Enter Third Number : '))
result = num1 if num1<num2<num3 else num2 if num2<num3 else num3
print(f'The Smallest of {num1} , {num2} and {num3} is {result}')
'''

# write a program to check whether the given number is even or odd
'''
num = int(input("Enter the Number : "))
if num>0:
    result = "Even" if num % 2 == 0 else "Odd"
    print(f'{num} is {result}')
else:
    print("Invalid Input !")
'''

# write a program to check whether a given number is between 1 and 100 (inclusive)?
'''
num = int(input("Enter the Number : "))
if num > 100 or num < 1:
    print(f'{num} is out of range !')
else:
    print(f'{num} is within the range !')
'''

# Iterative Statements (Loops)

# 1. for loop

# print characters present in the given string
'''
name = input("Enter your name : ")
for i in name:
    print(i)
'''

# print characters present in the given string index-wise
'''
name = input("Enter your name : ")
for i in range(0,len(name)):
    print(i,' : ',name[i])
'''

# print number from 0 to 10
'''
for i in range(11):
    print(i)
'''

# print odd number from 0 to 20
'''
for i in range(21):
    if i%2 == 1:
        print(i)
'''

# print numbers from 10 to 1 (descending order)
'''
for i in range(10,0,-1):
    print(i)
'''

# print sum of numbers present in a given list
'''
L = eval(input("Enter a List of Numbers : "))
sum = 0
for i in L:
    sum += i
print(sum)

# Alternatively
L = []
sum = 0
for i in range(4):
    n = int(input("Enter a Number : "))
    L.append(n)
    sum += n

print(f'sum = {sum}')
print(L)
'''

# print numbers from 1 to 10 using while loop
'''
i = 1
while i < 11:
    print(i)
    i += 1
'''

# print the sum of first n natural numbers
'''
n = int(input('Enter the value of n : '))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)
'''

# write a program to prompt user to enter your favourite player
'''
fav_player = input("Enter the name of your favourite player : ")
while fav_player.lower() != 'dhoni':
    fav_player = input("Enter the name of your favourite player : ")
print(f'Your favourite player is {fav_player}')
'''

# Username Password Program
'''
user = "shubham"
passwd = 'gupta101'
username = input("Enter the Username : ")
password = input("Enter the password : ")
if username == user and password == passwd:
    print("Welcome!")
else:
    while user != username.lower() or passwd != password.lower():
        print("Incorrect Username or Password Please Retry!")
        username = input("Enter the Username : ")
        password = input("Enter the password : ")
    print("Welcome!")
'''

# nested loops
'''
count = 0
for i in range(5):
    for j in range(5):
        print(i,j)
        count += 1

print(f'Total Number of Iterations = {count}')
'''

# Transfer Statements

# Qsn: Which Loop will break in case of following Programs:
'''
for i in range(10):
    for j in range(10):
        if j == 5:
            print('Loop Completed!')
            break
        print(i,j)
'''
'''
for i in range(10):
    for j in range(10):
        if i == 5:
            print('Loop Skipped!')
            break
        print(i,j)
'''

# continue
# basic example
'''
for i in range(10):
    if i == 5:
        print('Loop Skipped!')
        continue
    print('order',end='')
    print(' = ',end='')
    print(i)
'''

# print only odd numbers between 1 and 20
'''
for num in range(1,20):
    if num % 2 == 0: continue
    print(num)
'''

# print table of n: (Although this code is expensive, still it's possible to do so.)
'''
n = int(input('Enter the Number: '))
for num in range(1, (n*10) + 1):
    if num % n != 0: continue
    print(num)
'''

# Program : skipping ZeroDivisionError
'''
numbers = [10, 20, 0, 5, 0, 30]
for number in numbers:
    if number == 0:
        print('dividing with zero leads to ZeroDivisionError!')
        continue
    else:
        print('100/%d = %d' %(number, 100/number))
        # this statement converts values into int resulting in data loss
        # i,e; less precision and accuracy
print('------------X-------------')
'''
# Alternatively : using try/except
'''
numbers = [10, 20, 0, 5, 0, 30]
for number in numbers:
    try:
        print('100/{} = {}'.format(number, 100/number))
    except:
        print('dividing with zero leads to ZeroDivisionError!')
'''

# 1. for-else without break being executed.
'''
print('1. for-else without break being executed.')
cart = [10, 20, 30, 40, 50]
for item in cart:
    if item >= 500:
        print("We can't place this order without insurance!")
        break
    print('Processing Item', item)
else:
    print('Congrats...! All your items processed successfully!')
'''

# 2. for-else with break being executed.
'''
print('2. for-else with break being executed.')
cart = [10,20,30,700,40,50]
for item in cart:
    if item >= 500:
        print("We can't place this order without insurance!")
        break
    print('Processing Item',item)
else:
    print('Congrats...! All your items processed successfully!')
'''

# del
'''
s1 = 'shubham'
s2 = s1
s3 = s1
print(s1,s2,s3)
del s1
print('s2 =',s2)
print('s3 =',s3)
# print('s1 =',s1)
del s2,s3
# print(s2)
# print(s3)
s1 = None
print(s1)

# deleting an item of string object
s = 'shubham'
print(s[0])
# del s[0]
'''