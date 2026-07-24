# nparrays attributes

import numpy as np
a1 = np.arange(10)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8,dtype=int).reshape(2,2,2)

print(a1)
print(a2)
print(a3)

# ndim (returns dimentions of array)

print(a1.ndim)

print(a2.ndim)

print(a3.ndim)

# shape (returns shape of nparray)

print(a1.shape)
print(a3.shape)
print(a2.shape)

# size (returns no. of elements in an nparray)

print(a1.size)
print(a3.size)
print(a2.size)

# itemsize (returns the space occupied by the single item of nparray) (ex. single integer occupy 8bytes of space)

print(f"space occupied by single element in bytes of nparray is : ",a1.itemsize)


# astype (changing datatype of nparray)

print(a3.dtype)

a3.astype(np.int32)





