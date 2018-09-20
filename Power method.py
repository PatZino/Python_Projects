import numpy as np


a = [[5, -1, 7], [-1, -1, 1], [7, 1, 5]]

maxval = 0
k = 1


def powerMethod(a):
    x = [1, 1, 1]
    for i in range(20):
        y = np.matmul(a, x)
        print("y = ", y)
        maxval1 = np.amax(y)
        x = (1 / maxval1) * y
        yield x, maxval1


for eigenvector, eigenvalue in powerMethod(a):
    print("eigenvector = ", eigenvector, "eigenvalue = ", eigenvalue, "\n")
