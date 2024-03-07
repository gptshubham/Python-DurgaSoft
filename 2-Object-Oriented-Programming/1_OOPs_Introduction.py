# class Student:
    # ''' doc_string '''  --> optional
    # Properties ( Variables) --> name, marks, roll no
    # actions (methods)

'''
class Student:
    def __init__(self):
        print('Constructor Execution...')
        self.name='shubham'
        self.rollno=101
        self.marks=98
    def talk(self):
        print('Hello I am',self.name)
        print('My Roll No. is',self.rollno)
        print('My Marks is',self.marks)

print(Student.__doc__)
# help(Student)

# creating object
s1 = Student()
s2 = Student()
# accessing object variables
print(s1.name)
print(s1.rollno)
print(s1.marks)
print(s2.name)
# calling method
s1.talk()

print(id(s1))
print(id(s2))
print(s1 is s2)


# Passing Value to Constructor
class Student:
    def __init__(self,name,rollno,marks): # parameters: self,name,rollono,marks
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def talk(self):
        print('Hello I am',self.name)
        print('My Roll No. is',self.rollno)
        print('My Marks is',self.marks)

s1 = Student('Abhi',100,99)
# TypeError: Student.__init__() takes 1 positional argument but 4 were given
# Error no longer exits after creating name,rollno and marks arguments for __init__()
print('Student 1:',s1.name,s1.rollno,s1.marks)
s2 = Student('Mohit',110,95)
print('Student 2:',s2.name,s2.rollno,s2.marks)


# Everything about Self Variable --> always refers to current object
class Test:
    def __init__(self):
        print('Id of object reffered by self:', id(self))

t = Test()
print('Id of object reffered by t:',id(t))
t1 = Test()
print('Id of object reffered by t1:',id(t1))
s1.talk()
s2.talk()


# self is not a keyword we can use any name instead of self
# However, it is recommended to use self : good programming practice
class Student:
    def __init__(dhoni, name, rollno, marks): # parameters: self,name,rollono,marks
        dhoni.name=name
        dhoni.rollno=rollno
        dhoni.marks=marks

    def talk(kohli):
        print('Hello I am', kohli.name)
        print('My Roll No. is', kohli.rollno)
        print('My Marks is', kohli.marks)

s = Student('shubham',120,91)
print(s.name,s.rollno,s.marks)


# whatever first argument we are using will act as self
class Test:
    def __init__(x):
        print('constructor')
        print('Id of object reffered by x:', id(x))

# t = Test(10)
# # TypeError: Test.__init__() takes 1 positional argument but 2 were given
# t1 = Test(x=10)
# # TypeError: Test.__init__() got multiple values for argument 'x'
t = Test()
print('Id of object reffered by t:',id(t))
'''


# Everything about Constructors

class Test:
    def __init__(self,count):
        print('Constructor Execution...',count)

t1 = Test(1)
t2 = Test(2)
t3 = Test(3)
t4 = Test(4)
t5 = Test(5)

# main purpose of Constructor --> Instance Variable
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

s1 = Student('Shubham',101,91)

# s2 = Student('Abhi',102,95,'male')
# TypeError: Student.__init__() takes 4 positional arguments but 5 were given
# s3 = Student('Mohit',103)
# TypeError: Student.__init__() missing 1 required positional argument: 'marks'

# Constructor is Optional
class Test:
    def m1(self):
        print('Method Execution...')

t = Test()
t.m1()

# Calling Constructor Explicitly
class Test:
    def __init__(self,note):
        print('Constructor Execution...','Id:',id(self),note)

t = Test('object creation')
t.__init__('Calling Constructor Explicitly')
t.__init__('Calling Constructor Explicitly')

# Method or Constructor Overloading --> not supported by Python
# PVM will always consider only the most recent one
class Test:
    def __init__(self):
        print('no-arg constructor')
    def __init__(self,x):
        print('one-arg constructor')

# t = Test() --> Invalid
# TypeError: Test.__init__() missing 1 required positional argument: 'x'
t = Test(10)

class Test:
    def __init__(self,name):
        self.name=name

t = Test('Shubh')
print(t.name)
t.__init__('Abhi')
print(t.name)
t.__init__('Mohit')
print(t.name)

# Doubt : multiple classes , multiple methods, which one is gonna change
# if we call __init__() explicitly multiple times with different objects
# conclusion: depends on the object

class Test:
    def __init__(self,name):
        self.name=name

class Demo:
    def __init__(self,name):
        self.name=name

t = Test('Mohit')
d = Demo('David')
t.__init__('Shubh')   # Mohit will be replaced by Shubh
d.__init__('Abhi')    # David will be replaced by Abhi

# Doubt : what if we have a function and a class with same name
# not a good progrmming practice
def Test():
    print('Test Function...')

class Test:
    def Test(self):
        print('Test Method inside Test Class...')


t = Test()
t.Test()
Test()        # overwritten by Test Class
print(Test())
t.Test()

class Test:
    def Test(self):
        print('Test Method inside Test Class...')

def Test():
    print('Test Function...')


Test()
t = Test()
# t.Test()       # overwritten by Test() Function
# AttributeError: 'NoneType' object has no attribute 'Test'
print(t)         # function does not return anything

# Constructor vs Method --> Notes
# basis - Name, Execution, No. of Executions, Role
