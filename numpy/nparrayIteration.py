import numpy as np

# =====Iteration====

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a4 = np.arange(27).reshape(3,3,3)

print(a1)
print(a2)
print(a4)

print(f"every element in a4 is listed below")

for i in np.nditer(a4):
    print(i)