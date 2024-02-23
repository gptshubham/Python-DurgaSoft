# Password Generation API Mini Project

# generate random password of given length (>= 8) where even index positions are
# alphabet symbols and odd index positions are digits

from random import *

# creating alphabet list
alphabets = []
for i in range(ord('A'),ord('Z')+1):
    alphabets.append(chr(i))
for i in range(ord('a'),ord('z')+1):
    alphabets.append(chr(i))

# creating digits range odject
digits = range(0,9)

# password function
def password(n):
    # length validation
    if n < 8:
        return 'Invalid Input! Please select an input >= 8'
    else:
        # creating password variable
        password = ''
        # creating password using for loop, str concatenation,and choice()
        for i in range(n):
            if i%2 == 0:
                password += str(choice(digits))
            else:
                password += choice(alphabets)
        # printing output
        return password

# print(password(16))