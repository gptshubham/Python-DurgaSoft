# # creating list with Dynamic Input
# L = input('Enter a List : ')            # [10,20,30,40]
# print(type(L))                          # str

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
