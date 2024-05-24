# Function Aliasing, Nested Functions, Higher Order Functions , Decorator Function
'''
def calc(a,b):
    print(f'The Sum : {a+b}')
    print(f'The Difference : {a-b}')
    print(f'The Product : {a*b}')
    print(f'The Dividend : {round((a/b),2)}')

calc(20,3)
print()
calc(200,10)
print()
calc(40,7)

# In Python , everything is an object, even function.
print(calc)
print(id(calc))
print(type(calc))
print()
# calc is a variable name referring to a function object

# Function Aliasing
new_calc = calc
new_calc(30,8)
print()
del calc
new_calc(20,4)
'''

# Nested Functions
'''
def outer():
    print('outer function started')
    def inner():
        print('inner function execution')
    print('outer function completed')
outer()
print()

def outer():
    print('outer function started')
    def inner():
        print('inner function execution')
    inner()
    inner()
    inner()
    print('outer function completed')
outer()
print()

# inner()
# NameError: name 'inner' is not defined
'''

# outer function can return inner function --> Higher Order Function
'''
def outer():
    print('outer function started')
    def inner():
        print('inner function execution')
    print('outer function returning inner function')
    return inner

outer()
print()

newf = outer()      # newf = inner
newf()
newf()
newf()
newf()
newf()
print()

# Tricky Doubt - what if outer() returns inner() instead of inner
def outer():
    print('outer function started')
    def inner():
        print('inner function execution')
    print('outer function returning inner function')
    return inner()

newf = outer()
print(newf)
print()

# Passing function as argument to another function --> Higher Order Function
def f1(func):
    print(f'f1 function got {func} function as argument')
    func()

def fx():
    print('fx function execution')

def fy():
    print('fy function execution')

f1(fx) # we are calling f1() by passing fx function as argument
print()
f1(fy)
'''

# Decorator Function

# Theoretical Example
'''
def decor(func):
    def inner():
        print('send person to Beauty Parlour')
        print('showing a person with full decoration')
    return inner

# function without decorator
def display():
    print('Showing a person as it is')

display()        # display() function is executed
print()

# function with decorator
@decor
def display():
    print('Showing a person as it is')

display()         # inner() function is executed
print()
display()         # inner() function is executed
print()
display()         # inner() function is executed
print()
display()         # inner() function is executed
'''


# Basic Practical Example of Decorator
'''
def decor_for_add(func):
    def inner(x, y):      # No. of arguments must match with original functon add
        print('#' * 40)
        print(f'The sum of {x} and {y} is ', end='')
        func(x, y)        # Calling original function add
        print('#' * 40)
    return inner

# add function without decorator
def add(a, b):
    print(a + b)


add(10,20)
print()

# add function with decorator
@decor_for_add
def add(a, b):
    print(a + b)

add(10,20)
add(100,200)
add(1000,2000)
add(777,888)
'''

# Decorator Example : Spacial functionality for specific Entity
def decor_for_dhoni(func):
    def inner(name):
        names = ['Dhoni', 'Kohli', 'Rohit', 'Sachin']
        if name in names:
            print('#' * 40)
            print(f'Hello {name}!')
            print('I am your Biggest Fan!')
            print(f'Love You {name}.')
            print('#' * 40)
        else:
            func(name)
    return inner


@decor_for_dhoni
def wish(name):
    print(f'Hello {name}!')


wish('python')
wish('Dhoni')
wish('Jaddu')
wish('Chahal')
wish('Pandya')
wish('Kohli')
wish('Rohit')


