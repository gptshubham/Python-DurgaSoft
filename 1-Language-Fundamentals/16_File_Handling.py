# Temporary Storage Areas

# d = {}
# for i in range(3):
#     name=input('Enter Name: ')
#     balance = int(input('Enter Balance : '))
#     d[name]=balance
#     # data is not available after execution is completed --> Temporary Storage Area
#
# print(d)

# Permanent Storage Areas --> files,databases,big data technologies

# files

# # Opening a file
# f=open('abc.txt')        # default mode --> 'r'
# # Reading data from file
# data = f.read()
# # Printing data
# print(data)
# f.close()
# print()
# # # file Properties and various modes

# # 'r' mode --> Existing File
# f=open('abc.txt')
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)
# print()

# # 'r' mode --> Non-Existing File
# f=open('xyz.txt')                 # FileNotFoundError
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'w' mode --> Existing File
# f=open('abc.txt','w')
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'w' mode --> Non-Existing File
# f=open('abc01032024.txt','w')         # file got created
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'a' mode  --> Existing File
# f=open('abc.txt','a')
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'a' mode  --> Non-Existing File
# f=open('xyz.txt','a')                  # file got created
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'r+' mode  --> Existing File
# f=open('abc.txt','r+')
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'r+' mode --> Non-Existing File
# f=open('xyz01032024.txt','r+')                 # FileNotFoundError
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'w+' mode --> Existing File
# f=open('abc.txt','w+')
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'w+' mode --> Non-Existing File
# f=open('xyz01032024.txt','w+')         # file got created
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'a' mode  --> Existing File
# f=open('abc.txt','a')
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'a+' mode  --> Non-Existing File
# f=open('lmn.txt','a+')                  # file got created
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'x' mode  --> Existing File
# f=open('xyz.txt','x')                    # FileExistsError
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

# # 'x' mode  --> Non-Existing File
# f=open('lmn01032024.txt','x')              # file got created
# print('File Name: ',f.name)
# print('File Mode: ',f.mode)
# print('Is File Readable: ',f.readable())
# print('Is File Writable: ',f.writable())
# print('Is File Closed: ',f.closed)
# f.close()
# print('Is File Closed: ',f.closed)

