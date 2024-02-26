# Program 4: write a program to generate fake employee data for database testing

from random import *

# alphabets list
alphabets = []
for i in range(ord('A'),ord('Z')+1):
    alphabets.append(chr(i))
for i in range(ord('a'),ord('z')+1):
    alphabets.append(chr(i))

# digits str
digits = '0123456789'

# city option
cities = ['Hyderabad','Chennai','Bangalore','Pune','Delhi','Mumbai']

# designation options
designations = ['Software Engineer','Senior Software Engineer','Team Lead','Project Lead','Project Manager']

# Employee Name
def get_emp_name():
    # random length of employee name between 3 and 10
    emp_name_len = randint(3,10)
    # employee name generation
    emp_name = ''
    for i in range(emp_name_len):
        emp_name += choice(alphabets)
    # return statement
    return emp_name.title()

# Employee Number
def get_emp_no():
    # generating employee number
    emp_no = 'e-'
    for i in range(4):
        emp_no += choice(digits)
    # return statement
    return emp_no

# Employee salary
def get_emp_salary():
    # generating salary
    salary = round(uniform(10000,50000),2)
    # return statement
    return salary

# Employee Mobile Number
def get_emp_mob_no():
    # first digit
    mob_no = str(choice(range(6,10)))
    # remaining 9 digits
    for i in range(9):
        mob_no += str(choice(range(10)))
    # return statement
    return mob_no

# Employee City
def get_emp_city():
    # choosing employee city
    city = choice(cities)
    # return statement
    return city

# Employee Designation
def get_emp_designation():
    # choosing employee designation
    designation = choice(designations)
    # return statement
    return designation

def get_fake_emm_data():
    print('Employee Name: ',get_emp_name())
    print('Employee Number: ',get_emp_no())
    print('Employee salary: ',get_emp_salary())
    print('Employee City: ',get_emp_city())
    print('Employee Mobile Number: ',get_emp_mob_no())
    print('Employee Designation: ',get_emp_designation())

if __name__ == '__main__':
    # generating employee data for 1 employee
    # get_fake_emm_data()

    # generating employee data for n employees
    n = int(input('Enter the No. of Employees : '))
    for i in range(n):
        get_fake_emm_data()
        print()
