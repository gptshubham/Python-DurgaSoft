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
