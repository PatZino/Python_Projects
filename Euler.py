import numpy as np


n = 6
h = 0.2


x = np.zeros([n])
y = np.zeros([n])
exact = np.zeros([n])
error = np.zeros([n])
y[0] = 0
x[0] = 0
for i in range(1, n):
    x[i] = x[i-1] + h
    y[i] = h*(y[i-1] + x[i-1]) + y[i-1]
    exact[i] = np.exp(x[i]) - x[i] - 1
    error[i] = exact[i] - y[i]

print("i", " "*2, "x", " "*5, "y", " "*10, "exact", " "*5, "error")
for i in range(n):
    print(i, format(x[i], '6f'), "\t", format(y[i], '6f'), "\t", format(exact[i], '6f'), "\t", format(error[i], '6f'))


