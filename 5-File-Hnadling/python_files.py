# # collection related data structures --> temporary storage of data
#
# l = []
# while (data := input('Enter some name: ')) != 'done':
#     l.append(data)
# print(l)

# file properties

f = open('abc.txt', 'r')
print('File Name: ', f.name)
print('File Mode: ', f.mode)
print('Is File Readable: ', f.readable())
print('Is File Writable: ', f.writable())
print('Is File Closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

# default mode
f = open('abc.txt')
print('File Name: ', f.name)
print('File Mode: ', f.mode)
print('Is File Readable: ', f.readable())
print('Is File Writable: ', f.writable())
print('Is File Closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

# w mode
f = open('abc.txt', 'w')
print('File Name: ', f.name)
print('File Mode: ', f.mode)
print('Is File Readable: ', f.readable())
print('Is File Writable: ', f.writable())
print('Is File Closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

# a mode
f = open('abc.txt', 'a')
print('File Name: ', f.name)
print('File Mode: ', f.mode)
print('Is File Readable: ', f.readable())
print('Is File Writable: ', f.writable())
print('Is File Closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

# r+ mode
f = open('abc.txt', 'r+')
print('File Name: ', f.name)
print('File Mode: ', f.mode)
print('Is File Readable: ', f.readable())
print('Is File Writable: ', f.writable())
print('Is File Closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

# w+ mode
f = open('abc.txt', 'w+')
print('File Name: ', f.name)
print('File Mode: ', f.mode)
print('Is File Readable: ', f.readable())
print('Is File Writable: ', f.writable())
print('Is File Closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

# a+ mode
f = open('abc.txt', 'a+')
print('File Name: ', f.name)
print('File Mode: ', f.mode)
print('Is File Readable: ', f.readable())
print('Is File Writable: ', f.writable())
print('Is File Closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

# x mode
# f = open('abc.txt', 'x')
f = open('xyz.txt', 'x')
print('File Name: ', f.name)
print('File Mode: ', f.mode)
print('Is File Readable: ', f.readable())
print('Is File Writable: ', f.writable())
print('Is File Closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)
