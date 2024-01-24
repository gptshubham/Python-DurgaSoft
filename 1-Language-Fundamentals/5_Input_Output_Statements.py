# # input()
# x = input('Enter some value : ')
# print(x,type(x))
# x = int(input('Enter some value : '))
# print(x,type(x))
# x = float(input('Enter some value : '))
# print(x,type(x))
#
# # write a program to read 2 numbers from the keyboard and print the sum
# num1 = int(input('Enter First Number : '))
# num2 = int(input('Enter Second Number : '))
# print('Sum =',num1 + num2)
# print('Sum =',int(input('Enter First Number : ')) + int(input('Enter Second Number : '))) # Not Recommended from readability point of view
#
# # write a program to read Employee Data from the keyboard and print that Data
# employeeNumber = int(input('Enter Employee Number : '))
# employeeName = input('Enter Name : ')
# employeeSalary = float(input('Enter Salary : '))
# employeeAddress = input('Enter Address : ')
# married = bool(input('Enter whether married or not? [True|False] : '))
# print('Please Confirm Your Information :',employeeName,employeeNumber,employeeSalary,married,employeeAddress,sep='\n')
#
# # Better Alternative of above code
# employeeNumber = eval(input('Enter Employee Number : '))
# employeeName = input('Enter Name : ')
# employeeSalary = eval(input('Enter Salary : '))
# employeeAddress = input('Enter Address : ')
# married = eval(input('Enter whether married or not? [True|False] : '))
# print('Please Confirm Your Information :',employeeName,employeeNumber,employeeSalary,married,employeeAddress,sep='\n')

# # eval()
# x = eval('10+20+30')
# print(x,type(x))
#
# result = float(input('Enter some expression : '))           # leads to ValueError
# print(result)
# result = eval(input('Enter some expression : '))
# print(result,type(result))
#
# # taking list as input form user
# L = eval(input('Enter some list : '))
# print(L,type(L))
# taking tuple as input form user
# t = eval(input('Enter some tuple : '))
# print(t,type(t))
# taking dictionary as input from user
# d = eval(input('Enter a dictionary'))
# print(d,type(d))

# List Comprehension
# # split()
# s = '10 20 30'
# l = s.split()                          # returns list of strings
# print(l)
#
# # unpacking (and assigning)
# a,b,c = [10,20,30]
# print(a,b,c)
#
# # string value to int type ===> int()
# # read multiple values from the keyboard in a single line and convert them into list of int values
# l0 = input('Enter Two Values : ').split()
# print(l0)
# a,b = l0
# print(a,type(a))
# print(b,type(b))
# l1 = []
# for i in l0:
#     l1.append(int(i))
# print(l1)
# a,b=l1
# print(a,type(a))
# print(b,type(b))
#
# # list comprehension - concise code of above problem statement
# a,b = [int(x) for x in input('Enter Two Numbers : ').split()]
# print(a,type(a))
# print(b,type(b))
#
# # read two int values from the keyboard in a single line and print the product.
# a,b = [int(x) for x in input('Enter Two Values : ').split()]
# print('The Product =',a*b)
# alternatively
# a,b = [int(x) for x in input('Enter Two Values : ').split(',')]
# print('The Product =',a*b)
#
# write a program to read 3 float numbers from the keyboard with , seperator and print their sum
# a,b,c = [float(x) for x in input('Enter Three Float Values seperated by , : ').split(',')]
# print('Sum =',a+b+c)

# Command Line Arguments
# from sys import argv
# print(type(argv))                  # List
# print('the number of command line arguments: ',len(argv))
# print('the list of command line arguments: ',argv)
# print('the first argument: ',argv[0])
# print('the second argument: ',argv[1])
#
# sum = 0
# for x in argv[1:]:
#     sum += int(x)
# print(sum)
#
# print(argv[1])

# # Output Statements
# # print()
#
# # Form 1: print()
# print('Shubham')
# print()
# print('Gupta')
#
# # Form 2: print('string')
# print('Shubham Kumar Gupta')
# print(len('Shubham Kumar Gupta'))
# print('Shubham\nKumar\nGupta')
# print(len('Shubham\nKumar\nGupta'))
# print('shubham'+'kumar'+'gupta')
# print('Shubham'* 5)
# print('Shubham'*3 + 'Kumar')
#
# # Form 3: print(object)
# print(10)
# print(10.5)
# print(True)
# print([10,20,30,40])
# print((10,20,30,40))
#
# # Form 4: sep attribute
# firstName = 'Shubham'
# secondName = 'Kumar'
# lastName = 'Gupta'
# print(firstName,secondName,lastName,sep='-')
# print(firstName,secondName,lastName,sep='*******')
# a,b,c = 10,20,30
# print(a,b,c,sep='*')
# print(a,b,c,sep='-')
#
# # Form 5: end attribute
# firstName = 'Shubham'
# secondName = 'Kumar'
# lastName = 'Gupta'
# print(firstName,end='')
# print(secondName,end='')
# print(lastName)
# print(firstName,end='-')
# print(secondName,end='-')
# print(lastName)
# print(firstName,end='*')
# print(secondName,end='*')
# print(lastName)
# print(firstName,end='-')
# print(secondName,end='*')
# print(lastName)
# a,b,c = 10,20,30
# print(a,b,c,end='****')
# print()
# print(a,b,c,sep='*',end='###')
# # print('shubham')
#
# # Form 6: print(formatted string)                     # learned something new here
# a = 10
# b = 20
# c = 30
# print("a's value is %i" %a)
# print("a's value is %d" %a)
# print("b's value is %d and c's value is %d" %(b,c))
# f = 2.333333333333333333333333333
# print("f's value is %f" %f)
# user = 'shubham'
# print('my name is %s' %user)
# l = [10,20,30,40]
# print('Hello %s...The list items are %s' %(user,l))
#
# Form 7: print() with {}
# {} --> replacement operator
user = 'shubham'
age = 22
gender = 'male'
print('My name is {} . I am a {} years old {}.'.format(user,age,gender))
# order of arguments is important
print('My name is {} . I am a {} years old {}.'.format(gender,age,user))
print('My name is {2} . I am a {1} years old {0}.'.format(gender,age,user))
# order of arguments is important
print('My name is {0} . I am a {1} years old {2}.'.format(gender,age,user))
print('My name is {x} . I am a {y} years old {z}.'.format(x=user,y=age,z=gender))
# order of arguments is not important
print('My name is {x} . I am a {y} years old {z}.'.format(z=gender,y=age,x=user))
