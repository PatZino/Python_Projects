import numpy as np
from numpy import array
from numpy import linalg as LA

a = array([[10, 7, 8, 7], [7, 5, 6, 5], [8, 6, 10, 9], [7, 5, 9, 10]])
I = array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
k = 1


def modifiedPowerMethod(a):
    x = [0.5, 0.5, 0.5, 0.5]
    z = [0.5, 0.5, 0.5, 0.5]
    #  innerAddition = 0
    for i in range(6):
        y = np.matmul(a, x)
        #  print("y = ", y)
        ld2 = np.matmul(x, y)
        #  print("ld2: ", ld2)
        x = y / (LA.norm(y))
        yield x, ld2
    """
        maxval1 = np.matmul(x, y)
        inner = np.square(y)
        #  print("inner: ", inner)
        for j in range(len(y)):
            innerAddition += inner[j]
        #  print("innerAddition: ", innerAddition)
        euclidean = np.sqrt(innerAddition)
        print("euclidean = ", euclidean)
        x = y / euclidean
        """
    b = a - (ld2 * I)
    print("B:", b)
    print("- " * 50)

    for i in range(6):
        y1 = np.matmul(b, z)
        #  print("y = ", y1)
        ld = np.matmul(z, y1)
        #  print("ld: ", ld)
        z = y1 / (LA.norm(y1))
        yield z, ld


for eigenvector, eigenvalue in modifiedPowerMethod(a):
    print("eigenvector = ", eigenvector, "eigenvalue = ", eigenvalue, "\n")
