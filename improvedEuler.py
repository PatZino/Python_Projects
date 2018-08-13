import numpy as np
from matplotlib import pyplot as plt
import math


x0 = 0
y0 = 0
n = 6
h = 0.2


x = np.zeros([n])
y = np.zeros([n])
exact = np.zeros([n])
error = np.zeros([n])

y[0] = y0
x[0] = x0


for i in range(0, n-1):
    x[i+1] = x[i] + h
    k1 = h * (x[i] + y[i])
    k2 = h * (x[i+1] + y[i] + k1)
    y[i+1] = y[i] + 0.5 * (k1 + k2)
    exact[i+1] = math.exp(x[i+1]) - x[i+1] - 1
    error[i+1] = exact[i+1] - y[i+1]

print("i", " "*4, "xi", " "*5, "yi", " "*8, "exact", " "*8, "error")
for i in range(n):
    print(i, " "*4,  round(x[i], 4), " "*4, round(y[i], 4), " "*7, round(exact[i], 4), " "*9, round(error[i], 4))


plt.plot(x, y, 'o')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("improved Euler's method")
plt.show()
