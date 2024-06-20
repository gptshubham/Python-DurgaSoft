# Also Refer to python_pattern Module

# Pattern 1 : Single Row of Stars
'''
# taking number of asterisks as input from user
n = int(input('Enter the Number of Asterisks: '))

# printing Single Row of Asterisks Pattern
print('* ' * n)

# Alternatively : using for loop
for i in range(n):
    print('*',end=' ')
'''

# Pattern 2 : square
'''
# taking number of rows as input from user
n = int(input('Enter the number of rows: '))

# printing square_of_asterisks pattern using for loop
for asterisk in range(n):
    print('* ' * n)
'''

# Alternatively : using nested for loop
'''
n = int(input('Enter the number of rows: '))
pattern_of = input('Enter tha character: ')
for row in range(n):
    for col in range(n):
        print(pattern_of, end=' ')
    print()
'''

# Pattern 3 : Constant Row Number Pattern / Number Grid Pattern / Number Matrix Pattern
'''
# taking number of rows as input from user
n = int(input('Enter the number of rows: '))

# printing Constant Row Number Pattern using for loop
for row in range(n):
    for col in range(n):
        print(row + 1, end=' ')
    print()
'''
# Alternatively:
'''
# taking number of rows as input from user
n = int(input('Enter the number of rows: '))

# printing Constant Row Number Pattern using for loop
for row in range(1, n + 1):
    for col in range(n):
        print(row, end=' ')
    print()
'''

# Pattern 4 : Alphabet Row Pattern / Alphabet Grid Pattern / Repeated Character Row Pattern
'''
# print(chr(97))
# print(ord('A'))
# taking number of rows as input from user
n = int(input('Enter the Number of Rows: '))

# printing Alphabet Row Pattern using for loop
for row in range(n):
    for col in range(n):
        print(chr(65 + row), end=' ')
    print()
'''

# Pattern 5 : Repeated Row Number Pattern
'''
# taking number of rows as input from user
n = int(input('Enter the Number of Rows: '))

# printing Repeated Row Number Pattern using for loop
for row in range(n):
    for col in range(n):
        print(col + 1, end=' ')
    print()
'''
# Alternatively:
'''
# taking number of rows as input from user
n = int(input('Enter the Number of Rows: '))

# printing Repeated Row Number Pattern using for loop
for row in range(n):
    for col in range(1, n + 1):
        print(col, end=' ')
    print()
'''

# Pattern 6 : Descending Number Pattern
'''
# taking number of rows as input from user
n = int(input('Enter the Number of Rows: '))

# printing Descending Number Pattern using for loop
for row in range(n):
    for col in range(n, 0, -1):
        print(col, end=' ')
    print()
'''

# Alternatively:
'''
# taking number of rows as input from user
n = int(input('Enter the Number of Rows: '))

# printing Descending Number Pattern using for loop
for row in range(n):
    for col in range(n):
        print(n - col, end=' ')
    print()
'''

# Pattern 7 : Right Triangle Star Pattern
'''
# taking number of rows as input from user
n = int(input('Enter the Number of Rows: '))

# printing Right Triangle Star Pattern using for loop
for row in range(n):
    for col in range(row + 1):
        print('*', end=' ')
    print()
'''
# Alternatively
'''
# taking number of rows as input from user
n = int(input('Enter the Number of Rows: '))

# printing Right Triangle Star Pattern using for loop
for row in range(n):
    print('* ' * (row + 1))
'''

# Pattern 8 : Descending Number Triangle
'''
# taking number of rows as input from user
n = int(input('Enter the Number of Rows: '))

for row in range(n):
    for col in range(row + 1):
        print(n - col, end=' ')
    print()
'''

# Pattern 9 : Pyramid Pattern
# taking number of rows as input from user
n = int(input('Enter the Number of Rows: '))

# Printing Pyramid Pattern
for row in range(n):
    print(' ' * (n - (row + 1)),end='')
    print('* ' * (row + 1))

