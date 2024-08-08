# # collection related data structures --> temporary storage of data
#
# l = []
# while (data := input('Enter some name: ')) != 'done':
#     l.append(data)
# print(l)

# # file properties
#
# f = open('abc.txt', 'r')
# print('File Name: ', f.name)
# print('File Mode: ', f.mode)
# print('Is File Readable: ', f.readable())
# print('Is File Writable: ', f.writable())
# print('Is File Closed: ', f.closed)
# f.close()
# print('Is File Closed: ', f.closed)

# # default mode
# f = open('abc.txt')
# print('File Name: ', f.name)
# print('File Mode: ', f.mode)
# print('Is File Readable: ', f.readable())
# print('Is File Writable: ', f.writable())
# print('Is File Closed: ', f.closed)
# f.close()
# print('Is File Closed: ', f.closed)

# # w mode
# f = open('abc.txt', 'w')
# print('File Name: ', f.name)
# print('File Mode: ', f.mode)
# print('Is File Readable: ', f.readable())
# print('Is File Writable: ', f.writable())
# print('Is File Closed: ', f.closed)
# f.close()
# print('Is File Closed: ', f.closed)

# # a mode
# f = open('abc.txt', 'a')
# print('File Name: ', f.name)
# print('File Mode: ', f.mode)
# print('Is File Readable: ', f.readable())
# print('Is File Writable: ', f.writable())
# print('Is File Closed: ', f.closed)
# f.close()
# print('Is File Closed: ', f.closed)

# # r+ mode
# f = open('abc.txt', 'r+')
# print('File Name: ', f.name)
# print('File Mode: ', f.mode)
# print('Is File Readable: ', f.readable())
# print('Is File Writable: ', f.writable())
# print('Is File Closed: ', f.closed)
# f.close()
# print('Is File Closed: ', f.closed)

# # w+ mode
# f = open('abc.txt', 'w+')
# print('File Name: ', f.name)
# print('File Mode: ', f.mode)
# print('Is File Readable: ', f.readable())
# print('Is File Writable: ', f.writable())
# print('Is File Closed: ', f.closed)
# f.close()
# print('Is File Closed: ', f.closed)

# # a+ mode
# f = open('abc.txt', 'a+')
# print('File Name: ', f.name)
# print('File Mode: ', f.mode)
# print('Is File Readable: ', f.readable())
# print('Is File Writable: ', f.writable())
# print('Is File Closed: ', f.closed)
# f.close()
# print('Is File Closed: ', f.closed)

# # x mode
# # f = open('abc.txt', 'x')
# f = open('xyz.txt', 'x')
# print('File Name: ', f.name)
# print('File Mode: ', f.mode)
# print('Is File Readable: ', f.readable())
# print('Is File Writable: ', f.writable())
# print('Is File Closed: ', f.closed)
# f.close()
# print('Is File Closed: ', f.closed)

