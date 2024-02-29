from patterns.shapes import *

# user's choice of pattern
pattern = input('Enter the pattern to print [square, right_angled_triangle, pyramid, hollow_diamond]: ')

# printing pattern
exec(pattern+'()')

