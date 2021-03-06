import numpy as np
from numpy import array


a = array([[5, -1, 7], [-1, -1, 1], [7, 1, 5]])
I = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
k = 1


def powerMethod(a):
    x = [1, 1, 1]
    z = [1, 1, 1]
    for i in range(30):
        y = np.matmul(a, x)
        #  print("y = ", y)
        maxval1 = np.amax(y)
        #  print("maxval1 = ", maxval1)
        x = (1 / maxval1) * y
        yield x, maxval1

    b = a - (maxval1 * I)
    print("B:", b, "\n")
    print("- "*50, "\n")

    for i in range(69):
        y = np.matmul(b, z)
        absVal = np.absolute(y)
        val3 = np.argmax(absVal)
        lmda = y[val3]
        z = (1 / lmda) * y
        yield z, lmda


for eigenvector, eigenvalue in powerMethod(a):
    print("eigenvector = ", eigenvector, "eigenvalue = ", format(eigenvalue, '6f'), "\n")




