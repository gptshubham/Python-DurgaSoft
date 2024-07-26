# File Handling Mini Project 1 :
# take username and marks of different subjects from user
# create a new file dynamically
# write marks data entered by user to the file

name = input('Enter your name: ')
f = open(f'{name.lower()}.txt', 'w')
m1 = input('Enter marks of Python: ')
m2 = input('Enter marks of Java: ')
m3 = input('Enter marks of Oracle: ')
m4 = input('Enter marks of Linux: ')
f.write(f'Student Name: {name}\n')
f.write('#'*50 + '\n')
f.write(f'Python: {m1}\n')
f.write(f'Java: {m2}\n')
f.write(f'Oracle: {m3}\n')
f.write(f'Linux: {m4}')
print('You marks entered successfully')
f.close()