# Writing data to the file --> write() and writelines()
"""
# 1. write(str)
f = open('abc1.txt', 'w')
f.write('Shubham')
f.write('Kumar')
f.write('Gupta')

print('Data Written to the file successfully')
f.close()

f = open('abc1.txt')
print(f.read())
f.close()

# \n for changing lines while writing data to a file
f = open('abc1.txt', 'w')
f.write('Shubham\n')
f.write('Kumar\n')
f.write('Gupta\n')

print('Data Written to the file successfully')
f.close()

f = open('abc1.txt')
print(f.read())
f.close()

# 'a' to append data (No Overwriting of Existing Data)
f = open('abc1.txt', 'a')
f.write('Shubham ')
f.write('Kumar ')
f.write('Gupta ')

print('Data Written to the file successfully')
f.close()

f = open('abc1.txt')
print(f.read())
f.close()

# 2. writelines(list of lines)
l = ['shubh', 'abhi', 'sonal', 'anya', 'deo']

f = open('abc1.txt', 'w')
for s in l:
    f.write(s)

f.close()

f = open('abc1.txt')
print(f.read())
f.close()

# \n for changing lines while writing data to a file
l = ['shubh', 'abhi', 'sonal', 'anya', 'deo']

f = open('abc1.txt', 'w')
for s in l:
    f.write(s + '\n')

f.close()

f = open('abc1.txt')
print(f.read())
f.close()

# alternatively: writelines()
l = ['shubh', 'abhi', 'sonal', 'anya', 'deo']

f = open('abc1.txt', 'w')
f.writelines(l)
print('List of lines written to the file successfully')
f.close()

f = open('abc1.txt')
print(f.read())
f.close()

# \n for changing lines while writing data to a file
l = ['shubh\n', 'abhi\n', 'sonal\n', 'anya\n', 'deo\n']

f = open('abc1.txt', 'w')
f.writelines(l)
print('List of lines written to the file successfully')
f.close()

f = open('abc1.txt')
print(f.read())
f.close()

# passing tuple instead of list
t = ('shubh\n', 'abhi\n', 'sonal\n', 'anya\n', 'deo\n')

f = open('abc1.txt', 'w')
f.writelines(t)
print('List of lines written to the file successfully')
f.close()

f = open('abc1.txt')
print(f.read())
f.close()

# passing set instead of list # order is not maintained
s = {'shubh\n', 'abhi\n', 'sonal\n', 'anya\n', 'deo\n'}

f = open('abc1.txt', 'w')
f.writelines(s)
print('List of lines written to the file successfully')
f.close()

f = open('abc1.txt')
print(f.read())
f.close()

# passing dict instead of list
d = {'shubh\n': 100, 'abhi\n': 200, 'sonal\n': 300, 'anya\n': 400, 'deo\n': 500}

f = open('abc1.txt', 'w')
f.writelines(d)  # only keys are written to the file
# keys must be str type otherwise : TypeError
print('List of lines written to the file successfully')
f.close()

f = open('abc1.txt')
print(f.read())
f.close()
"""
import csv

# Reading character data from the files
# --> read(), read(n), readline(), readlines()
'''
# reading entire data --> read()
f = open('abc1.txt')
print(f.read())
f.close()

# reading first 10 characters --> read(n)
f = open('abc1.txt')
print(f.read(10))  # '\n' is also counted as one character
f.close()

# reading data line by line --> readline()
f = open('abc.txt')
print(f.readline().rstrip())
print(f.readline().rstrip())
print(f.readline())
f.close()
# alternatively: using end= argument instead of rstrip()
f = open('abc.txt')
print(f.readline(),end='')
print(f.readline(),end='')
print(f.readline())
f.close()

# while loop with readline()
f = open('abc.txt')
line = f.readline()
while line != '':
    print(line,end='')
    line = f.readline()
f.close()
print()

# avoiding blank lines while reading data
f = open('abc2.txt')
line = f.readline()
while line != '':
    print(line.rstrip())
    line = f.readline()
f.close()
print()

# how to avoid such blank lines
f = open('abc2.txt')
line = f.readline()
while line != '':
    if line != '\n':
        print(line.rstrip())
    line = f.readline()
f.close()
print()

# readlines()
f = open('abc1.txt')
l = f.readlines()
print(l)

for line in l:
    print(line,end='')
f.close()
print()
# read() and readline() are mostly used methods
'''

# file pointer
'''
f = open('abc1.txt')
print(f.read(3))
print(f.read(5))
print(f.read())

# write a program to read data from input.txt and write to output.txt
f1 = open('input.txt')
f2 = open('output.txt', 'w')
data = f1.read()
f2.write(data)
print('The data copied successfully')
f1.close()
f2.close()
'''

# # with Statement
#
# with open('abc.txt') as f:
#     print(f.read())
#
# # checking if the file is closed after with statement
# with open('abc1.txt', 'w') as f:
#     f.write('Dhoni\n')
#     f.write('Kohli\n')
#     f.write('Rohit\n')
#     print('Is file closed: ', f.closed)
# print('Is file closed: ', f.closed)
#
# # reading data written to the file
# with open('abc1.txt') as f:
#     print(f.read())


# tell() and seek() Methods

# tell()
'''
f = open('abc.txt')
print(f.tell())
print(f.read(5))
print(f.tell())
print()
print(f.read())
print(f.tell())
f.close()

f = open('abc1.txt', 'w')
print(f.tell())
f.close()

f = open('abc2.txt', 'a')
print(f.tell())
f.close()

f = open('abc1.txt','r+')
print(f.tell())
f.close()

f = open('abc1.txt', 'w+')
print(f.tell())
f.close()

f = open('abc.txt', 'a+')
print(f.tell())
f.close()
'''

