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

# write a program to read string from the keyboard and print its
# characters in both the forward and the backward direction
s = input('Enter a String : ')
print('forward direction: {}\nbackward direction: {}'.format(s[::],s[::-1]))
# using while loop
# forward direction
s = input('Enter a String : ')
count = 0
while count<len(s):
    print(s[count])
    count += 1
# backward direction
s = input('Enter a String : ')
count = len(s) -1
while count>=0:
    print(s[count])
    count -= 1
# using for loop
# forward direction
s = input('Enter a String : ')
for i in s:
    print(i)
# backward direction
s = input('Enter a String : ')
for i in range(len(s)-1,-1,-1):
    print(s[i])