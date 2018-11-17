import numpy as np
from numpy import array


A = array([[5, -1, 7], [-1, -1, 1], [7, 1, 5]])
I = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
k = 1

def powerMethod(A):
    x = [1, 1, 1]
    z = [1, 1, 1]
    for i in range(30):
        y = np.matmul(A, x)
        absy = np.absolute(y)
        indexy = np.argmax(absy)
        maxval = y[indexy]
        x = (1/maxval) * y
        yield x, maxval

    B = A - (maxval*I)
    print("-"*50)
    for i in range(30):
        y = np.matmul(B, z)
        absy1 = np.absolute(y)
        indexy1 = np.argmax(absy1)
        maxval1 = y[indexy1]
        z = (1 / maxval1) * y
        yield z, maxval1

for eigenvector, eigenvalue in powerMethod(A):
    print("eigenvector= ", eigenvector, "\t", "eigenvalue= ", format(eigenvalue, "6f"))
