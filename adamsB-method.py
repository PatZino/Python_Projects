import numpy as np
import math


n = 3
h = 0.2
x = np.zeros([11])
y = np.zeros([11])


x[0] = 0
y[0] = 0

x[1] = 0.2
y[1] = 0.021400

x[2] = 0.4
y[2] = 0.091818

x[3] = 0.6
y[3] = 0.222107


def afunction(a, b):
    d = a + b
    return d


for i in range(n, 10):
    x[i + 1] = x[i] + h
    print("x", x)
    a = 9 * afunction(x[i - 3], y[i - 3])
    print("a", a)
    b = 37 * afunction(x[i - 2], y[i - 2])
    print("b", b)
    c = 59 * afunction(x[i - 1], y[i- 1])
    print("c", c)
    d = 55 * afunction(x[i], y[i])
    print("d", d)
    e = (h/24) * (d - c + b - a)
    print("e", e)
    y[i+1] = y[i] + e
    #  print("w", w)

for i in range(0, 10):
    print("y[i+1]", round(y[i+1], 6))