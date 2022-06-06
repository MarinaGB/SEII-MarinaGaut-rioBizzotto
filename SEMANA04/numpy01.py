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


