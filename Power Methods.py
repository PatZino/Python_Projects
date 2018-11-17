import numpy as np
from numpy import array


a = array([[5, -1, 7], [-1, -1, 1], [7, 1, 5]])
I = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
k = 1
N = 3
lists = []


def powerMethod(a):
    x = [1, 1, 1]
    z = [1, 1, 1]
    for i in range(N):
        y = np.matmul(a, x)
        maxval1 = np.amax(y)
        lists.append(maxval1)
        print("lists: ", lists)
        x = (1 / maxval1) * y
        if lists[i] != lists[i - 1]:
            yield x, maxval1


for eigenvector, eigenvalue in powerMethod(a):
    print("eigenvector = ", eigenvector, "eigenvalue = ", eigenvalue, "\n")

"""
    b = a - (maxval1 * I)
    print("B:", b, "\n")
    print("- "*50, "\n")

    for i in range(N):
        y = np.matmul(b, z)
        #  print("y = ", y)
        absVal = np.absolute(y)
        #  print("absVal: ", absVal)
        val3 = np.argmax(absVal)
        #  print("val3 = ", val3)
        lmda = y[val3]
        #  print("lmda : ", lmda)
        z = (1 / lmda) * y
        yield z, lmda
"""


