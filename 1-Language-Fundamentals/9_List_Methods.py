# # creating list with Dynamic Input
# L = input('Enter a List : ')            # [10,20,30,40]
# print(type(L))                          # str
from copy import copy

# L = list(input('Enter a List : '))      # [10,20,30,40]
# print(L)     # ['[', '1', '0', ',', '2', '0', ',', '3', '0', ',', '4', '0', ']']
# print(type(L))                          # <class 'list'>

# # eval()
# L = eval(input('Enter a List : '))      # [10,20,30,40]
# print(type(L))                          # <class 'list'>

# # Empty List
# L = []
# print(L,type(L))

# list() --> conversion into list

# # range --> list
# L = list(range(10,41,10))
# print(L,type(L))                # [10,20,30,40] <class 'list'>
#
# # string --> list
# user = 'shubham gupta'
# print(user,type(user))          # shubham gupta <class 'str'>
# L = list(user.replace(' ',''))
# print(L)                        # ['s', 'h', 'u', 'b', 'h', 'a', 'm', 'g', 'u', 'p', 't', 'a']
# print(type(L))                  # <class 'list'>
#
# # string class split() method
# user = 'shubham gupta'
# print(user,type(user))          # shubham gupta <class 'str'>
# L = user.split()
# print(L,type(L))                # ['shubham', 'gupta'] <class 'list'>
#
# # Tuple --> List
# t = (10,20,30,40)
# print(t,type(t))                # (10, 20, 30, 40) <class 'tuple'>
# L = list(t)
# print(L,type(L))                # [10, 20, 30, 40] <class 'list'>
#
# # set --> list
# s = {10,20,30,40}
# print(s,type(s))                # {40, 10, 20, 30} <class 'set'>
# L = list(s)
# print(L,type(L))                # [40, 10, 20, 30] <class 'list'>
# L = sorted(list(s))
# print(L,type(L))                # [10, 20, 30, 40] <class 'list'>

# # dict --> list
# d = {"firstName" : 'shubham' , "middleName" : 'kumar' , "lastname" : 'gupta'}
# L = list(d)
# print(L,type(L))                # ***** Surprise
# # ['firstName', 'middleName', 'lastname'] <class 'list'>

# # Accessing List Elements
# L = [10,20,30,40,50,60,70,80,90]
# # print(L[100])                 # IndexError
# print(L[2:5])                   # [30, 40, 50]

# # list vs. mutability
# L = [10,20,30,40]
# L[0] = 7777
# print(L)

# # Traversal
# # using for loop
# L = [10,20,30,40]
# for i in L:
#     print(i)
# # using while loop
# L = [10,20,30,40]
# i = 0
# while i<len(L):
#     print(L[i])
#     i += 1
# # print noly the even elements of list
# L = [7,16,9,12,19,17,22,28]
# for i in L:
#     if i%2 == 0:
#         print(i)


# List Functions

# # len()
# L = [10,20,30,40]
# print(len(L))

# # count()
# L = [10,20,10,20,30,10,20,40,20]
# print(L.count(10))
# print(L.count(40))
# print(L.count(400))

# # index()
# L = [10,20,10,20,30,10,20,40,20]
# print(L.index(10))
# print(L.index(20))
# print(L.index(40))
# # print(L.index(400))           # ValueError
# # how to avoid ValueError
# L = [10,20,10,20,30,10,20,40,20]
# value = int(input('Enter the Element to Find : '))
# if value in L:
#     print(L.index(value))
# else:
#     print('Value not available!')

# # append()
# # write code to add elements to the list upto 100 which are divisible by 10
# L = []
# for i in range(10,101):
#     if i%10 == 0:
#         L.append(i)
# print(L)

# # insert()
# user = 'shubham gupta'
# print(user)
# middleName = 'kumar'
# L = user.split()
# L.insert(1,middleName)
# user = ' '.join(L)
# print(user)

# # no IndexError in case of insert()
# L = [10,20,30,40]
# L.insert(100,7777)
# print(L)                                   # ***** Surprise
# L.insert(-100,6666)
# print(L)                                   # ***** Surprise

# # extend()
# L1 = ['chicken','mutton','fish']
# L2 = ['KF','RC','FO']
# L3 = L1.extend(L2)
# print(L1)
# print(L3)                                  # ***** Surprise
# L2.extend(L1)
# print(L2)
# # Note: extend() changes the original list and returns None as output, hence
# # we cannot store ['chicken', 'mutton', 'fish', 'KF', 'RC', 'FO'] in a new variable
# # However, if we don't  want to change the original list and store the result
# # in a new variable L2 then we can just use + operator
# L1 = ['chicken','mutton','fish']
# L2 = ['KF','RC','FO']
# L3 = L1 + L2
# print(L3)

