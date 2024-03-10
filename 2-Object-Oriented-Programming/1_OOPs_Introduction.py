"""
class Student:
    ''' doc_string '''  # optional
    #Properties ( Variables)  # name, marks, roll no
    #actions (methods)
print(Student.__doc__)
help(Student)
"""

# Syntactical Example of a Class and Objects
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
'''

# Passing Value to Constructor
'''
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
s1.talk()
s2.talk()
'''

# Everything about Self Variable --> always refers to current object
'''

class Test:
    def __init__(self):
        print('Id of object reffered by self:', id(self))

t = Test()
print('Id of object reffered by t:',id(t))
t1 = Test()
print('Id of object reffered by t1:',id(t1))


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
'''
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
'''

# Method or Constructor Overloading --> not supported by Python
'''
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
'''

# Doubt : multiple classes , multiple methods, which one is gonna change
# if we call __init__() explicitly multiple times with different objects
# conclusion: depends on the object
'''
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
'''

# Doubt : what if we have a function and a class with same name
# not a good progrmming practice
'''
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
'''

# Mini Application : Movie
"""
class Movie:
    '''Movie Class developed by Shubham for Python demo purpose'''
    def __init__(self, title, hero, heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print('Movie Name:',self.title)
        print('Hero:',self.hero)
        print('Heroine:',self.heroine)

# creating multiple objects of Movie Class with Dynamic Information
list_of_movies = []
while True:
    title = input('Enter movie name: ')
    hero = input('Enter Hero of the movie: ')
    heroine = input('Enter heroine of the movie: ')
    m = Movie(title,hero,heroine)
    list_of_movies.append(m)
    print('Movie added to the list successfully!')
    option = input('Add Another Movie [Yes|No]: ')
    if option.lower() == 'no':
        break

print('All Movies Information...')
print('#'*40)
for movie in list_of_movies:
    movie.info()
    print()


m1 = 'Bahubali Prabhas Anushka'
m2 = 'Sultan Salman Anushka'
m3 = 'Jawan SRK Nayanthara'
m4 = 'Dangal Aamir Fatima Sana Shaikh'
"""

# Types of Variables --> instance , static and local
'''
# Instance Variable --> value varies from object to object
class Student:
    def __init__(self,name='Guest',rollno=0):
        self.name=name          # instance variable
        self.rollo=rollno       # instance variable

s = Student('Shubham',101)
# accessing the value of instance variable
print(s.name)
print(s.rollo)

# Static Variable --> value is constant for all objects
class Student:
    collegeName = 'IIT Madras'  # static variable
    def __init__(self,name='Guest',rollno=0):
        self.name=name         # instance variable
        self.rollo=rollno      # instance variable

# accessing the value of static variable
print(Student.collegeName)   # --> Recommended
s = Student()
print(s.collegeName)
# no need to create object to access static variables hence not recommended

# Local Variable --> declared inside a method directly
# to meet temporary requirements of the programmer

class Student:
    collegeName = 'IIT Madras'  # static variable
    def __init__(self,name='Guest',rollno=0):
        self.name=name          # instance variable
        self.rollo=rollno       # instance variable
    def m1(self):
        x = 10                 # x is local variable
        for i in range(x):     # i is local variable
            print(i,end=' ')
        print()

s = Student()
s.m1()
'''

# Types of Methods
'''
# Instance Method --> uses at least one instance variable
class Student:
    collegeName = 'IIT Madras'
    def __init__(self,name='Guest',rollno=0):
        self.name=name
        self.rollo=rollno

    def getStudentInfo(self):
        print('Student Name:',self.name)
        print('Student RollNo:',self.rollo)

s = Student('Abhi',102)
print('calling instance methods...')
s.getStudentInfo()
# Student.getStudentInfo()
# TypeError: Student.getStudentInfo() missing 1 required positional argument: 'self'
'''

# If Method uses no instance variable --> class method or static method

# Class Method --> uses any class variable and @classmethod
'''
class Student:
    collegeName = 'IIT Madras'
    director = 'Andrew Thangaraj'
    def __init__(self,name='Guest',rollno=0):
        self.name=name
        self.rollo=rollno

    def getStudentInfo(self):
        print('Student Name:',self.name)
        print('Student RollNo:',self.rollo)

    @classmethod
    def getCollegeInfo(cls):
        print('College Name:',cls.collegeName)
        print('Director:',cls.director)

s = Student('Shubham',101)
print('calling instance methods...')
s.getStudentInfo()
print('Calling Class Method...')
s.getCollegeInfo()


# cls memory address vs. class memory address
class Test:
    @classmethod
    def m1(cls):
        print(id(cls))

    @classmethod
    def m2(cls):
        print(id(cls))

print('cls memory address vs. class memory address...')
print(id(Test))
Test.m1()
Test.m2()
'''

# Static Methods --> No Instance or Static Variables used
'''
class Student:
    collegeName = 'IIT Madras'
    director = 'Andrew Thangaraj'
    def __init__(self,name='Guest',rollno=0):
        self.name=name
        self.rollo=rollno

    def getStudentInfo(self):
        print('Student Name:',self.name)
        print('Student RollNo:',self.rollo)

    @classmethod
    def getCollegeInfo(cls):
        print('College Name:',cls.collegeName)
        print('Director:',cls.director)

    @staticmethod
    def getScore(math,stat,eng,python):
        return (math+stat+eng+python)/4

s = Student('Shubham',101)
print('Calling Instance Methods...')
s.getStudentInfo()
print('Calling Class Method...')
Student.getCollegeInfo()
print('Calling Static Method...')
score = Student.getScore(95,95,98,90)
print('Average Score:',score)
# Everything about Instance Variable
'''

