nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num, "números de 1 a 5")

for num in nums:
    if num == 3:
        print('Achado número 3!')
        break
    print(num)

for i in range(1, 11):
    print(i, "número de 1 a 10")

x = 0

while x < 5:
    print(x, "0 até 4")
    x+=1

x = 0

while True:
    if x == 3:
        break
    print(x)
    x+=1