f = open('teste.txt', 'r')
print(f.name)
f.close()


f = open('teste.txt', 'r')
print(f.mode)
f.close()


with open('teste.txt', 'r') as f:
    pass
print(f.closed)


with open('teste.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)


with open('teste.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)


with open('teste.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)



with open('teste.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())