# Everythind about Instance Variables

# How to declare Instance Variables
'''
class Test:
    def __init__(self,a,b):     # inside constructor using self
        self.a = a
        self.b = b
    def m1(self,c):             # inside instance method using self
        self.c = c

# t1 object
t1 = Test(10,20)
print(t1.__dict__)
t1.m1(30)
print(t1.__dict__)
t1.d = 40                       # outside of the class using object reference
t1.e = 50
print(t1.__dict__)

# t2 object
t2 = Test(111,222)
print(t2.__dict__)
t2.d = 444
print(t2.__dict__)
'''

# How to access Instance Variables
'''
class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def m1(self):
        print(self.a)            # accessing instance variable within the class
        print(self.b)

t = Test(10,20)
t.m1()
print(t.a)                      # accessing instance variable within the class
print(t.b)
'''

# How to delete Instance Variables
'''
class Test:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def m1(self):
        del self.a              # deleting instance variable within the class

t = Test(10,20,30,40)
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.b,t.c                   # deleting instance variable from outside the class
print(t.__dict__)
'''

'''
# Instance Variable deleted form one object will not be deleted from other object
class Test:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def m1(self):
        del self.a

t1 = Test(10,20,30,40)
del t1.a
print(t1.__dict__)
t2 = Test(11,22,33,44)
print(t2.__dict__)
'''

'''
# Changing the values of instance variable of one object won't affect the values for the remaining objects
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

t1 = Test()
t2 = Test()
t1.a = 888
t1.b = 999
print(t1.__dict__)
print(t2.__dict__)
'''

# Everything about Static Variables - Declaration, Access, Update, Deletion

# Where and How to Declare Static Variables
'''
class Test:
    a = 10    # within the class directly but outside of any method (generally)
    def __init__(self):
        Test.b = 20      # within the constructor using class name

    def m1(self):        # within instance method using class name
        Test.c = 30

    @classmethod
    def m2(cls):        # within class method using class name or cls
        Test.d = 40
        cls.e = 50

    @staticmethod       # within static method using class name    
    def m3():           # (not recommended: not a good programming practice)
        Test.f = 70

print(Test.__dict__)
t = Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.g = 80
print(Test.__dict__)    # outside the class using class name 
'''

# How to Access Static Variables:
'''
# using class name to access static variables is good programming practice
class Test:
    a = 10
    def __init__(self): # within constructor using self or class name
        Test.b = 20
        print('within constructor using self:',self.a)
        print('within constructor using class name(recommended):',Test.a)
    def m1(self):       # within instance method using self or class name
        Test.c = 30
        print('within instance method using self:',self.a)
        print('within instance method using class name (recommnded):',Test.a)
    @classmethod
    def m2(cls):        # within class method using class name or cls
        Test.d = 40
        cls.e = 50
        print('within class method using cls:',cls.a)
        print('within class method using class name:',Test.a)
    @staticmethod       # within static method using class name
    def m3():           # (not recommended: not a good programming practice)
        Test.f = 70
        print('within static method using class name',Test.a)
    
print('Accessing Static Variables...')
t = Test()
t.m1()
Test.m2()
Test.m3()
print('Outside the class using class name:',Test.a)
'''

# How to Update the value of Static Variable
'''
class Test:
    a = 10
    def __init__(self):
        # within the constructor using class name
        print(Test.a)
        Test.a = 20
        print(Test.a)
    def m1(self):
        # within instance method using class name
        Test.a = 30
        print(Test.a)
    @classmethod
    def m2(cls):
        # within class method using class name or cls
        Test.a = 40
        print(cls.a)
        cls.a = 50
        print(cls.a)
    @staticmethod
    def m3():
        # within static method using class name
        # (not recommended: not a good programming practice)
        Test.a = 60
        print(Test.a)

t = Test()
t.m1()
Test.m2()
Test.m3()
# Outside the Class using Class Name
Test.a = 70
print(Test.a)
'''

# Tricky Example 1
'''
class Test:
    x = 10
    def __init__(self):
        self.y = 20

t1 = Test()
t2 = Test()
print('t1:',t1.x,t1.y)
print('t1 instance variables:',t1.__dict__)
print('t2:',t2.x,t2.y)
print('t2 instance variables:',t2.__dict__)
t1.x = 888              # new instance variable 'x' is created
t1.y = 999
print('t1:',t1.x,t1.y)
print('t1 instance variables:',t1.__dict__)
Test.x = 888
print('t2:',t2.x,t2.y)
print('t2 instance variables:',t2.__dict__)
'''

# Tricky Example 2
'''
class Test:
    x = 10
    def __init__(self):
        self.y = 20

    def m1(self):
        self.x = 888
        self.y = 999

t1 = Test()
t2 = Test()
t1.m1()
print('t1:',t1.x,t1.y)      # 888 999
print('t1 instance variables:',t1.__dict__)
print('t2:',t2.x,t2.y)      # 10 20
print('t2 instance variables:',t2.__dict__)
'''

# Tricky Example 3
'''
class Test:
    x = 10
    def __init__(self):
        self.y = 20

    @classmethod # remove this decorator and see the magic - head spinning effet
    def m1(cls):
        cls.x = 888
        cls.y = 999

t1 = Test()
t2 = Test()
print('t2:',t2.x,t2.y)      # 10 20
print('t2 instance variables:',t2.__dict__)
t1.m1()
print('t1:',t1.x,t1.y)      # 888 20
print('t1 instance variables:',t1.__dict__)
print('t2:',t2.x,t2.y)      # 888 20
print('t2 instance variables:',t2.__dict__)
print('Static Variables:',Test.x,Test.y)
'''
