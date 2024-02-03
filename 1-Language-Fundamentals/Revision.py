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
