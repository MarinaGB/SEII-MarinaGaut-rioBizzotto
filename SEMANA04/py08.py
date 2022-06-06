def hello_func():
    print("Chamando a função")

hello_func()

def hello_func_2(greeting):
    return '{} Função'.format(greeting)

print(hello_func_2('Chamar'))

def hello_func_3(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

print(hello_func_3('Hi', 'name'))
print(hello_func_3('Hi'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Atr', name='John', age=22)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap(2022))

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2022, 8))