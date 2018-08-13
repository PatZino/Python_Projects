import numpy as np
import math


n = 4
N = 12
h = 0.2
x = np.zeros([N])
y = np.zeros([N])
w = np.zeros([N])


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
    # print(round(d, 6))
    return d


for i in range(0, n):
    y[i] = afunction(x[i], y[i])


for i in range(n, N-1):
    w[i] = 0.222107 + (h / 24) * (55 * y[i-1] - 59 * y[i-2] + 37 * y[i-3] - 9 * y[i-4])
    print("w[", i, "] = ", round(w[i], 6))
