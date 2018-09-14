import numpy as np
import math
import random


"""
def summation(x):
    Sum = sum(x ** 2)
    return Sum / len(x)


a = [1, 2, 3, 4, 5]
#  print("sum = ", summation())
"""


def ackley (x, a=20, b=0.2, c=2*np.pi):
    firstPart = 0
    secondPart = 0
    for i in range(len(x)):
        firstPart += -b * ((x[i] ** 2) * 0.5)
        secondPart += np.cos(c * x[i])
        result = -a * np.exp(firstPart) - np.exp(secondPart) + a + np.exp(1)
    return result


#  d = ackley(2)
#  print("d = ", d)


def ackley2D (x, y):
    a = 20
    b = 0.2
    c = 2*np.pi
    firstPart = 0
    secondPart = 0
    for i in range(len(x)):
        firstPart += (-b * (((x[i] ** 2) * 0.5) + ((y[i] ** 2) * 0.5)))
        secondPart += (np.cos(c * x[i]) + np.cos(c * y[i]))
        #  result = -a * np.exp(firstPart) - np.exp(secondPart) + a + np.exp(1)
    return -a * np.exp(firstPart) - np.exp(secondPart) + a + np.exp(1)


alist = ['a1', 'a2', 'a3']
blist = ['235', '456', '239']

for i, a in enumerate(alist):
    print(i, a)


print("*"*50)

for j, b in alist:
    print(j, b)


print("*"*50)

for j, b, c in blist:
    print(j, b, c)


print("*"*50)


pop = [-0.1, -0.2, -0.3, 0.4, -0.5, -0.6]
pop2 = [3, -5, -5, -5,  3]

fitness = [ackley2D(ind1, ind2)for ind1 in [pop] for ind2 in [pop]]
fitness2 = ackley(pop)
fitness3 = ackley(pop2)

print("fitness = ", fitness)
print("fitness2 = ", fitness2)
print("fitness3 = ", fitness3)
"""
b = np.cos(np.radians(60))
print("b = ", b)

c = math.sin(math.radians(30))
print("c = ", c)

d = np.power(3, 2)
print("d = ", d)
"""
"""
def objective_function(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]**2
        print("sum = ", sum)
        print("len of x = ", len(x))
    return sum / len(x)


a = objective_function([1, 2, 3])
print("a = ", a)

F = 0.6
x1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
x2 = np.array([5, 3, 2, 7, 9, 13, 17, 19, 20, 25])
x3 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

d = x1 - x2
print(d)

mutation = x1 + (F * (x3 - x2))
print("mutation = ", mutation)

a = np.zeros([10])
b = np.zeros([10])
c = np.zeros([10])

for i in range(10):
    a[i] = i
    b[i] = 3 * i


for i in range(10):
    print("a[", i, "]= ", a[i], "\t", "b[", i, "]= ", b[i])
    c[i] = b[i] - a[i]
    print("b - a = ", c[i], "\n")


# Random float in [0.0, 1.0)
y = random.random()
print("y = ", y)

# Random float in [0, 5]
x = random.uniform(0, 5)
print("x = ", x)

# Random integer in [0, 5]
z = random.randint(0, 5)
print("x = ", z)


n = 5

print("\n")
for j in range(0, n):
    print(j)
print("_"*50)

r = int(input("enter the radius: "))
area = math.pi * math.pow(r, 2)
print("area of circle: ", round(area, 2))

print("_"*50)
print(math.pi)


input("Press the enter key to find out.")
print("107 % 4 = ", 107 % 4)
print("3 % 2 = ", 3 % 2)
print("1 % 2 = ", 1 % 2)
print("1 / 2 = ", 1 / 2)
print("3 / 2 = ", 3 / 2)
print("107 / 4 = ", 107 / 4)
print("107 // 4 = ", 107 // 4)
print("*"*50)


def halton(i, j):
    prime = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    p1 = prime[j]
    print("p1 = ", p1)
    p2 = p1
    print("p2 = ", p2)
    sum = 0

    while i > 0:
        x = i % p1  # % is the module operator
        print("x = ", x)
        sum = sum + x / p2
        print("sum = ", sum)
        i = math.floor(i / p1)
        print("i = ", i)
        p2 = p2 * p1
        print("p2 = ", p2)
    return sum


print("halton(3, 0) = ", halton(3, 0))

print("*"*50)
# Euclid Algorithm


def euclid(a, b):
    if a == 0:
        return b
    return euclid(b % a, a)


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("answer = ", euclid(a, b))
"""
