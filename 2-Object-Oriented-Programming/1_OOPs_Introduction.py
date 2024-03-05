# class Student:
    # ''' doc_string '''  --> optional
    # Properties ( Variables) --> name, marks, roll no
    # actions (methods)

class Student:
    '''This class is developed by Shubham for Demo Purpose'''
    def __init__(self):
        print('Constructor Execution...')
        self.name = 'Shubham'
        self.rollno = 101
        self.marks = 91
    def talk(self):
        print('Hello I am',self.name)
        print('My Roll No. is',self.rollno)
        print('My Marks are',self.marks)

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


