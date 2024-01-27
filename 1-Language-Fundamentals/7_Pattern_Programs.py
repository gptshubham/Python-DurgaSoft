# Pattern Programming

# # 1. print the given number of stars
# n = int(input('Number of Stars to Display : '))
# print('* ' * n)
#
# # Alternatively: using for loop
# n = int(input('Number of Stars to Display : '))
# for rows in range(n):
#     print('*',end=' ')
# # print() to print the next input line in a separate line
# print()
#
# # Alternatively using while loop
# n = int(input('Number of Stars to Display : '))
# while n>0:
#     print('*',end=' ')
#     n -= 1

# # 2. square patterns

# # 2A. print *'s in square pattern
# n = int(input('Enter length of square : '))
# for rows in range(n):
#     print('*  ' * n)
#
# # Alternatively: using for loop
# n = int(input('Enter length of square : '))
# for rows in range(n):
#     print('*',end='  ')
#     for cols in range(n-1):
#         print('*',end='  ')
#     print()

# # 2B. print character provided by user
# # in square pattern
# n = int(input('Enter length of square : '))
# ch = input('Enter the character to print ; ')
# for rows in range(n):
#     print('%s  ' %ch * n)

# # 2C. print value of n in square pattern
# n = int(input('Enter length of square : '))
# ch = str(n)
# for rows in range(n):
#     print('%s  ' %ch * n)

# # 2D. print square pattern row number-wise
# n = int(input('Enter length of square : '))
# for i in range(n):
#     print((str(i+1)+'  ') * n)
#
# # Alternatively: using for loop
# n = int(input('Enter length of square : '))
# for rows in range(0,n):
#     print(rows+1,end='  ')
#     for cols in range(0,n-1):
#         print(rows+1,end='  ')
#     print()

# # 2E. Square Pattern: R1->A,R2->B,R3->C,.....
# n = int(input('Enter length of square : '))
# ch = ord('A')
# for rows in range(n):
#     print((chr(ch + rows)+'  ')*n)
# # Alternatively:
# n = int(input('Enter length of square : '))
# for rows in range(n):
#     print((chr(65+rows)+'  ')*n)

# # 2F. Square Pattern: 1 2 3 4 5 * n times Row-wise
# n = int(input('Enter length of square : '))
# for rows in range(n):
#     for cols in range(n):
#         print(cols+1,end='  ')
#     print()

# # 2G. Square Pattern: 5,4,3,2,1 *n times Row-wise
# n = int(input('Enter length of square : '))
# for rows in range(n):
#     for cols in range(n,0,-1):
#         print(cols,end='  ')
#     print()

# # 3A. Right Angle Triangle: * Pattern
# n = int(input('Enter the Height of RAT : '))
# for rows in range(n):
#     print('* ' * (rows+1))
# # Alternatively using Nested Loops
# n = int(input('Enter the Height of RAT : '))
# for rows in range(n):
#     for cols in range(rows+1):
#         print('*',end=' ')
#     print()

# # 3B. Right Angle Triangle: number pattern 1,22,333,4444,55555
# n = int(input('Enter the Height of RAT : '))
# for rows in range(n):
#     print((str(rows+1) + ' ') * (rows+1))

# # 3C. Right Angle Triangle: number pattern 1,12,123,1234,12345
# n = int(input('Enter the Height of RAT : '))
# for rows in range(n):
#     for cols in range(rows+1):
#         print(cols+1,end=' ')
#     print()
# # Alternatively: using while loop
# n = int(input('Enter the Height of RAT : '))
# rows = 0
# while rows<n:
#     cols = 0
#     while cols<=rows:
#         print(cols+1,end=' ')
#         cols += 1
#     rows += 1
#     print()

# # 3D. Right Angle Triangle: number pattern 5,54,543,5432,54321
# n = int(input('Enter the Height of RAT : '))
# for rows in range(n,0,-1):
#     for cols in range(n,rows-1,-1):
#         print(cols,end=' ')
#     print()
# # Alternatively: using positive indexing
# n = int(input('Enter the Height of RAT : '))
# for rows in range(n):
#     for cols in range(rows+1):
#         print(n-cols,end=' ')
#     print()

# # 3E. Right Angle Triangle: number pattern
# # 1,21,321,4321,54321
# n = int(input('Enter the Height of RAT : '))
# for rows in range(n):
#     for cols in range(rows+1,0,-1):
#         print(cols,end=' ')
#     print()

# # 4. Pyramid * Pattern
# n = int(input('Enter the value of n : '))
# for i in range (n):
#     print(' '*(n-i-1),end='')
#     print('* '*(i+1))

# # 5. Hollow Diamond --> those two stars at both ends
# # killed my efforts 😂
# n = int(input('Enter the value of n : '))
# for i in range(n):
#     print(' '*(n-i-1),end='')
#     print('*',end='')
#     print(' '*(i*2),end='')
#     print('*')
# for i in range(n):
#     print(' '*i,end='')
#     print('*',end='')
#     print(' '*((n-i-1)*2),end='')
#     print('*')

# Hollow Diamond Pattern --> Right Approach
n = int(input('Enter the value of n : '))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range((i*2)+1):
        if j == 0 or j == 2*i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range((i*2)+1):
        if j == 0 or j == 2*i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
