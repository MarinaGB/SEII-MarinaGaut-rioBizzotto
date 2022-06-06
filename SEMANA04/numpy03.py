import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([4,6,8,2])
print(a1)
a2 = np.zeros(10)
print(a2)
a3 = np.ones(4)
print(a3)
a4 = np.random.random(10)
print(a4)
a5 = np.random.randn(10)
print(a5)
a6 = np.linspace(0, 10, 100)
print(a6)
a7 = np.arange(0, 10, 0.2)
print(a7)

print(a1*2)

print(2*a1>10)

print(1/a4 + a4)


a1 = np.array([2,4,6,8,10])
print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[::2])
print(a1>3)
print(a1[a1>3])
print(a1%4)
print(a1%4==0)
print(a1[a1%4==0])

plt.plot(a6, a6**2)
plt.show()
plt.hist(a4)
plt.show()

def f(x):
    return x**2 * np.sin(x) / np.exp(-x)

plt.plot(a7, f(a7))
plt.show()


x = np.linspace(0, 10, 100)
y = f(x)

plt.plot(x,y)


names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])
first_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
print(names[first_letter_j])
d = np.vectorize(lambda s: s[0])(names)
print(d)