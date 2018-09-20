import numpy as np

print("_"*50)

mat0 = np.arange(4).reshape((2, 2))
print("mat0: ", mat0)
maxval0 = np.amax(mat0, axis=0)
print("maxval0: ", maxval0)
maxval01 = np.amax(mat0, axis=1)
print("maxval01: ", maxval01)

print("_"*50)

mat1 = [[0, 1], [2, 3]]
mat2 = [1, 2]
matmul = np.matmul(mat1, mat2)
print("matmul = ", matmul)
maxval2 = np.amax(mat1, axis=0)
maxval3 = np.amax(mat1, axis=0)
print("maxval2: ", maxval2, "\n", "maxval3: ", maxval3)

print("_"*50)

mat3 = [[5, -1, 7], [-1, -1, 1], [7, 1, 5]]
mat4 = [1, 1, 1]
matmul = np.matmul(mat3, mat4)
print("matmul = ", matmul)
maxval = np.amax(matmul)
print("maxval: ", maxval)

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

p = np.zeros([5])
print(p)

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

print("\n")
x = np.linspace(0, 10, 10)
print("x = ", x)

print("\n")
print(1/6)
