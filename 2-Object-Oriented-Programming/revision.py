'''
# let's recreate the Student class from scratch
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

s = Student()
print(s.name)
print(s.rollno)
print(s.marks)
s.talk()

s1 = Student()
s2 = Student()

print(id(s1))
print(id(s2))
print(s1 is s2)
'''

# Instance Variables
'''
class Test:
    def __init__(self):
        self.a = 10

    def m1(self):
        self.a = 20
        self.b = 30

    def m2(self):
        self.e = 60
        self.f = 70

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
t.a = 40
t.c = 50
print(t.__dict__)
# accessing instance variables
print(t.a,t.b,t.c)
'''

# Destructor
import time
class Test:
    def __init__(self):
        print('Object initialization...')

    def __del__(self):
        print('Resource deallocation and cleanup activities...')

t1 = Test()
t1=None
t2 = Test()
del t2
t3 = Test()
time.sleep(5)
print('End of Application')

