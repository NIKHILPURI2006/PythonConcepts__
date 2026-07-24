import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a4 = np.arange(27).reshape(3,3,3)

print(a1)
print(a2)
print(a4)

# Transpose (returns transpose of matrix)
print(np.transpose(a2)) 

# ravel (turns every array no matter whats the dim to 1d array)

print(np.ravel(a4))