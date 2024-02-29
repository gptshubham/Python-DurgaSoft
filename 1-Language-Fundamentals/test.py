from patterns.shapes import *

'''
# ModuleNotFoundError: No module named 'patterns'
# The above error no longer exits after installing patterns package using pip
'''

# user's choice of pattern
pattern = input('Enter the pattern to print [square, right_angled_triangle, pyramid, hollow_diamond]: ')

# printing pattern
exec(pattern+'()')

