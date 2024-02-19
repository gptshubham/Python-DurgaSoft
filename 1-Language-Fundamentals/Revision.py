# # Merge characters of 2 strings into a single string by taking characters alternatively
# s = input('Enter First String : ')
# k = input('Enter Second String : ')
# sk = ''
#
# i=j=0
# while i<len(s) or j<len(k):
#     if i<len(s):
#         sk += s[i]
#         i+=1
#     if j<len(k):
#         sk += k[j]
#         j+=1
# print(sk)

# # write a program to sort alphanumeric characters present in the given string.
# # B2A1D3 --> ABD123
# s = input('Enter the String : ')
# sAlpha = ''
# sdigit = ''
# for i in s:
#     if i.isalpha():
#         sAlpha += i
#     else:
#         sdigit += i
# sAlpha = ''.join(sorted(sAlpha))
# sdigit = ''.join(sorted(sdigit))
# print(sAlpha + sdigit)

# # # Input: B2A1D3 --> every alphabet symbol followed by a single digit
# # # Output: BBADDD
# s = input('Enter the String : ')
# output = ''
# for i in s:
#     if i.isalpha():
#         ch = i
#     else:
#         output += ch * int(i)
# print(output)

# # Input: B12A11D13 --> every alphabet symbol followed by a number
# # Output: B*12 times + A*11 times + D*13 times
# s = input('Enter the String : ')
# output = ''
# digit = ''
# for i in range(len(s)):
#     if s[i].isalpha():
#         ch = s[i]
#     else:
#         digit += s[i]
#         if i < len(s) -1:
#             if s[i+1].isalpha():
#                 output += ch * int(digit)
#                 print(ch,output.count(ch),'times')
#                 digit = ''
#         if i == len(s) -1:
#             output += ch * int(digit)
#             print(ch,output.count(ch),'times')
# print(output)
# Note: while loop is preferred by the mentor as focus is very much on the index positions
# Also, for i in s does not seem appropriate in the given case => while loop ✔

# # Input: B2A1D3 --> Output: BDABDG
# s = input('Enter the String : ')
# output = ''
# for i in s:
#     if i.isalpha():
#         ch = i
#         output += i
#     else:
#         output += chr(ord(ch) + int(i))
# print(output)

# # Program 12: Remove duplicate characters from given string
# s = input('Enter the String : ')
# output = ''
# for i in s:
#         if i not in output:
#             output += i
# print(output.replace(' ',''))

# # write a program to print various indices where
# # a given substring is present in a given string
# # Input:string --> ABCDCDC,subString --> CDC , Output:2
# string = 'ABCDCDC'
# subString = 'CDC'
# start = 0
# end = len(string)
# count = 0
# i = 0
# while True:
#     position = string.find(subString,start,end)
#     if position != -1:
#         count += 1
#         start = position + len(subString) -1
#     else:
#         break
#     i+=1
# print(count)

# Sets
# s = {'s','k','g'}

# s.add((1,2,3))
# print(s)

# s.add([4,5,6])
# print(s)

# s.add({4,5,6})
# print(s)               # ***** Surprise!

# d = {10:'Sachin',7:'Dhoni',18:'Kohli'}

# s.add(d)
# print(s)

# s.update(d)
# print(s)

# s.update({4,5,6})
# print(s)

# s.update([4,5,6])
# print(s)

# s = {'s','k','g'}
#
# popped_item = s.pop()
# print(s)
# print(popped_item)
#
# popped_item = s.pop()
# print(s)
# print(popped_item)
#
# popped_item = s.pop()
# print(s)
# print(popped_item)
#
# if s:
#     popped_item = s.pop()
#     print(s)
#     print(popped_item)
# else:
#     print('Invalid Operation: pop from empty set!')

# s = {'s','k','g'}
# s.discard('m')
# print(s)

# s.clear()
# print(s)

# # lambda function
#
# # write a function to return square of given value
# s = lambda n:n**2
# print(s(7))

