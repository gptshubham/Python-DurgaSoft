# function vs. method
'''
print(type(print))
print([].append)
print(type(list))
print(type(eval))
'''

# dict --> list Conversion
'''
d = {"firstName": 'shubham', "middleName": 'kumar', "lastname": 'gupta'}
# list of keys of dict (preferred)
l = list(d)
print(l, type(l), sep='\n')

# Alternatively: using .keys() method
keys = d.keys()
print(keys, type(keys), sep='\n')

keys_list = list(d.keys())
print(keys_list, type(keys_list), sep='\n')

# list of values of dict
values = d.values()
print(values, type(values), sep="\n")

values_list = list(d.values())
print(values_list, type(values_list), sep="\n")
'''


# List Methods

# 1. Getting Info about List --> len(), .count(), .index()

# .count()
'''
L = [10, 20, 10, 20, 30, 10, 20, 40, 20]
print(L.count(10))
print(L.count(20))
print(L.count(1000))
'''

# .index()
'''
L = [10, 20, 10, 20, 30, 10, 20, 40, 20]
print(L.index(10))
print(L.index(20))
print(L.index(30))
# print(L.index(1000))
'''

# Handling ValueError while using .index() method
# print(L.find(10)) --> find method is not available for list
# so, we are going to build find method for list from scratch
'''


def find(list, element):
    if element in L:
        return L.index(element)
    else:
        return -1


L = [10, 20, 10, 20, 30, 10, 20, 40, 20]
element = int(input('Enter an Element to Look For: '))
result = find(L, element)
print(result)
'''

# 2A. Manipulation of List Elements --> .append(), .insert(), .extend()
'''
# .insert()
name = 'shubham gupta'
# insert kumar in the middle
name_list = name.split()
# print(name_list)
name_list.insert(1, 'kumar')
# print(name_list)
revised_name = ' '.join(name_list)
print(revised_name)

L = [10, 20, 10, 20, 30, 10, 20, 40, 20]
L.insert(100, 50)
print(L)  # No IndexError

# .extend()
L1 = ['chicken', 'mutton', 'fish']  # my favourite example, even though I'm a vegetarian
L2 = ['KF', 'RC', 'FO']
L1.extend(L2)
print(L1)
'''

# 2B. Manipulation of List Elements --> .remove(), .pop(), .clear()
# .remove()
'''
L1 = ['chicken','mutton','fish']
print(L1)
L2 = L1.remove('fish')
print(L1)
print(L2)
# L1.remove('Fish')
# ValueError: list.remove(x): x not in list

# Handling ValueError
remove_item = input('Enter Item to remove from list: ')
if remove_item in L1:
    L1.remove(remove_item)
else:
    print('Item not in List!')


# removing an element which is available multiple times
L1 = ['KF', 'KF', 'RC', 'KF', 'KF', 'FO', 'KF']
remove_item = input('Enter an Item to remove from list: ')

while True:
    if remove_item in L1:
        L1.remove(remove_item)
    else:
        break
print(L1)

# Alternatively: using try except statement
L1 = ['KF', 'KF', 'RC', 'KF', 'KF', 'FO', 'KF']
remove_item = input('Enter an Item to remove from list: ')

while True:
    try:
        L1.remove(remove_item)
    except:
        break
print(L1)
'''

# .pop()
'''
L1 = [9211, 'AK47', 'AK203', 'Donald Trump', 'Joe Biden']
pop_item = L1.pop()
print("Item Popped: ",pop_item)
print(L1)

# .pop() and IndexError
L1 = list()
# L1.pop()
# IndexError: pop from empty list

# Handling IndexError
if L1:
    L1.pop()
else:
    print("list is empty!")

# Alternatively: using try / except Statement
try:
    L1.pop()
except:
    print('List is empty!')


# Another case of IndexError --> index out of range
# and how to avoid such error
L1 = [9211, 'AK47', 'AK203', 'Donald Trump', 'Joe Biden']
pop_item_index = int(input('Enter Index Position to Pop Out: '))

try:
    L1.pop(pop_item_index)
except:
    print('Index Out of Range!')

# Alternatively: using len() function
L1 = [9211, 'AK47', 'AK203', 'Donald Trump', 'Joe Biden']
pop_item_index = int(input('Enter Index Position to Pop Out: '))

if pop_item_index < len(L1):
    L1.pop(pop_item_index)
else:
    print('Index Out of Range!')

# popping items in the forward direction
L1 = [9211, 'AK47', 'AK203', 'Donald Trump', 'Joe Biden']
print(L1)
i = 0
while L1:
    print(f'Popped Element: {L1.pop(i)}')
print(L1)

# # popping items in the backward direction
L1 = [9211, 'AK47', 'AK203', 'Donald Trump', 'Joe Biden']
print(L1)

i = -1
while L1:
    print(f'Popped Element: {L1.pop(i)}')
print(L1)
'''

# .clear()
'''
L1 = [9211,'AK47','AK203','Donald Trump','Joe Biden']
print(L1)
L1.clear()
print(L1)
L1.clear()
'''

# 3. Ordering Elements of List --> .reverse(), .sort()

# reverse()
'''
L1 = [9211,'AK47','AK203','Donald Trump','Joe Biden']
print(L1)
L1.reverse()
print(L1)
'''

# sort() --> ascending order / alphabetical order
'''
L1 = [40, 20, 30, 10, 50, 40]
print(L1)
L1.sort()
print(L1)

L1 = ['salman', 'khan', 'akshay', 'kumar']
print(L1)
L1.sort()
print(L1)

# TypeError
L1 = [40, 20, 30, 'salman', 'khan']
# L1.sort()

# L2 = sorted(L1)

# sorting elements in reverse order --> descending order / reversed alphabetical order
L1 = [40, 20, 30, 10, 50, 40]
print(L1)

L1.sort(reverse=True)
print(L1)

# Alternatively: using sorted() function
L1 = [40, 20, 30, 10, 50, 40]
print(L1)
L2 = sorted(L1, reverse=True)
print(L2)
'''

# Aliasing vs Cloning

# Aliasing
'''
L1 = [10, 20, 30, 40]
L2 = L1
print(L1)
print(L2)
L1[0] = 777
print(L1)
print(L2)
L2[-1] = 999
print(L1)
print(L2)
'''

# Cloning

# Cloning using Slice Operator
'''
L1 = [10, 20, 30, 40]
L2 = L1[:]
print(L1)
print(L2)
L1[0] = 777
print(L1)
print(L2)
L2[-1] = 999
print(L1)
print(L2)
'''

# Cloning using .copy()
'''
L1 = [10, 20, 30, 40]
L2 = L1.copy()
print(L1)
print(L2)
L1[0] = 'kkk'
print(L1)
print(L2)
L2[-1] = 'jjj'
print(L1)
print(L2)
'''

# Mathematical Operators for List Objects
