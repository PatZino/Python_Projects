import numpy as np
from numpy import array
from numpy import linalg as LA

a = array([[10, 7, 8, 7], [7, 5, 6, 5], [8, 6, 10, 9], [7, 5, 9, 10]])
I = array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
k = 1


def modifiedPowerMethod(a):
    x = [0.5, 0.5, 0.5, 0.5]
    z = [0.5, 0.5, 0.5, 0.5]
    for i in range(6):
        y = np.matmul(a, x)
        ld2 = np.matmul(x, y)
        x = y / (LA.norm(y))
        yield x, ld2
    b = a - (ld2 * I)
    print("B:", b)
    print("- " * 50)

    for i in range(101):
        y1 = np.matmul(b, z)
        ld = np.matmul(z, y1)
        z = y1 / (LA.norm(y1))
        yield z, ld


for eigenvector, eigenvalue in modifiedPowerMethod(a):
    print("eigenvector = ", eigenvector, "eigenvalue = ", format(eigenvalue, '6f'), "\n")
