import string

firstname = 'Thirunavukkarasu'
lastname = 'Arumugam'

# Full name normal way
print('My Full name: ' + firstname+' ' + lastname)

# Full name format method
fn =  'My full name is: {} {}'.format(firstname,lastname)
print(fn)

# Full name using F string method
fn = f'My full name {firstname} {lastname.upper()}'
print(fn)

# to see all the methods of the str utility
print('Methods supported by STR')
print(dir(firstname))

# to see the details of the str methods
#print(help(str))
print('thiruna'.capitalize())
print('THIRUNA'.title())

# Ascii
print(string.digits)
print(string.octdigits)
print(string.hexdigits)