# # remove()
# L1 = ['chicken','mutton','fish']
# L2 = L1.remove('fish')
# print(L1)
# print(L2)
# # Note: remove() changes the original list and returns None as output hence
# # we cannot store ['chicken', 'mutton'] in a new variable
# # However, if we don't  want to change the original list and store the result
# # in a new variable L2 then we can just use copy()
# L1 = ['chicken','mutton','fish']
# L2 = copy(L1)
# L2.remove('fish')
# print(L1)
# print(L2)

# # How to avoid ValueError if item is not present in list
# L1 = ['chicken','mutton','fish']
# remove_item = input('Enter the item to remove : ')
# if remove_item in L1:
#     L1.remove(remove_item)
# else:
#     print('%s is not available!' % remove_item)
# print(L1)

# # removing an element which is available multiple times
# L1 = ['KF','KF','RC','KF','KF','FO','KF']
# remove_item = input('Enter the item to remove : ')
# while True:
#     if remove_item in L1:
#         L1.remove(remove_item)
#     else:
#         break
# print(L1)

# # pop()
# L1 = [420,9211,'AK47','AK203','Donald Trump','Joe Biden']
# pop_item = L1.pop()
# print('item popped out :',pop_item)
# print(L1)
#
# # IndexError
# L1 = []
# # pop_item = L1.pop()
# # How to avoid IndexError
# if L1:
#     new_pop_item = L1.pop()
#     print(new_pop_item)
# print(L1)
# # Alternatively: using len()
# if len(L1) != 0:
#     new_pop_item = L1.pop()
#     print(new_pop_item)
# print(L1)
#
# # Another case of IndexError --> index out of range
# # and how to avoid such error
# L1 = [420,9211,'AK47','AK203','Donald Trump','Joe Biden']
# pop_item_index = int(input('Enter the index to pop : '))
# if pop_item_index > len(L1)-1:
#     print('Input out of Range!')
# else:
#     popped_item = L1.pop(pop_item_index)
#     print('item popped :',popped_item)
#     print(L1)
#
# # popping items in the forward direction
# L1 = [9211,'AK47','AK203','Donald Trump','Joe Biden']
# i = 0
# n = len(L1)
# while i<n:
#     # print('Current Index Value :',i)
#     # print('Current n value :',n)
#     print('Popped Element :',L1.pop(i))
#     if len(L1) == 0:
#         break
# print(L1)
#
# # alternatively: (I prefer this one --> concise code)
# L1 = [9211,'AK47','AK203','Donald Trump','Joe Biden']
# i = 0
# while L1:
#     print('Popped Element :', L1.pop(i))
# print(L1)
#
# # # popping items in the backward direction
# L1 = [9211,'AK47','AK203','Donald Trump','Joe Biden']
# i = -1
# while L1:
#     print('Popped Element :', L1.pop(i))
# print(L1)

# # clear()
# L1 = [9211,'AK47','AK203','Donald Trump','Joe Biden']
# L1.clear()
# print(L1)

# # reverse()
# L1 = [9211,'AK47','AK203','Donald Trump','Joe Biden']
# print(L1)
# L1.reverse()
# print(L1)

# # sort() --> ascending order / alphabetical order
# L1 = [40,20,30,10,50,40]
# print(L1)
# L1.sort()
# print(L1)

# L1 = ['salman','khan','akshay','kumar']
# print(L1)
# L1.sort()
# print(L1)

# # TypeError
# L1 = [40,20,30,'salman','khan']
# L1.sort()
# print(L1)

# # sorting elements in reverse order --> descending order / reversed alphabetical order
# L1 = [40,20,30,10,50,40]
# L1.sort(reverse=True)
# print(L1)

# # Aliasing vs. Cloning
#
# # Aliasing --> creating duplicate reference variable
# L1 = [10,20,30,40]
# L2 = L1
# print(L1,id(L1))
# print(L2,id(L2))
# # Problem --> changing one affects the other
# L1[0] = 7777
# print('L1 :',L1)
# print('L2 :',L2)
# L2[1] = 8888
# print('L1 :',L1)
# print('L2 :',L2)
#
# # cloning --> creating duplicate list object
# # 1. using [:]
# L1 = [10,20,30,40]
# L2 = L1[:]
# print(L1,id(L1))
# print(L2,id(L2))
# L1[1] = 7777
# print(L1)
# print(L2)
# # 2. copy() --> preferred
# L1 = [10,20,30,40,50]
# L3 = L1.copy()
# print(L1,id(L1))
# print(L3,id(L3))
# L1[1] = 7777
# print(L1)
# print(L3)

