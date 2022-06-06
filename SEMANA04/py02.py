message = 'Hello World'

message2 = message.replace('World', 'Universe')

print(message2)

name = 'Michael'

greeting = 'Hello'

message3 = greeting + ', ' + name + '. Welcome!'

print(message3)

message4 = '{}, {}. Welcome!'.format(greeting, name)

print(message4)

message5 = f'{greeting}, {name.upper()}. Welcome!'

print(message5)

print(dir(name))