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
        lmda = np.matmul(x, y)
        normy = LA.norm(y)
        x = y / normy
        yield x, lmda

    B = a - (lmda * I)
    print("-"*50)
    for i in range(6):
        y = np.matmul(B, z)
        lmda = np.matmul(z, y)
        normy = LA.norm(y)
        z = y / normy
        yield x, lmda


for eigenvector, eigenvalue in modifiedPowerMethod(a):
    print("eigenvector= ", eigenvector, "\t", format(eigenvalue, "6f"))