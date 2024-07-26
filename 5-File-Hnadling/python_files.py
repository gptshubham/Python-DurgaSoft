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

# Reading character data from the files
# --> read(), read(n), readline(), readlines()

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

# file pointer
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