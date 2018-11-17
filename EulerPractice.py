import numpy as np


x0 = 0
y0 = 0
h = 0.2
n = 4

x = np.zeros(12)
y = np.zeros(12)
exact = np.zeros(12)
error = np.zeros(12)
x[0] = x0
y[0] = y0

for i in range(0, n):

    k1 = h * (x[i] + y[i])
    k2 = h * (x[i] + 0.5 * h + y[i] + 0.5 * k1)
    k3 = h * (x[i] + 0.5 * h + y[i] + 0.5 * k2)
    k4 = h * (x[i] + h + y[i] + k3)

    x[i+1] = x[i] + h
    y[i+1] = y[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)


def func(p, q):
    result = p + q
    return result


for i in range(n, 11):
    x[i+1] = x[i] + h
    a = 55 * func(x[i], y[i])
    b = 59 * func(x[i-1], y[i-1])
    c = 37 * func(x[i-2], y[i-2])
    d = 9 * func(x[i-3], y[i-3])
    y[i+1] = y[i] + (h/24)*(a - b + c - d)


print("i", " "*10, "x", " "*5, "y", " "*5, "exact", " "*6, "error", " "*6)
for i in range(0, 11):
    exact[i+1] = np.exp(x[i+1]) - x[i+1] - 1
    error[i+1] = exact[i+1] - y[i+1]
    print(i, "\t", format(x[i], "6f"), "\t", format(y[i], "6f"), "\t", format(exact[i], "6f"), "\t",
          format(error[i], "6f"), "\t",)