import numpy as np

print("_"*50)

global p
p = np.zeros((3, 3))

for k in range(3):
    for l in range(3):
        p[k][l] = 4*l
        print(k, l)
    print("\n")

testP = np.array([p])
print(testP)

print("_"*50)


result = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(result)

print("_"*20, "Playing with numpy arrays", "_"*20)
a = np.zeros((2, 2))
print(a)

print("\n")

b = np.ones((3, 3))
print(b)

print("\n")

c = np.full((3, 3), 4)
print(c)

print("\n")

d = np.random.random((3, 3))
print(d)

print("\n")

e = np.eye(4)
print(e)
