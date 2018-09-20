import numpy as np


a = [[10, 7, 8, 7], [7, 5, 6, 5], [8, 6, 10, 9], [7, 5, 9, 10]]
maxval = 0
k = 1


def modifiedPowerMethod(a):
    x = [0.5, 0.5, 0.5, 0.5]
    innerAddition = 0
    for i in range(6):
        y = np.matmul(a, x)
        print("y = ", y)
        maxval1 = np.matmul(x, y)
        inner = np.square(y)
        #  print("inner: ", inner)
        for j in range(len(y)):
            innerAddition += inner[j]
        #  print("innerAddition: ", innerAddition)
        euclidean = np.sqrt(innerAddition)
        print("euclidean = ", euclidean)
        x = y / euclidean
        yield x, maxval1


for eigenvector, eigenvalue in modifiedPowerMethod(a):
    print("eigenvector = ", eigenvector, "eigenvalue = ", eigenvalue, "\n")
