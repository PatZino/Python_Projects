import numpy as np
from numpy import array

a = array([[4, 0,5 ], [1, 4, 2], [3, 0, 4]])
I = array([[1,0,0], [0,1,0], [0,0,1]])


def powermethod(a):
    x = [1, 1, 1]
    z = [1, 1, 1]
    for i in range(30):
        y = np.matmul(a, x)
        absy = np.absolute(y)
        maxindex = np.argmax(absy)
        lmbd = y[maxindex]
        x = (1/lmbd) * y
        yield x, lmbd

    print("-" * 70)
    B = a - (lmbd * I)
    print("B = ", B)
    print("-"*70)

    for i in range(30):
        y = np.matmul(B, z)
        absy1 = np.absolute(y)
        maxindex1 = np.argmax(absy1)
        lmbd1 = y[maxindex1]
        z = (1 / lmbd1) * y
        yield z, lmbd1


for eigenvector, eigenvalue in powermethod(a):
    print("eigenvector= ", eigenvector, "\t", "eigenvalue= ", format(eigenvalue, "6f"))