# seek()
'''
f = open('abc1.txt')
print(f.read(3))
f.seek(0)
print(f.read(3))
f.seek(10)
print(f.read(3))
'''

# data modification

# with open('xyz.txt', 'r+') as f:
#     text = f.read()
#     print('Data before modification: ')
#     print('#'*40)
#     print(text)
#     f.seek(17)
#     f.write('GEMS!!!')
#     f.seek(0)
#     text = f.read()
#     print('Data after modification: ')
#     print('#' * 40)
#     print(text)

# How to check a particular file exists or not ?
'''
import os
fname = input('Enter the File Name: ')
filecheck = os.path.isfile(fname)
if filecheck:
    print(f'{fname} is available')
else:
    print(f'{fname} is not available')
'''

# write a program to check whether the given file exists or not.
# if it's available then print it's content
'''
# importing os module
import os
# taking filename as input from the user
fname = input('Enter the File Name: ')
# checking if the file exists and storing the result in the filecheck variable
filecheck = os.path.isfile(fname)
# conditional statements to print output
if not filecheck:
    print(f'{fname} is not available!')
else:
    with open(fname) as f:
        print(f.read())
'''

# Write a program to print the number of lines, words and characters
# present in the given file?
'''
import os
fname = input('Enter file name: ')
fileckeck = os.path.isfile(fname)
if not fileckeck:
    print(f'{fname} is not available!')
else:
    with open(fname) as f:
        # number of lines in the file
        line_list = f.readlines()
        line_count = len(line_list)
        print(f'No. of Lines: {line_count}')
        # number of words and characters in the file
        char_count = 0
        word_count = 0
        for line in line_list:
            char_count += len(line)
            word_count += len(line.split())
        print(f'No. of Words: {word_count}')
        print(f'No. of Characters: {char_count}')

'''

# Hndling Binary Data --> Not recommended to use in the real world
'''
f1 = open('download.jpeg','rb')
f2 = open('dog1.jpeg','wb')
# f2.write(f1.read())
data = f1.read()  # bytes
# print(type(data))
f2.write(data)
print('New Image is available with the name: dog1.jpeg')
'''

# Handling CSV Files --> Very common requirement in real time
# However, Pandas Library is used extensively in real time

# writing data to the csv file:
'''
import csv
with open('emp.csv','w') as f:
    w = csv.writer(f)
    w.writerow(['ENO', 'ENAME', 'ESAL', 'EADDR'])
    w.writerow([100,'shubham',1000,'Kolkata'])
    w.writerow([100,'shubham',1000,'Kolkata'])
    w.writerow([100,'shubham',1000,'Kolkata'])
    w.writerow([100,'shubham',1000,'Kolkata'])
print('data written successfully')
'''

# read data from the enduser and write that data to the csv file
'''
import csv
with open('emp.csv','w') as f:
    w = csv.writer(f)
    w.writerow(['ENO', 'ENAME', 'ESAL', 'EADDR'])
    while True:
        eno = input('Enter Employee Number: ')
        ename = input('Enter Employee Name: ')
        esal = input('Enter Employee Salary: ')
        eaddr = input('Enter Employee Address: ')
        w.writerow([eno, ename, esal, eaddr])
        print('Record inserted successfully')
        option = input("more records? ['Yes'|'No']: ")
        if option.lower() == 'no':
            break
print('data written to the file successfully')
'''

# How to read data from a csv file
'''
import csv
with open('emp.csv') as f:
    r = csv.reader(f)
    # print(r)
    # print(type(r))
    data = list(r)
    print(data)
    for row in data:
        for col in row:
            print(col,'\t',end='')
        print()
'''

# Zipping and Unzipping Files
'''
# Creating Zip File
from zipfile import *
f = ZipFile('marks.zip','w',ZIP_DEFLATED)
f.write('abhi.txt')
f.write('shubham.txt')
f.write('sonal.txt')
f.close()
print('marks.zip file created successfully')

# Unzipping a Zipped File
f = ZipFile('marks.zip','r',ZIP_STORED)  # ZIP_STORED is default value
names = f.namelist()
# print(names)
for name in names:
    print('File Name: ',name)
    print('The Content of the file is: ')
    f1 = open(name,'r')
    print(f1.read())
    f1.close()
    print()
'''

