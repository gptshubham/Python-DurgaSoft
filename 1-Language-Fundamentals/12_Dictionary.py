# # Dictionary
# d = {10:'Sachin',7:'Dhoni',18:'Kohli'}
# print(d)

# # Accessing Values of Dictionary
# d = {10:'Sachin',7:'Dhoni',18:'Kohli'}
#
# # 1. using keys
# print(d[10])
# print(d[7])
# print(d[18])
# # print(d[100])     # KeyError: 100
# # Handling KeyError --> using membership operator
# key_to_search = int(input('Enter the key to access : '))
# if key_to_search in d:
#     print(d[key_to_search])
# else:
#     print('Invalid Key!')
# # # Handling KeyError --> using .get(key) method
# print(d.get(key_to_search))
#
# # 2. using loops with in operator
# # --> ultimately we are using the key only to access the data
# for i in d:
#     print(i,end=' ')
#     print(d[i])

# # updating values of Dictionary
# d = {10:'Sachin',7:'Dhoni',18:'Kohli'}
#
# for i in d:
#     d[i] = d[i].upper()
#
# for i in d:
#     print(i,end=' ')
#     print(d[i])

# # Creating Dictionary
#
# # Empty Dictionary
# d = {}
# print(d,type(d))
# d = dict()
# print(d,type(d))
#
# # adding key value to the dictionary
# # if data is known at the time of creation
# d['firstName'] = 'shubham'
# d['middleName'] = 'kumar'
# d['lastName'] = 'gupta'
# print(d)
# d['firstName'] = 'abhi'
# print(d)
#
# # if value is not known at the time of creation
# d = {}

# # write a program to enter name and marks in the dictionaty and display information on the screen
# marks_dict = {}
# while True:
#     name = input("Enter Student's Name : ")
#     marks = int(input('Enter Marks : '))
#     marks_dict[name] = marks
#     print('Insertion Successful!')
#     option = input('More Students ? [y|n] : ')
#     while option.lower() not in ('y','n'):
#             option = input('Invalid Option! Please Select a Valid Option [y|n] : ')
#     if option.lower() == 'n':
#         break
# # print(marks_dict)
# print('Name\t\tMarks')
# print('#'*17)
# for i in marks_dict:
#     print('{}\t\t{}'.format(i,marks_dict[i]))
# print('#'*17)

# # How to remove a particular entry from dictionary
# d = {1:'India',2:'Nepal',3:'Bhutan',4:'Afghanistan',5:'Myanmar',6:'Bangladesh',7:'Sri Lanka',8:'Maldives',9:'China',
#      10:'Pakistan'}
# del d[10]
# print(d)
# del d[8]
# print(d)
# del d[9]
# print(d)
# # del d[100]
# # print(d)       # KeyError: 100
# # use membership operator to handle KeyError
# removed = int(input('Enter the Key to Remove : '))
# if removed in d:
#     del d[removed]
# else:
#     print('Invalid Key!')

# # clear()
# d = {1:'India',2:'Nepal',3:'Bhutan',4:'Afghanistan',5:'Myanmar',6:'Bangladesh',7:'Sri Lanka'}
# d.clear()
# print(d)

# # del
# d = {1:'India',2:'Nepal',3:'Bhutan',4:'Afghanistan',5:'Myanmar',6:'Bangladesh',7:'Sri Lanka'}
# del d
# print(d)      # NameError: name 'd' is not defined.

# # Important Functions and Methods related to Dictionary

# # dict() --> convert into dict data type
#
# # Note:
# # The elements of the collection must be pairs
#
# # List_of_Tuple_of_Pairs --> Dict
# L = [(10,'Sachin'),(7,'Dhoni'),(18,'Kohli')]
# print(L)
# d1 = dict(L)
# print(d1)
#
# # Nested_List --> Dict
# nested_L = [[10,'Sachin'],[7,'Dhoni'],[18,'Kohli']]
# print(nested_L)
# d2 = dict(nested_L)
# print(d2)
#
# # Nested_Tuple --> Dict
# t = ((10,'Sachin'),(7,'Dhoni'),(18,'Kohli'))
# print(t)
# d2 = dict(t)
# print(d2)
#
# # Set_of_Tuple_of_Pairs --> Dict
# s = {(10,'Sachin'),(7,'Dhoni'),(18,'Kohli')}
# print(s)
# d3 = dict(s)
# print(d3)
#
# # s = "(1,'Shubham'),(2,'Kumar'),(3,'Gupta')"
# # print(s)
# # d4 = dict(s)
# # print(d4)     # ValueError

