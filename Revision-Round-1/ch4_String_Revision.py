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

input_str = input('Enter a String: ')
print(input_str.istitle())

input_str = input('Enter a String: ')
print(input_str.isspace())
'''

# Program 1 : write a program to reverse a given string
'''
input_str = input('Enter a string: ')
output_str = input_str[::-1]
print(output_str)
'''
# alternatively:
'''
output_str = reversed(input_str)
print(output_str)
print(type(output_str))
print(''.join(output_str))
print(type(''.join(output_str)))
'''

# Program 2 : write a program to Reverse Order of Words in a string
'''
input_str = input('Enter a String: ')
split_str = input_str.split()
reversed_words_list = split_str[::-1]
reversed_words_str = ' '.join(reversed_words_list)
print(reversed_words_str)
'''
# alternatively: using for loop and .append()
'''
input_str = input('Enter a String: ')
word = ''
word_list = list()
for i in range(len(input_str)):
    if i == len(input_str) - 1:
        word += input_str[i]
        # print(word)
        word_list.append(word)
        # print(word_list)
    if input_str[i] == ' ':
        word_list.append(word)
        # print(word_list)
        word = ''
    else:
        word += input_str[i]
    # print(word)
print(' '.join(word_list[::-1]))
'''

# Program 3 : write a program to reverse the internal content of each word
# Input : one two three
# Output : eno owt eerht
'''
input_str = input('Enter a String: ')
word = ''
word_list = list()
for i in range(len(input_str)):
    if i == len(input_str) - 1:
        word += input_str[i]
        word_list.append(word[::-1])
    if input_str[i] != ' ':
        word += input_str[i]
    else:
        word_list.append(word[::-1])
        word = ''
print(' '.join(word_list))
'''

# Program 4 : Reverse Internal Content of every second word
# Input : one two three four
# Output : one owt three ruof
'''
input_str = input('Enter a String: ')
word = ''
word_list = list()
count = 0
for i in range(len(input_str)):
    if i == len(input_str) - 1:
        word += input_str[i]
        count += 1
        if count % 2 == 0:
            word_list.append(word[::-1])
        else:
            word_list.append(word)
    if input_str[i] != ' ':
        word += input_str[i]
    else:
        count += 1
        if count % 2 == 0:
            word_list.append(word[::-1])
            word = ''
        else:
            word_list.append(word)
            word = ''
print(' '.join(word_list))
'''

# Program 5 : print characters at odd positions and even positions for any given string
# HINT: (possition => index)
'''
input_str = input('Enter a string: ')
even_pos_chars = ''
odd_pos_chars = ''
for i in range(len(input_str)):
    if i % 2 != 0:
        odd_pos_chars += input_str[i]
    else:
        even_pos_chars += input_str[i]
print('even position characters: ',even_pos_chars)
print('odd position characters: ',odd_pos_chars)
'''

# Program 6 :Merge characters of 2 strings into a single string by taking characters alternatively
'''
input_str_1 = input('Enter First String: ')
input_str_2 = input('Enter Second String: ')

min_length = len(input_str_1) if len(input_str_1) <= len(input_str_2) else len(input_str_2)

concated_str = ''

for i in range(min_length):
    concated_str += (input_str_1[i] + input_str_2[i])
print(concated_str)
'''

# alternatively: using while loop - complete concatenation
'''
input_str_1 = input('Enter First String: ')
input_str_2 = input('Enter Second String: ')

concated_str = ''
i = 0
while i < len(input_str_1) or i < len(input_str_2):
    if i < len(input_str_1):
        concated_str += input_str_1[i]
    if i < len(input_str_2):
        concated_str += input_str_2[i]
    i += 1

print(concated_str)
'''

# # Program 7:
# Input: ABCDEF and 123456
# Output: AA1BB2CC3DD4EE5FF6
'''
alphabets = input('Enter Alphabets: ')
digits = input('Enter a Number: ')

i = 0

output = ''
while i<len(alphabets) or i<len(digits):
    if i < len(alphabets):
        output += (alphabets[i].upper() * 2)
    if i < len(digits):
        output += digits[i]
    i += 1

print(output)
'''

# Program 8: write a program to sort alphanumeric characters present in the given string.
# First Alphabets and then Numeric Values : B4A1D3 --> ABD134
'''
input_str = input('Enter an AlphaNumeric String: ')
alpha = ''
digits = ''
for i in input_str:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        alpha += i
    else:
        print('Invalid Input!')
        break

output = sorted(alpha) + sorted(digits)
print(''.join(output))
'''

# Program 9:
# Input: a4b3c2 --> every alphabet symbol followed by a single digit
# Output: aaaabbbcc
'''
input_str = input('Enter an AlphaNumeric String: ')
char = ''
output = ''
for i in input_str:
    if i.isalpha():
        char = i
    elif i.isdigit():
        output += (char * int(i))

print(output)
'''

# Program 10:
# Input: a14b13c12 --> every alphabet symbol followed by a number
# Output: a*14 times + b*13 times + c*12 times
'''
input_str = input('Enter an Alphanumeric String: ')
alpha = ''
num = ''
output = ''
for i in range(len(input_str)):
    if input_str[i].isalpha():
        alpha = input_str[i]
    elif input_str[i].isdigit():
        num += input_str[i]
        if i + 1 == len(input_str):
            output += (alpha * int(num))
            print(f'from inside the loop : \n\tcount of {alpha} : {output.count(alpha)}')
        else:
            if input_str[i + 1].isalpha():
                output += (alpha * int(num))
                print(f'from inside the loop : \n\tcount of {alpha} : {output.count(alpha)}')
                alpha = ''
                num = ''

print(f'output after the loop is executed :\n\t{output}')
'''

# Program 11: Input: a4k3b2 --> Output: aeknbd
'''
input_str = input('Enter an Alphanumeric String: ')
alphabets = 'abcdefghijklmnopqrstuvwxyz'

char = ''
output = ''
for i in range(len(input_str)):
    if input_str[i].isalpha():
        output += input_str[i]
        char = input_str[i]
        # print(char)
    elif input_str[i].isdigit():
        index = alphabets.find(char) + int(input_str[i])
        # print(index)
        output += alphabets[index]
    else:
        print('Invalid Input!')

print(output)
'''

# Program 12: Remove duplicate characters from given string
# and sort the string
# Input: AAABAB DADBCDAD CACBC CCAACBD --> Output: ABCD
'''
input_str = input('Enter a String: ')
output = ''
for i in input_str:
    if i in output:
        continue
    else:
        output += i
output = ''.join(sorted(output.replace(' ','')))
print(output)
'''

# Program 13: Find No. of Occurrences of Each Character
# present in a given string in sorted order
'''
input_str = input('Enter a String: ')
d = dict()
for i in input_str:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
# print(d)

keys = sorted(d.keys())
# print(keys)

for i in keys:
    if i != ' ':
        print(i, d[i])
'''