# # Deep Copy & Shallow Copy --> Discussed in Next Level
# # Note : L.copy() creates a Shallow Copy

# # Mathematical Operators for List Object

# # + operator ( Concatenation )
# L1 = [10,20,30]
# L2 = [70,80,90]
# L3 = L1 + L2
# print(L3)
# L4 = L1 + [40]
# print(L1)
# print(L4)
# # Note: Difference between + operator and extend()
# s = 'Dhoni'
# L1.extend(s)
# ages = (22,23,24)
# L2.extend(ages)
# print(L2)
# ages = {22,23,24}
# L3.extend(ages)
# print(L3)

# # * operator ( Repetition )
# L1 = [10,20,30]
# L2 = L1 * 2
# print(L2)

# eqality operators

# # == , !=
# L1 = [10,20,30]
# L2 = [10,20,30]
# print(L1 == L2)
# L1 = ['Dhoni','Kohli','Rohit']
# L2 = ['Dhoni','Kohli','Rohit']
# L3 = ['dhoni','kohli','rohit']
# print(L1 == L2)
# print(L1 == L3)
# print(L1 != L3)

# # Relational Operators ( Comparison )
# # Note: not used frequently with List Objects,
# # can be used to compare elements
# x = [100,10,5]
# y = [10,20,30,40,50,60]
# print(x>y)
# print(x>=y)
# print(x<y)
# print(x<=y)
# x = [100,10,5]
# y = [100,20,30,40,50,60]
# print(x>y)
# print(x>=y)
# print(x<y)
# print(x<=y)

# # Membership Operators
# L1 = ['Dhoni','Kohli','Rohit']
# print('Dhoni' in L1)
# print('dhoni' in L1)
# print('Dhoni' not in L1)
# print('dhoni' not in L1)
# print('sikhar' in L1)
# print('sikhar' not in L1)

# # Identity Operaors --> memory address comparison is done
# L1 = ['Dhoni','Kohli','Rohit']
# L2 = L1
# print(L1 is L2)
# L3 = ['Dhoni','Kohli','Rohit']
# print(L1 is L3)
# print(L1 is not L3)

# # Nested List
# L = [10,20,[30,40]]
# print(L)
# print(L[0])
# print(L[1])
# print(L[2])
# print(L[2][0])
# print(L[2][1])

# # Nested List as Matrix
# L = [[10,20,30],[40,50,60],[70,80,90]]
# print('Elements by Row-wise :')
# for row in L:
#     print(row)
# print('Elements in Matrix Style :')
# for row in L:
#     for element in row:
#         print(element,end=' ')
#     print()
# # accessing elements of matrix using index
# print('Elements in Matrix Style using index :')
# L = [[10,20,30],[40,50,60],[70,80,90]]
# for i in range(len(L)):
#     for j in range(len(L[i])):
#         print(L[i][j],end=' ')
#     print()

# # List Comprehension

# # even numbers between 1 and 10 (inclusive)
# L = [x for x in range(1,11) if x%2 == 0]
# print(L)

# # square of even numbers between 1 and 10 (inclusive)
# L = [x**2 for x in range(1,11) if x%2 == 0]
# print(L)

# # 2^n of natural numbers upto 10
# L = [2**x for x in range(1,11)]
# print(L)

# # create a list from words list containing only
# # the first letters of the words in the words list
# words = ['dhoni','kohli','rohit','hardik']
# L = [item[0] for item in words]
# print(L)

# num1 = [10,20,30,40]
# num2 = [30,40,50,60]
# # create a list with numbers which are present in num1
# # but not in num2
# num3 = [x for x in num1 if x not in num2]
# print(num3)
# # create a list with common numbers present in both lists
# num4 = [x for x in num1 if x in num2]
# print(num4)

# # Nested List using List Comprehension
# s = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
# words = s.split()
# print(words)
# L = [[word.title(),len(word)] for word in words]
# print(L)

# # write a program to display unique vowels present in the given word
# vowels = ['a','e','i','o','u']
# word = input('Enter any word : ').lower()
# unique_vowels_in_word = [x for x in vowels if x in word]
# print(unique_vowels_in_word)

