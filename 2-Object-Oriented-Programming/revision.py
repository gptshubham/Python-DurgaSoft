# Session 74 : Class, Object and Reference Variable
'''
# Student Class Example
class Student:
    """This class is developed by Shubham for Demo Purpose"""
    # variable --> attribute/ property
    # method --> behaviour/ actions

print(Student.__doc__)
help(Student)
'''

# Student Class (not a full-fledged example)
'''
class Student:
    def __init__(self):
        print('Constructor Execution...')
        self.name = 'Shubham'
        self.roll_no = 91
        self.marks = 100
    def talk(self):
        print(f'Hello I am: {self.name}')
        print(f'My Roll Number is: {self.roll_no}')
        print(f'My Marks are: {self.marks}')


s1 = Student()
print(s1.name, s1.roll_no, s1.marks)
s1.talk()
# print(s.__doc__)
# help(Student)
s2 = Student()
print(s1.name, s1.roll_no, s1.marks)
print(id(s1))
print(id(s2))
'''
