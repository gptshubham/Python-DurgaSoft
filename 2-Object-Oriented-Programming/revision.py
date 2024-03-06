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