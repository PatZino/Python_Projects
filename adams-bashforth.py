import numpy as np
import math


x0 = 0
y0 = 0
n = 4
h = 0.2

x = np.zeros([12])
y = np.zeros([12])
exact = np.zeros([12])

y[0] = y0
x[0] = x0

for i in range(0, n):
    k1 = h * (x[i] + y[i])
    k2 = h * (x[i] + 0.5*h + y[i] + 0.5*k1)
    k3 = h * (x[i] + 0.5*h + y[i] + 0.5*k2)
    k4 = h * (x[i] + h + y[i] + k3)

    x[i+1] = x[i] + h
    y[i+1] = y[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)


def afunction(p, q):
    result = p + q
    return result


for i in range(n, 11):
    x[i + 1] = x[i] + h
    a = 55 * afunction(x[i], y[i])
    b = 59 * afunction(x[i - 1], y[i - 1])
    c = 37 * afunction(x[i - 2], y[i - 2])
    d = 9 * afunction(x[i - 3], y[i - 3])
    e = (h / 24) * (a - b + c - d)
    y[i+1] = y[i] + e


print("i", "\t", "x[i]", "\t", "y[i]", "\t", "exact[i]")
for i in range(0, 11):
    exact[i + 1] = math.exp(x[i + 1]) - x[i + 1] - 1
    print(i, "\t", round(x[i], 1), "\t", round(y[i], 6),
          "\t", round(exact[i], 6))
