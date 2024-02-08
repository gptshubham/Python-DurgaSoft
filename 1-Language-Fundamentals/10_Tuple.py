# # Tuple
# t = (7,'Dhoni',18,'Kohli')
# print(t,type(t))
# print(id(t))
# t1 = t
# print(t1,type(t1))
# print(id(t1))

# # () are optional in Tuple
# t = 45,'Rohit',77,'Gill'
# print(t,type(t))                    # ***** Surprise

# # Empty Tuple
# t = ()
# print(t,type(t))

# # Single Valued Tuple
# t = (20)
# print(t,type(t))                   # ***** Surprise
# t = ('Dhoni')
# print(t,type(t))
# t = (20,)
# print(t,type(t))
# t = 20,
# print(t,type(t))

# # immutable
# # t1[0] = 7777
# # print(t1)
# # # TypeError: 'tuple' object does not support item assignment

# # ordered --> indexing and slicing, iterable
# # hetero objects
# # duplicate values
# t = (7,'Dhoni',18,'Kohli',45,'Rohit',77,'Gill',7,'Dhoni')
# print(t[0],t[1])
# print(t[2:6])
# print(t[-2],t[-1])

# # iterable
# for i in t:
#     print(i,end=' ')
# print()

# i = len(t) -1
# while i>=0:
#     print(t[i],end=' ')
#     i -= 1

# # tuple()
# L = [7,'Dhoni',18,'Kohli',45,'Rohit',77,'Gill',7,'Dhoni']
# print(L)
# print(type(L))
# t = tuple(L)
# print(t)
# print(type(t))

# # Dynamic Input
# # eval()
# t = eval(input('Enter a Tuple : '))
# print(t)
# print(type(t))

# # List vs. Tuple
# # memory consumption
# L = [7,'Dhoni',18,'Kohli',45,'Rohit',77,'Gill',7,'Dhoni']
# t = (7,'Dhoni',18,'Kohli',45,'Rohit',77,'Gill',7,'Dhoni')
# import sys
# print(sys.getsizeof(L))
# print(sys.getsizeof(t))
#
# # tuple as key in a dictionary
# d = {}
# t = (7,7,7)
# d[t] = 'Dhoni'
# print(d)
#
# # list as key in a dictionary
# d = {}
# t = [7,7,7]
# d[t] = 'Dhoni'
# print(d)        # TypeError: unhashable type: 'list'

# # mathematical operators for tuple
# # + , *
# t1= (7,'Dhoni',18,'Kohli')
# t2 = (45,'Rohit',77,'Gill')
# t3 = t1 + t2
# print(t3)
# print(t1*3)

# # Tuple Methods and Functions
# t1= (7,'Dhoni',18,'Kohli',45,'Rohit',77,'Gill',7,'Dhoni')
# # len()
# print(len(t1))

# # count()
# print(t1.count('Dhoni'))

# # index()
# print(t1.index('Rohit'))

# # sort() vs. sorted()
# # print(t1.sort())
# t1= (7,18,45,77,7)
# t2 = tuple(sorted(t1))      #--> highly expensive
# print(t2)
# t3 = tuple(sorted(t1,reverse=True))  #--> highly expensive
# print(t3)

# # min()
# t1= (7,18,45,77,7)
# print(min(t1))

# # max()
# t1= (7,18,45,77,7)
# print(max(t1))

# # comparison operators
# t1 = (7,18,45,77,7)
# t2 = (7,18,45,77,7)
# t3 = (7,7,18,45,77)
# print(t1 > t2)
# print(t1 >= t2)
# print(t1 < t3)
# print(t1 <= t3)

# # equality Operators
# t1 = (7,18,45,77,7)
# t2 = (7,18,45,77,7)
# t3 = (7,7,18,45,77)
# print(t1 == t2)
# print(t1 == t3)
# print(t1 != t3)

# # identity operators
# t1 = (7,18,45,77,7)
# t2 = t1
# t3 = (7,18,45,77,7)
# print(t1 is t2)
# print(t1 is t3)           # ***** Surprise

# # Tuple Packing and Unpacking
# # Packing
# a=10
# b=20
# c=30
# d=40
# t = a,b,c,d
# print(t,type(t))

# # unpacking
# t = (7,18,45,77,7)
# a,b,c,d,e = t
# print(a)
# print(d)
# # ValueError in case of unpacking
# # a,b,c,d = t
# # print(a,b,c,d)
# # a,b,c,d,e,f = t
# # print(a,b,c,d,e,f)
# # How to Handle
# # 1.use len() before unpacking and then unpack accordingly
# # 2. use * with last variable
# a,b,*c = t
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))

# # write a program to take tuple of numbers from the keyboard
# # and print its sum and average
# t = eval(input('Enter a Tuple of Numbers : '))     #(10,20,30,40,50)
# sum = sum(t)
# avg = sum / len(t)
# print('Sum :',sum)
# print('Avg :',avg)