# # len()
# d = {10:'Sachin',7:'Dhoni',18:'Kohli'}
# print(len(d))

# # .get(key)
# d = {10:'Sachin',7:'Dhoni',18:'Kohli'}
# print(d.get(7))
# print(d.get(45))
# print(d.get(45,'Key not Available!'))

# # .pop()
# d = {1:'India',2:'Nepal',3:'Bhutan',4:'Afghanistan',5:'Myanmar',6:'Bangladesh',7:'Sri Lanka',8:'Maldives',9:'China',10:'Pakistan'}
# popped = d.pop(9)
# print('Popped :',popped)
# # popped = d.pop(100)   # KeyError: 100
# popped = d.pop(10)
# print('Popped :',popped)
# print(d)

# # .popitem()
# d = {1:'India',2:'Nepal',3:'Bhutan',4:'Afghanistan',5:'Myanmar',6:'Bangladesh',7:'Sri Lanka',8:'Maldives',9:'China',10:'Pakistan'}
# popped = d.popitem()
# print('Popped Item :',popped)
#
# # d = {}
# # popped = d.popitem()
# # print(popped)    # KeyError: 'popitem(): dictionary is empty'
#
# # basic example
# d = {}
# i = 0
# while i<10:
#     d[chr(65+i)] = 100 + 10*i
#     i += 1
# print(d)
#
# while len(d) != 0:
#     print('Processing Item:',d.popitem())

# # .keys()
# d = {10:'Sachin',7:'Dhoni',18:'Kohli',45:'Rohit'}
# k = d.keys()
# print(k)
# # iteration --> dict_keys
# for key in k:
#     print(key,end=' ')
# print()

# # .values()
# d = {10:'Sachin',7:'Dhoni',18:'Kohli',45:'Rohit'}
# v = d.values()
# print(v)
# # iteration --> dict_values
# for value in v:
#     print(value,end=' ')
# print()
# # Duplicate Values --> allowed
# d = {100:'Dhoni',200:'Dhoni',300:'Dhoni'}
# print(d.values())

# # .items()
# d = {10:'Sachin',7:'Dhoni',18:'Kohli',45:'Rohit'}
# d_elements = d.items()
# print(d_elements)
# # iteration --> dict_items
# for item in d_elements:
#     print(item)
# # iteration and String formatting
# for k,v in d.items():
#     print('{}:{}'.format(k,v))

# # .setdefault()
# d = {10:'Sachin',7:'Dhoni',18:'Kohli',45:'Rohit'}
# print(d.setdefault(63,'SKY'))
# print(d)

# # .update()
# d1 = {10:'Sachin',7:'Dhoni'}
# print(d1)
# d2 = {18:'Kohli',45:'Rohit'}
# print(d2)
# d1.update(d2)
# print(d1)

# # aliasing vs. cloning
# d1 = {10:'Sachin',7:'Dhoni'}
# # aliasing
# d2 = d1
# # cloning
# d3 = d1.copy()
# print(id(d1))
# print(id(d2))
# print(id(d3))
# print(d1 is d2)
# print(d1 is d3)

# # Program 1: write a program to take dictionary from
# # keyboard and print the sum of values
#
# # using loops
# d = eval(input('Enter a Dictionary : '))  # {'A':100,'B':200,'C':300,'D':400}
# total = 0
# for v in d.values():
#     total += v
# print('Sum :',total)
#
# # without loop
# d1 = eval(input('Enter a Dictionary : '))
# print('Sum :',sum(d1.values()))

# # Program 2: WAP to find number of occurrences
# # of each letter present in the given string
#
# # Approach 1: using if-else
# print('Program 2: Approach 1')
# s = 'shubhamgupta'
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# # print(d)
# for k,v in sorted(d.items()):
#     print('{} : {}'.format(k,v))
#
# # Approach 2: using .get()
# print('Program 2: Approach 2')
# s = 'shubhamgupta'
# new_d = {}
# for i in s:
#     new_d[i] = new_d.get(i,0) + 1
# # print(new_d)
# for k,v in sorted(new_d.items()):
#     print('{} : {}'.format(k,v))

