# Square Pattern
def square():
    print('You chose to print SQUARE Pattern...')
    n = int(input('Enter length of square : '))
    for rows in range(n):
        print('*  ' * n)

# Right Angled Triangle
def right_angled_triangle():
    print('You chose to print Right Angled Triangle...')
    n = int(input('Enter the Height of RAT : '))
    for rows in range(n):
        print('* ' * (rows+1))

# Pyramid
def pyramid():
    print('You chose to print PYRAMID Pattern...')
    n = int(input('Enter the value of n : '))
    for i in range (n):
        print(' '*(n-i-1),end='')
        print('* '*(i+1))

# Diamond
def hollow_diamond():
    print('You chose to print Hollow Diamond Pattern...')
    n = int(input('Enter the value of n : '))
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for j in range((i * 2) + 1):
            if j == 0 or j == 2 * i:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(' ', end='')
        for j in range((i * 2) + 1):
            if j == 0 or j == 2 * i:
                print('*', end='')
            else:
                print(' ', end='')
        print()
