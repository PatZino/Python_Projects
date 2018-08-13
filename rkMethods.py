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
    k1 = h * (x[i] + y[i])
    k2 = h * (x[i] + 0.5*h + y[i] + 0.5*k1)
    k3 = h * (x[i] + 0.5*h + y[i] + 0.5*k2)
    k4 = h * (x[i] + h + y[i] + k3)

    x[i+1] = x[i] + h
    y[i+1] = y[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    exact[i + 1] = math.exp(x[i + 1]) - x[i + 1] - 1
    error[i + 1] = exact[i + 1] - y[i + 1]

print("i", " "*4, "xi", " "*5, "yi", " "*12, "exact", " "*12, "error")
for i in range(n):
    print(i, " "*4,  round(x[i], 6), " "*4, round(y[i], 6), " "*10, round(exact[i], 6), " "*9, round(error[i], 6))

plt.plot(x, y, 'o')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Runge-Kutta method")
plt.show()

