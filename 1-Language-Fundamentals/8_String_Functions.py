# string --> most commonly used data type in Python
# use '''Shubham's Msg reads "Let's Party!"'''
# to avoid using escape characters

# # Indexing

# # Positive Indexing
# s = 'Dhoni'
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])

# # negative indexing
# s = 'Kohli'
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])

# # write a program to read string from the keyboard and display its characters
# # by index-wise (both positive index and negative index)
# # Hint: PI - Length = NI
# s = input('Enter a string : ')
# count = 0
# for i in s:
#     print('The Character Present at Positive Index {} and Negative Index {} is {}'.format(count,count-len(s),i))
#     count += 1

# # Slice Operator (Slicing)

# # s[begin:end:step]
# user = 'Shubham Kumar Gupta'
# begin = user.index('S')
# print(begin,type(begin))
# end = user.index('m') +1
# print(end,type(end))
# firstName = user[begin:end]
# print(firstName)
# begin = user.index('K')
# end = user.index('r')+1
# middleName = user[begin:end]
# print(middleName)
# begin = user.index('G')
# lastName = user[begin:]
# print(lastName)

# # Alternatively using sliceOf() --> I'm trying to be over smart here 😜
# # However it turned out to be worth it as the function sliceOf works
# def sliceOf(string, char1, char2):
#     start = string.index(char1)
#     end = string.index(char2) +1
#     subString = string[start:end]
#     return subString
#
# user = 'shubham kumar gupta'
# firstName = sliceOf(user, 's', 'm')
# print(firstName)
# middleName = sliceOf(user, 'k', 'r')
# print(middleName)
# lastName = sliceOf(user, 'g', 'a')
# print(lastName)
# # last name isn't working as index gives us the first occurrence
# # of character in the string and not the subsequent ones
# # Hence, it's not going to work with the last character and
# # in all such cases where character is occurring multiple times
# # throughout the string
# # Let's go old school and fetch that lastName
# lastName = user[user.index('g'):]
# print(lastName)

# # step size
# user = 'shubham kumar gupta'
# # I'm going to perform postmortem of my name 😬🤪
# print(user[::2])
# print(user[user.index('s'):user.index('m')+1:2])
# print(user[user.index('s'):user.index('r')+1:3])
# print(user[len(user)-1::-2])
# # slice operator never throws IndexError
# print(user[3:3000])

# # a basic example of slice operator
# s = 'abcdefghij'
# print(s[1:6:2])
# print(s[::1])       # complete string in original order
# print(s[::-1])      # complete string in reverse order
# print(s[5:2:-1])    # let's talk finance
# print(s[-7:-9:-1])  # let's talk us politics
# # print(s[::0])     # ValueError: slice step cannot be zero

# # write a program to read string from the keyboard and print its
# # characters in both the forward and the backward direction
# s = input('Enter a String : ')
# print('forward direction: {}\nbackward direction: {}'.format(s[::],s[::-1]))
# # using while loop
# # forward direction
# s = input('Enter a String : ')
# count = 0
# while count<len(s):
#     print(s[count])
#     count += 1
# # backward direction
# s = input('Enter a String : ')
# count = len(s) -1
# while count>=0:
#     print(s[count])
#     count -= 1
# # using for loop
# # forward direction
# s = input('Enter a String : ')
# for i in s:
#     print(i)
# # backward direction
# s = input('Enter a String : ')
# for i in range(len(s)-1,-1,-1):
#     print(s[i])

# # String Functions

# # strip() --> Removes spaces from the string : "    Dhoni   " --> "Dhoni"
# print(type('Dhoni') == str)
# favPlayer = input('''Enter Your Favourite Player's Name : ''')
# if favPlayer == 'Dhoni':
#     print('Your Favourite Player is %s' %favPlayer)
# # what if end user enters Dhoni with a space in the beginning or the end ?

# favPlayer = input('''Enter Your Favourite Player's Name : ''')
# favPlayer = favPlayer.strip()
# if favPlayer == 'Dhoni':
#     print('Your Favourite Player is %s' %favPlayer)

# # finding the substring

# # find()
# s = 'shubham kumar gupta'
# print(s.find('a'))
# print(s.find('kumar'))
# print(s.find('K'))             # find() returns -1 if substring is not available
# print(s.find('m'))             # it does not throw error
# print(s.find('a',8,12))
# print(s.find('s',6,12))

# # rfind()
# s = 'shubham kumar gupta'
# print(s.rfind('a'))
# print(s.rfind('a',8,12))
# print(s.rfind('m',6,12))
# print(s.rfind('s',6,12))

# # index()
# s = 'shubham kumar gupta'
# print(s.index('a'))
# print(s.index('kumar'))
# print(s.index('K'))

# customCount()
# # write a program to print various indices where
# # a given substring is present in a given

# # customCount Method: using for loop
# # --> works only if we are looking for a character only

# userInput = input('Enter a String : ')
# subString = input('Enter Sub-String to search for : ')
# l = []
# for i in range(0, len(userInput)):
#     if userInput[i] == subString:
#         l.append(i)
# print(l)

# # customCount Method: using while loop and find()
# # --> works with both characters and subStrings
# def customCount(str1,str2):
#     start = 0
#     end = len(userInput)
#     L =[]
#     count = 0
#     while True:
#         position = userInput.find(subString, start, end)
#         if position == -1:
#             print('No. of Occurrences :', count)
#             break
#             # can use flag also instead of break
#         else:
#             L.append(position)
#             # can also store positions in a list
#             start = position + len(subString)     # This one is unique
#             count += 1
#     return L

# userInput = input('Enter a String : ')
# subString = input('Enter Sub-String to search for : ')
# positionList = customCount(userInput,subString)
# print(positionList)
# # count()
# freq = userInput.count(subString)
# print("No of occurrences of '{}' in '{}' =".format(subString,userInput),freq)
# print(userInput.count(subString,5,10))

# # replace()
# userInput = input('Enter a String : ')
# target = input('Enter the target to replace : ')
# replacement = input('Enter the Replacement : ')
# userInput = userInput.replace(target,replacement)
# print(userInput)
# removing space with replace()
# # "      Shubham    K  uma   r   Gupt    a       " --> "ShubhamKumarGupta"
# spacedInput = input('Enter Your Name : ')
# user = spacedInput.replace(' ','')
# print(user)
# no_of_spaces = len(spacedInput) - len(user)
# print(no_of_spaces)

# split()
userInput = input('Enter a String : ')
userList = userInput.split()
print(userList)

userInput = input('Enter a String : ')
userList = userInput.split('-')
print(userList)

userInput = input('Enter a String : ')
userList = userInput.split(',')
print(userList)
