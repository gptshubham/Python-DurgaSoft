# write a program to read string from the keyboard and display its characters
# by index-wise (both positive index and negative index)
'''
input_str = input('Enter a String: ')
for i in range(len(input_str)):
    print(f'{i} : {input_str[i]}')
'''

# Finding Substring : Forward Direction --> find(), index()
# extract 'gupta' from name
'''
name = 'shubham kumar gupta'
begin = name.index('g')
sub_str = name[begin:]
print(sub_str)
'''

# extract 'kumar' from name : using .find() --> Preferred
'''
name = 'shubham kumar gupta'
first_space = name.find(' ')
second_space = name.find(' ',first_space + 1)
sub_str = name[first_space + 1:second_space]
print(sub_str)
'''

# Alternatively: using .index()
'''
name = 'shubham kumar gupta'
begin = name.index('k')
end = name.index('r') + 1
sub_str = name[begin:end]
print(sub_str)
'''

# extract 'shubham' from name
'''
name = 'shubham kumar gupta'
first_space = name.find(' ')
sub_str = name[:first_space]
print(sub_str)
'''

# Removing Spaces from String
# strip(), rstrip(), lstrip() --> covered in "PY4E Course2 - python data structures" extensively

# Finding Substring : Backward Direction --> rfind(), rindex()
'''
name = 'shubham kumar gupta'
# find(sub_str, begin, end) --> begin & end arguments are optional

# find() vs. rfind()
pos1 = name.find('m')
print(pos1)
pos2 = name.rfind('m')
print(pos2)
pos = name.find('m', pos1 + 1)
print(pos)
'''

# counting substring in a given string --> .count()
'''
user_input = input('Enter a Sentence: ')
sub_str = input('Enter a Sub String to Search for: ')
count_sub_str = user_input.count(sub_str)
print(count_sub_str)

sub_str_position_list = list()
i = 0
pos = None
while i <= len(user_input):
    pos = user_input.find(sub_str, i)
    if pos == -1:
        break
    else:
        sub_str_position_list.append(pos)
    # print(i)
    i = pos + 1
    # print(i)
print(sub_str_position_list)

# frequency of sub string in the first half of the string
print('first half frequency: ', user_input.count(sub_str, 0, int(len(user_input) / 2)))

# frequency of sub string in the second half of the string
print('second half frequency: ', user_input.count(sub_str, int(len(user_input) / 2), len(user_input)))
'''

# Replacing a String with Another String --> .replace()
'''
# help(str.replace)
user_input = input('Enter a Sentence: ')
replace_old = input('Enter Old Sub-string: ')
replace_new = input('Enter New Sub-string: ')
new_str = user_input.replace(replace_old, replace_new)
print(new_str)
'''

# Splitting of String --> .split()
'''
user_input = input('Enter a Sentence: ')    # type: str
split_delimiter = input('Enter the Split Delimiter: ')    # type: str
split_str = user_input.split(split_delimiter)
print(split_str)
'''

# Joining of Strings
'''
user_input = input('Enter a Sentence: ')    # type: str
split_delimiter = input('Enter the Split Delimiter: ')    # type: str
split_str = user_input.split(split_delimiter)
join_delimiter = input('Enter the Join Delimiter: ')
joined_str = join_delimiter.join(split_str)
print(joined_str)
'''

# Changing Case of a String
# .upper(), .lower(), .capitalize(), .title(), swapcase()
'''
input_str = input('Enter a String: ')
str_upper = input_str.upper()
print(str_upper)

input_str = input('Enter a String: ')
str_lower = input_str.lower()
print(str_lower)

input_str = input('Enter a String: ')
str_capitalized = input_str.capitalize()
print(str_capitalized)

input_str = input('Enter a String: ')
str_titled = input_str.title()
print(str_titled)

input_str = input('Enter a String: ')
str_swapcased = input_str.swapcase()
print(str_swapcased)
'''

# Checking Starting and Ending Part of a String
'''
input_str = input('Enter a String: ')
print(input_str.startswith('s'))
print(input_str.startswith('k'))
print(input_str.endswith('a'))
print(input_str.endswith('g'))
'''

# Checking Type of Characters Present in a String
# .isalpha(), .isalnum(),
'''
input_str = input('Enter a String: ')
print(input_str.isalpha())

input_str = input('Enter a String: ')
print(input_str.isdigit())

input_str = input('Enter a String: ')
print(input_str.isalnum())

input_str = input('Enter a String: ')
print(input_str.isnumeric())

input_str = input('Enter a String: ')
print(input_str.islower())

input_str = input('Enter a String: ')
print(input_str.isupper())
'''

input_str = input('Enter a String: ')
print(input_str.istitle())

input_str = input('Enter a String: ')
print(input_str.isspace())

# # write a program to print the type of character
# # provided by user as input
