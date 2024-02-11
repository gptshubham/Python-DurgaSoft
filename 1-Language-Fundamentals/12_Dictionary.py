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
