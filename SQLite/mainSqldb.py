import sqlite3

from employee import Employee

# This is in-memory sqlite db type. It runs every time the file runs.
# conn = sqlite3.connect(':memory:')

# employee.db file will be created and it is the database file where are the database code gets stored.
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# create table statement
# c.execute ('DROP TABLE EMPLOYEE')

sql_stmt = 'CREATE TABLE EMPLOYEE (FIRSTNAME TEXT, LASTNAME TEXT, PAY INTEGER)'


# c.execute(sql_stmt)


def insertion(emp):
    with conn:
        c.execute('INSERT INTO EMPLOYEE VALUES (:FIRST, :LAST, :PAY)',
                  {'FIRST': emp.firstname, 'LAST': emp.lastname, 'PAY': emp.pay})


def deletion(firstname=None):
    with conn:
        if firstname is None:
            c.execute('delete from employee')
        else:
            c.execute('delete from employee where firstname = ?', (firstname,))


def update(fname, setto):
    with conn:
        c.execute('update employee set lastname = :lastname where firstname = :firstname', {'lastname': setto, 'firstname': fname})


# INSERT the data into Employee table

# 1.  Create an instance of the employee class
emp_1 = Employee('Thiru', 'Arumugam', 100000)
emp_2 = Employee('Arasu', 'Arumugam', 20000)
emp_3 = Employee('Anitha', 'Cherian', 500000)
emp_4 = Employee('Gsg', 'Singh', 2300)
emp_5 = Employee('Roshan', 'Kumar', 4000)
# 2. Insert the value object to the function 'insertion'
insertion(emp_1)
insertion(emp_2)
insertion(emp_3)
insertion(emp_4)
insertion(emp_5)

print(' AFTER Insertion ...')
c.execute('select * from employee')
print(c.fetchall())

# DELETE the data from employee table.
print(' AFTER Deletion ...')
deletion('Thiru')
# deletion()

# UPDATE the data in employee table.
update('Gsg','Gaharwar')
c.execute('select * from employee')
print(c.fetchall())

# conn.commit()
# conn.close()
