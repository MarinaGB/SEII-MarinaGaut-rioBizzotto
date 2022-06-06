student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)

print(student['name'])

print(student.get('name'))

print(student.get('phone', 'Not found'))

student['phone'] = '555-5555'

student['name'] = 'Jane'

print(student)

student.update({'name': 'Jack', 'phone': '333-3333'})

print(student)

age = student.pop('age')

print(age)

print(student)

print(len(student))

print(student.keys())

print(student.items())

for key, value in student.items():
    print(key, value)