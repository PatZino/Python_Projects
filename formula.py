import numpy as np
import math

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
