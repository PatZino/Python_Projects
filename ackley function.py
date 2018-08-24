import numpy as np
from matplotlib import pyplot as plt


"""
a = 20
b = 0.2
c = 2 * np.pi


def ackley(x):
    first = (1/(len(x)) * sum(x ** 2)) ** 0.5
    second = 1/(len(x)) * sum()
"""


def ackley2d(x, y, a=20, b=0.2, c=2*np.pi):
    d = 2
    sum1 = x**2 + y**2
    sum2 = np.cos(c*x) + np.cos(c*y)
    term1 = -a * np.exp(-b*np.sqrt(sum1/d))
    term2 = -np.exp(sum2/d)
    s = term1 + term2 + a + np.exp(1)
    print("s = ", s)
    return s


fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection='3d')
x = np.linspace(-20, 20, 200)
print("x  = ", x)
y = x
print("y  = ", y)
X,Y = np.meshgrid(x, y)
Z = ackley2d(X, Y)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm,
        linewidth=0, antialiased=False)

#ax.set_zlim(0, 0.2)

ax.zaxis.set_major_locator(plt.LinearLocator(10))
ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.01f'))

fig.colorbar(surf, shrink=0.5, aspect=7, cmap=plt.cm.coolwarm)

plt.show()
