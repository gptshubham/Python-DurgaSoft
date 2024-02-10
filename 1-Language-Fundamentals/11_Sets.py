# Sets
# --> Unordered ==> no indexing, no slicing, no iteration
# --> Duplicates are not allowed ==> Unique Elements
# --> Hetero Elements
# --> Mutable and Growable
# --> { }
#

# # Creation of Set Objects
# s = {10,'Sachin',7,'Dhoni',18,'Kohli',45,'Rohit'}
# print(s)     # order is not preserved
# # set() --> conversion into set
# # str --> set
# s = 'Hardik'
# s1 = set(s)
# print(s1)
# # List --> set
# L = [10,'Sachin',7,'Dhoni',18,'Kohli',45,'Rohit',True]
# s = set(L)
# print(s)
# # Tuple --> set
# t = ('Sachin','Dhoni','Kohli','Rohit')
# s = set(t)
# print(s)
# # Dict --> set
# d = {10:'Sachin',7:'Dhoni',18:'Kohli',45:'Rohit'}
# s = set(d)
# print(s)
# # Note: given any sequence , we can convert it to set using set()
#
# # Dynamic input --> eval()
# s = eval(input('Enter any set of elements : '))
# print(s)
# print(type(s))
#
# # empty set
# s = {}
# print(s,type(s))
# s = set()
# print(s,type(s))

# important Methods and Functions related to set

# # .add()
# s = {'Sachin','Dhoni'}
# print(s)
# s.add('Kohli')
# print(s)
# s.add('Kohli')
# print(s)         # Doesn't throw an error ! Simply Ignored
# # s.add([10,20,30])
# # print(s)       # ***** Surprise!

# # .update()
# s = set()
# s1 = {10,7,18,45}
# s2 = ('Sachin','Dhoni','Kohli','Rohit')
# s3 = ['Pandya','Gill','Jadeja']
# s.update(s1,s2,s3)
# print(s)
#
# # s = set()
# # s4 = ['Sachin','Dhoni',['Kohli','Rohit']]
# # s.update(s4)
# # print(s)        # ***** Surprise!
#
# s = set()
# s.update('Pandya')
# print(s)

# # removing elements from set
#
# # .pop()
# s = {10,'Sachin',7,'Dhoni',18,'Kohli',45,'Rohit',True}
# print(s.pop())
# print(s.pop())
#
# # How to handle KeyError while using pop()
# # s = set()   # empty set
# # print(s.pop())    # KeyError: 'pop from an empty set'
# s = set()
# if s:
#     print(s.pop())     # No KeyError
# s = {10,'Sachin',7,'Dhoni',18,'Kohli',45,'Rohit',True}
# while s:
#     print(s.pop())    # No KeyError
#
# # .remove()
# s = {10,20,30,40}
# removed = s.remove(10)
# print(s)
# print(removed)
# # How to Handle KeyError while using remove
# rm = int(input('Enter the value to remove from set : '))
# # print(s.remove(rm))      # KeyError: 100
# # 1. using membership operators
# if rm in s:
#     s.remove(rm)
#     print(s)
# else:
#     print('Invalid Key!')

# # 2. .discard()
# s.discard(20)
# print(s)
# s.discard(100)
# print(s)

# # .clear()
# s = {10,20,30,40}
# s.clear()
# print(s)

# # Aliasing vs Cloning
# s1 = {10,20,30,40}
# s2 = s1
# s3 = s1.copy()
# print(id(s1))
# print(id(s2))
# print(id(s3))

# # Mathematical Operations on Set
# s1 = {1,2,3,7}
# s2 = {1,3,4,5,6,8,9}
# # print(s1+s2)         # unsupported operand
# # print(s1*3)          # unsupported operand
#
# # .union() vs. |
# print(s1.union(s2))
# print(s1 | s2)
#
# # .intersection() vs. &
# print(s1.intersection(s2))
# print(s1 & s2)
#
# # .difference() vs. -
# print(s1.difference(s2))
# print(s1 - s2)
# print(s2.difference(s1))
# print(s2 - s1)
#
# # .symmetric_difference() vs. ^
# print(s1.symmetric_difference(s2))
# print(s1 ^ s2)

# # Membership Operators --> applicable

# # Set Comprehension
# s = {x**3 for x in range(5)}
# print(s)
# print(type(s))

# # identity vs. equality
# s1 = {1,2,3}
# s2 = {1,2,3}
# print(s1 is s2)
# s3 = s1
# print(s1 is s3)
# s4 = {3,2,1}
# print(s1 == s4)
# print(s2 == s4)
# print(s3 == s4)

# # write a program to delete duplicates present in the list
#
# L = eval(input('Enter a list : '))
# # ['dhoni','kohli','sachin','rohit','kohli','kohli','sachin']
# s = set(L)
# L = list(s)
# L.sort()
# print(L)
#
# # what if we want the same order as the original list
# L = eval(input('Enter a list : '))
# L1 = []
# for i in L:
#     if i not in L1:
#         L1.append(i)
# print(L1)

# # write a program to print different vowels
# # present in the given word
#
# # using set operations
# word = set(input('Enter any word : ').lower())   # YouTubeInstagramLinkedInTwitter
# vowels_list = {'a','e','i','o','u'}
# result = word & vowels_list
# print(result)
#
# # using list and loops
# word = input('Enter any word : ').lower()
# vowels_list = ['a','e','i','o','u']
# result = []
# for i in vowels_list:
#     if i in word:
#         result += [i]
# print(result)
