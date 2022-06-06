language = 'Python'

if language == 'Python':
    print('Conditional was true')
else:
    print('Conditional was false')


language = 'C++'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

user = 'Admin'

logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')


if not logged_in:
    print('Please log in')
else:
    print('Wellcome')


a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))

print(id(b))

print(a is b)

a = [1, 2, 3]
b = a

print(id(a))

print(id(b))

print(a is b)

condition = 'Test'

if condition:
    print('Evaluated to true')
else:
    print('Evaluated to false')