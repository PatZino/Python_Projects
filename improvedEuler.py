import numpy as np


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
    exact[i+1] = np.exp(x[i+1]) - x[i+1] - 1
    error[i+1] = exact[i+1] - y[i+1]

print("i", " "*2, "x", " "*5, "y", " "*10, "exact", " "*5, "error")
for i in range(n):
    print(i, format(x[i], '6f'), "\t", format(y[i], '6f'), "\t", format(exact[i], '6f'), "\t", format(error[i], '6f'))


