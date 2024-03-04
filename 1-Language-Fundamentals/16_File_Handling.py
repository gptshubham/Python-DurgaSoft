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


# writing data to text files

# # write()
# f = open('abc.txt','w')
# f.write('Dhoni\n')
# f.write('Kohli\n')
# f.write('Sachin\n')
# f.write('Rohit\n')
# print('Data written to the file successfully')
# f.close()

# # write() --> Non-Existing File
# f = open('abc020324.txt','w')         # new file created
# f.write('Dhoni ')
# f.write('Kohli ')
# f.write('Sachin ')
# f.write('Rohit ')
# print('Data written to the file successfully')
# f.close()

# # writelines() --> list
# f = open('abc.txt','w')
# L = ['Dhoni\n','Kohli\n','Sachin\n','Rohit\n','Rahul']
# f.writelines(L)
# print('Data written to the file successfully')
# f.close()

# # writelines() --> set
# f = open('abc.txt','w')
# s = {'Dhoni\n','Kohli\n','Sachin\n','Rohit\n','Rahul\n'}
# f.writelines(s)
# print('Data written to the file successfully')
# f.close()

# # writelines() --> tuple
# f = open('abc.txt','w')
# t = ('Dhoni\n','Kohli\n','Sachin\n','Rohit\n','Rahul')
# f.writelines(t)
# print('Data written to the file successfully')
# f.close()

# # writelines() --> dict
# f = open('abc.txt','w')
# # d = {7: 'Dhoni',18:'Kohli',10:'Sachih',45:'Rohit'}
# # TypeError: write() argument must be str, not int
# d = {'7': 'Dhoni','18':'Kohli','10':'Sachih','45':'Rohit'}
# f.writelines(d)
# print('Data written to the file successfully')
# f.close()

# # creating file in a particular folder
# f = open('C:\\Shubham\\Durgasoft\\Python\\1-Language-Fundamentals\\test_files\\xyz.txt','w')   # *** \\
# f.write('First Line\n')
# f.write('Second Line\n')
# f.write('Third Line\n')
# print('Data written to the file successfully')
# f.close()


# # Writing Dynamic Data to the Dynamic File
#
# file_name = input('Enter File Name : ')
# f = open('C:\\Shubham\\Durgasoft\\Python\\1-Language-Fundamentals\\test_files\\studentdata\\'+file_name,'w')
# while True:
#     data = input('Enter data to write : ')
#     f.write(data+'\n')
#     option = input('More Data ? [Y|N] : ')
#     if option.lower() == 'n':
#         break
# print('Data written successfully!')
# f.close()

# # Reading data from a file

# # read()
# f = open('abc.txt')
# data = f.read()
# print(data)
# f.close()
# print()

# # read(n)
# f =open('abc.txt')
# print(f.read(5))
# print(f.read(5))
# f.seek(0)
# print(f.read(15))
# f.close()
# print()

# # readline()
# f = open('abc.txt')
# data = f.readline()
# print(data,end='')
# data = f.readline()
# print(data,end='')
# data = f.readline()
# print(data,end='')
# data = f.readline()
# print(data,end='')

# # readline() with while loop
# f = open('test_files\\studentdata\\Varsha.txt')
# line = f.readline()
# while line:
#     print(line,end='')
#     line = f.readline()
# f.close()

# # skipping blank lines
# f = open('abc.txt')
# line = f.readline()
# while line:
#     if line != '\n':
#         print(line,end='')
#     line = f.readline()
# f.close()

# # readlines()
# f = open('abc.txt')
# lines = f.readlines()
# print(type(lines))
# for line in lines:
#     if line != '\n':
#         print(line,end='')
# f.close()

# # where is my pointer
# f = open('abc.txt')
# print(f.read(4))
# print(f.readline())
# print(f.read(14))
# print(f.read())

# # Use case 1: Read data from input.txt and write to output.txt
# # reading data from input.txt
# f1 = open('test_files\\input.txt')
# f2 = open('test_files\\output.txt','w')
# data = f1.read()
# f2.write(data)
# f1.close()
# f2.close()

# # with statement
#
# # data read from input.txt
# with open('test_files\\input.txt') as f:
#     data = f.read()
#     print('data read from input.txt:')
#     print(data)
#     print('Is file closed: ',f.closed)
# print('Is file closed: ',f.closed)
# print()
# # data written to output.txt
# with open('test_files\\output.txt') as f:
#     data = f.read()
#     print('data written to output.txt:')
#     print(data)
#     print('Is file closed: ',f.closed)
# print('Is file closed: ',f.closed)

