print(__name__)  # __main__ ==> direct execution of Module3

if __name__ == '__main__':
    print('module3 executing directly just like main program')
else:
    print('module3 executing indirectly because of import statement')

def f1():
    print('f1 function')

def f2():
    print('f2 function')

def f3():
    print('f3 function')

def f4():
    print('f4 function')

if __name__ == '__main__':
    f1()
    f2()
    f3()
    f4()