# # Program 3: WAP to find the number of occurrences
# # of each vowels present in the given string
# print('Program 3')
# s = 'shubhamkumargupta'
# vowels = ['a','e','i','o','u']
# d = {}
# for i in s:
#     if i in vowels:
#         d[i] = d.get(i,0) + 1
#
# print(d)

# Program : write a program to accept student name and marks
# from the keyboard and with that data create a dictionary and
# also display student marks by taking student name as input

# # creation of dictionary
# marks = {}
# while True:
#     key = input('Enter Student Name : ')
#     value = int(input('Enter Student Marks : '))
#     marks[key] = value
#     option = input('More Student? [y|n] : ').lower()
#     while option not in ('y', 'n'):
#         print('Invalid Input!')
#         option = input('More Student? [y|n] : ').lower()
#         if option == 'n':
#             break
#     if option == 'n':
#         break
# print('Name\t\tMarks')
# print('#'*17)
# for key in marks:
#     print('{}\t\t{}'.format(key,marks[key]))
# print('#'*17)
#
# # display of name
# while True:
#     name = input('Enter Student Name : ')
#     if name in marks:
#         print("Marks of {} : {}".format(name,marks[name]))
#     else:
#         print('Student Not Found!')
#     option = input('Check Again? [y|n] : ').lower()
#     while option not in ('y','n'):
#         option = input('Invalid Input! Please Select Valid Input [y|n] : ')
#     if option == 'n':
#         break

# # Dictionary Comprehension
#
# # squares Example
# squares = {x:x**2 for x in range(1, 6)}
# print(squares)
# print(type(squares))
#
# # dubles Example
# dubles = {x:x*2 for x in range(1,6)}
# print(dubles)
# print(type(dubles))
#
# # alphabets Example
# alphabets = {x:chr(64 + x) for x in range(1, 27)}
# print(alphabets)
# print(type(alphabets))

# Merging of Collections

# # List
# L1 = [10,20,30]
# L2 = [70,80,90]
# L3 = L1 + L2
# print(L3)
# # Alternatively using *
# L4 = [*L1,*L2]
# print(L4)
# # Merging lists to create set
# s = {*L1,*L2}
# print(s)
# # Merging lists to create tuple
# t = (*L1,*L2)
# print(t)

# # Tuple
# t1 = ('dhoni','kohli')
# t2 = ('sachin','rohit')
# t3 = t1 + t2
# print(t3)
# # Alternatively using *
# t4 = (*t1,*t2)
# print(t4)
# # Merging tuples to crate List
# l = [*t1,*t2]
# print(l)
# # Merging tuples to create set
# s = {*t1,*t2}
# print(s)

# # Set
# s1 = {'hardik','sky'}
# s2 = {'gill','rahul'}
# # s3 = s1 + s2
# # print(s3)        # TypeError: unsupported operand
# # using *
# s4 = {*s1,*s2}
# print(s4)
# # Merging sets to create list
# l = [*s1,*s2]
# # Merging sets to create tuple
# print(l)
# t = (*s1,*s2)
# print(t)

# # Merging lists,tuples and sets to create List
# L = [*L4,*t4,*s4]
# print(L)
# # Merging lists,tuples and sets to create tuple
# T = (*L4,*t4,*s4)
# print(T)
# # Merging lists,tuples and sets to create set
# S = {*L4,*t4,*s4}
# print(S)
#
# # Merging of Dictionaries
# d1 = {7:'Dhoni',18:'Kohli'}
# d2 = {10:'Sachin',45:'Rohit'}
# d3 = {1:'KL',8:'Jadeja'}
# d4 = {**d1,**d2,**d3}
# print(d4)

# # Nested Collections
#
# # Example 1: display 1.20, 2.60
# L1 = [(10,20,30),(40,55,60)]
# print(L1[0][1])
# print(L1[1][-1])
#
# # Example 2: display 1.BMW, 2.all mobile brand names
# d = {
#     'cars':('Mercedes','BMW','Lanborghini'),
#     'mobiles':('Apple','Samsung','Nothing')
# }
# # display second car
# print(d['cars'][1])
# for mobile in d.get('mobiles'):
#     print(mobile)